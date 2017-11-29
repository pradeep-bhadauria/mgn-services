import datetime, uuid

from flask import Blueprint, request, redirect, make_response, url_for
from mgn.utils.token import generate_confirmation_token, confirm_token
from mgn.utils.constants import *
from mgn.utils.general_response import *
from mgn.utils.emails import account_verification, change_password_verification
from mgn.utils.validations import *
from voluptuous import Schema, Required, MultipleInvalid, All, Email
from mgn.utils.oauth import OAuthSignIn
from mgn.delegates.master_user_delegate import MasterUserDelegate
from mgn.delegates.user_notifications_delegate import UserNotificationsDelegate
from mgn.services.constants import HOME_URL, ROOT_DOMAIN, SHORT_TOKEN_VALIDITY, COOKIE_EXPIRATION_DAYS
from werkzeug import check_password_hash

mod = Blueprint('auth', __name__, url_prefix='/auth')


def generate_password():
    return str(uuid.uuid4().hex[0:8])


@mod.route('/confirm-email', methods=['PUT'])
def email_verification():
    data_request = request.get_json()
    schema = Schema({
        Required("email"): Email,
        Required("token"): str
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    email = data_request.get('email')
    token = data_request.get('token')
    if email == confirm_token(token, SHORT_TOKEN_VALIDITY):
        master_user = MasterUserDelegate()
        user = master_user.get_by_email(str(email))
        if user is not None:
            response_data = SUCCESS.copy()
            if user.is_active == ACTIVE:
                response_data[
                    "message"] = "This email address already confirmed! Please <a href='/login'>login</a> to continue."
            else:
                master_user = MasterUserDelegate(user.master_user_id)
                master_user.update_user_is_active(ACTIVE)
                response_data["message"] = "Email address confirmed! Please <a href='/login'>login</a> to continue."
                notification = UserNotificationsDelegate(user.id)
                notification.add('welcome', 'Welcome to MGN! ' + user.first_name, '', str(datetime.datetime.utcnow()))
            response = generic_success_response(response_data)
        else:
            response_data = ERROR.copy()
            response_data["message"] = "Invalid email address."
            response = generic_error_response(response_data)
    else:
        response_data = ERROR.copy()
        response_data["message"] = "Invalid token or token expired! <a href='/email-verification'>Click Here</a> to resend email."
        response = generic_error_response(response_data)
    return response


@mod.route('/send-email-verification', methods=['POST'])
def send_email_verification():
    data_request = request.get_json()
    schema = Schema({
        Required("email"): Email
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    email = data_request.get('email')
    master_user = MasterUserDelegate()
    user = master_user.get_by_email(str(email))
    if user is None:
        response_data = ERROR.copy()
        response_data["message"] = "Invalid email address."
        return generic_error_response(response_data)
    first_name = user.first_name
    email_resp = account_verification(first_name, email, generate_confirmation_token(email))
    if email_resp.status_code == 200:
        response_data = SUCCESS.copy()
        response_data["message"] = "Verification link sent. Please check your email."
        response = generic_success_response(response_data)
    else:
        response_data = ERROR.copy()
        response_data["email_response"] = email_resp.text
        response_data["message"] = "We are unable to verify email at this time."
        response_data["attribute"] = "email_verification"
        response_data["verification_link"] = "/email-verification"
        response = generic_error_response(response_data)
    return response


@mod.route('/send-password-link', methods=['POST'])
def send_password_link():
    data_request = request.get_json()
    schema = Schema({
        Required("email"): Email
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    email = data_request.get('email')
    master_user = MasterUserDelegate()
    user = master_user.get_by_email(str(email))
    if user is None:
        response_data = ERROR.copy()
        response_data["message"] = "Invalid email address."
        return generic_error_response(response_data)
    first_name = user.first_name
    email_resp = change_password_verification(first_name, email, generate_confirmation_token(email))
    if email_resp.status_code == 200:
        response_data = SUCCESS.copy()
        response_data["message"] = "Link sent!! Please check your email."
        response = generic_success_response(response_data)
    else:
        response_data = ERROR.copy()
        response_data["email_response"] = email_resp.text
        response_data["message"] = "Sorry!! We are unable to send email at this time."
        response = generic_error_response(response_data)
    return response


@mod.route('/forgot-password', methods=['PUT'])
def forgot_password(master_user_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("password"): validate_password,
        Required("email"): Email,
        Required("token"): str
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    password = data_request.get('password')
    email = data_request.get('email')
    token = data_request.get('token')
    if email != confirm_token(token, SHORT_TOKEN_VALIDITY):
        response_data = ERROR.copy()
        response_data[
            "message"] = "Invalid token or token expired! Please use <a href='/forgot-password'>forgot password</a> to resend email."
        return generic_error_response(response_data)
    master_user = MasterUserDelegate()
    user = master_user.get_by_email(str(email))
    if user is None:
        response_data = ERROR.copy()
        response_data["message"] = "Invalid email address."
        return generic_error_response(response_data)
    master_user = MasterUserDelegate(user.id)
    if password != '':
        if master_user.update_user_password(password):
            response_data = SUCCESS.copy()
            response_data["message"] = UPDATED
            response = generic_success_response(response_data)
        else:
            response = ERROR_RESPONSE
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/authorize/<string:provider>/user_type/<int:mgn_user_type_id>/auth_type/<int:auth_type_id>')
def oauth_authorize(provider=None, mgn_user_type_id=None, auth_type_id=None):
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize(mgn_user_type_id, auth_type_id)


@mod.route('/callback/<string:provider>/user_type/<int:mgn_user_type_id>/auth_type/<int:auth_type_id>')
def oauth_callback(provider=None, mgn_user_type_id=None, auth_type_id=None):
    oauth = OAuthSignIn.get_provider(provider)
    social_id, email, first_name, last_name, fb_profile_pic = oauth.callback(mgn_user_type_id, auth_type_id)
    if social_id is None:
        response_data = ERROR.copy()
        response_data["message"] = "Authentication Failed."
        response = generic_success_response(response_data)
        return response
    master_user = MasterUserDelegate()
    user = master_user.get_by_email(str(email))
    try:
        profile_pic = fb_profile_pic["data"]["url"]
    except:
        profile_pic = None
    if user is None:
        uuid = master_user.register(first_name, last_name, email, generate_password(), auth_type_id, mgn_user_type_id,
                                    profile_pic, social_id)
        if uuid is not None:
            auth_type = auth_type_id
            token = generate_confirmation_token(email)
            uid = generate_confirmation_token(uuid)
            response = make_response(redirect(url_for('auth.authorize', auth_type=auth_type, token=token, uid=uid)))
        else:
            response_data = ERROR.copy()
            response_data["message"] = "Unable to create account."
            response = generic_error_response(response_data)
    else:
        auth_type = auth_type_id
        token = generate_confirmation_token(user.email)
        uid = generate_confirmation_token(user.master_user_id)
        response = make_response(redirect(url_for('auth.authorize', auth_type=auth_type, token=token, uid=uid)))
    return response


@mod.route('/authorize/<string:auth_type>/<string:token>/<string:uid>', methods=['GET'])
def authorize(auth_type=None, token=None, uid=None):
    expire_date = datetime.datetime.now()
    expire_date = expire_date + datetime.timedelta(days=COOKIE_EXPIRATION_DAYS)

    response = make_response(redirect(HOME_URL))
    response.set_cookie('AID', value=auth_type, domain=ROOT_DOMAIN, expires=expire_date)
    response.set_cookie('UID', value=uid, domain=ROOT_DOMAIN, expires=expire_date)
    response.set_cookie('EID', value=token, domain=ROOT_DOMAIN, expires=expire_date)
    return response


@mod.route('/', methods=['POST'])
def login(auth_type=None, token=None, uid=None):
    data_request = request.get_json()
    schema = Schema({
        Required("email"): Email,
        Required("password"): validate_password
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    email = data_request.get('email')
    password = data_request.get('password')
    master_user = MasterUserDelegate()
    user = master_user.get_by_email(email)
    if user is not None and check_password_hash(user.password, password):
        if user.is_active == TRUE:
            response_data = SUCCESS.copy()
            user_json = user.serialize
            user_json["token"] = generate_confirmation_token(email)
            response_data["data"] = json.dumps(user_json)
            response_data["message"] = "Login Successful"
            response = generic_success_response(response_data)
        elif user.is_deleted == TRUE:
            response_data = ERROR.copy()
            response_data["message"] = "Account is been deleted"
            response = generic_error_response(response_data)
        elif user.is_blocked == TRUE:
            response_data = ERROR.copy()
            response_data["message"] = "Account is been blocked"
            response = generic_error_response(response_data)
        elif user.is_email_confirmed == FALSE:
            response_data = ERROR.copy()
            response_data["message"] = "Please verify your email address. <a href='/email-verification'>Click Here</a> to resend verification link."
            response = generic_error_response(response_data)
        return response
    response_data = ERROR.copy()
    response_data["message"] = "Username or Password is wrong"
    response = generic_error_response(response_data)
    return response
