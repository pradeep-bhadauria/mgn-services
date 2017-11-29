from flask import Blueprint, request
from mgn.utils.token import generate_confirmation_token, confirm_token
from mgn.utils.constants import *
from mgn.utils.general_response import *
from mgn.utils.emails import account_verification
from mgn.utils.validations import *
from mgn.delegates.master_user_delegate import MasterUserDelegate
from voluptuous import Schema, Required, MultipleInvalid, All, Range, Optional, Url
from flasgger.utils import swag_from
from mgn.utils.decorators import requires_login

mod = Blueprint('master_user_services', __name__, url_prefix='/master-user')


@mod.route('/', methods=['POST'])
@swag_from("docs/master_user_services/add_master_user.yml")
def add_master_user():
    data_request = request.get_json()
    schema = Schema({
        Required("first_name"): validate_name,
        Required("last_name"): validate_name,
        Required("email"): validate_email,
        Required("password"): validate_password,
        Required("auth_type"): validate_auth_type,
        Required("mgn_user_type"): validate_user_type,
        Optional("profile_pic"): Url
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    first_name = data_request.get('first_name')
    last_name = data_request.get('last_name')
    email = data_request.get('email')
    password = data_request.get('password')
    auth_type_id = data_request.get('auth_type')
    mgn_user_type_id = data_request.get('mgn_user_type')
    try:
        profile_pic = data_request.get('profile_pic')
    except:
        profile_pic = None
    master_user = MasterUserDelegate()
    social_id = None
    user = master_user.get_by_email(email)
    if user is not None:
        response_data = ERROR.copy()
        response_data["message"] = "This email is already in use! Please try Forgot Password"
        response = generic_error_response(response_data)
        return response
    uuid = master_user.register(first_name, last_name, email, password, auth_type_id, mgn_user_type_id, profile_pic,
                                social_id)
    if uuid is not None:
        if auth_type_id == EMAIL:
            email_resp = account_verification(first_name, email, generate_confirmation_token(email))
            if email_resp.status_code == 200:
                response_data = SUCCESS.copy()
                response_data["auth_type"] = auth_type_id
                response_data["message"] = "Account is been created. Please check your email for verification."
                response = generic_success_response(response_data)
            else:
                response_data = ERROR.copy()
                response_data["email_response"] = email_resp.text
                response_data["message"] = "We are unable to verify email at this time."
                response_data["attribute"] = "email_verification"
                response_data["verification_link"] = "/email-verification"
                response = generic_error_response(response_data)
        else:
            response = INVALID_RESPONSE
    else:
        response = FAILURE_RESPONSE
    return response


@mod.route('/<int:master_user_id>/name', methods=['PUT'])
@swag_from("docs/master_user_services/update_master_user_name.yml")
def update_master_user_name(master_user_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("first_name"): validate_name,
        Required("last_name"): validate_name
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    first_name = data_request.get('first_name')
    last_name = data_request.get('last_name')
    master_user = MasterUserDelegate(master_user_id)
    if first_name != '' and last_name != '':
        if master_user.update_user_name(first_name, last_name):
            response_data = SUCCESS.copy()
            response_data["message"] = UPDATED
            response = generic_success_response(response_data)
        else:
            response = ERROR_RESPONSE
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:master_user_id>/email', methods=['PUT'])
@swag_from("docs/master_user_services/update_master_user_email.yml")
def update_master_user_email(master_user_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("email"): validate_email
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    email = data_request.get('email')
    master_user = MasterUserDelegate(master_user_id)
    if email != '':
        if master_user.update_user_email(email):
            response_data = SUCCESS.copy()
            response_data["message"] = UPDATED
            response = generic_success_response(response_data)
        else:
            response = ERROR_RESPONSE
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:master_user_id>/username', methods=['PUT'])
@swag_from("docs/master_user_services/update_master_user_username.yml")
def update_master_user_username(master_user_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("username"): validate_username
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    username = data_request.get('username')
    master_user = MasterUserDelegate(master_user_id)
    if username != '':
        if master_user.update_user_username(username):
            response_data = SUCCESS.copy()
            response_data["message"] = UPDATED
            response = generic_success_response(response_data)
        else:
            response = ERROR_RESPONSE
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:master_user_id>/password', methods=['PUT'])
@swag_from("docs/master_user_services/update_master_user_password.yml")
def update_master_user_password(master_user_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("password"): validate_password
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    password = data_request.get('password')
    master_user = MasterUserDelegate(master_user_id)
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


@mod.route('/<int:master_user_id>/is-active', methods=['PUT'])
@swag_from("docs/master_user_services/update_master_user_is_active.yml")
def update_master_user_is_active(master_user_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("is_active"): All(int, Range(min=0, max=1))
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    is_active = data_request.get('is_active')
    master_user = MasterUserDelegate(master_user_id)
    if is_active != '':
        if master_user.update_user_is_active(is_active):
            response_data = SUCCESS.copy()
            response_data["message"] = UPDATED
            response = generic_success_response(response_data)
        else:
            response = ERROR_RESPONSE
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:master_user_id>/is-deleted', methods=['PUT'])
@swag_from("docs/master_user_services/update_master_user_is_deleted.yml")
def update_master_user_is_deleted(master_user_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("is_deleted"): All(int, Range(min=0, max=1))
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    is_deleted = data_request.get('is_deleted')
    master_user = MasterUserDelegate(master_user_id)
    if is_deleted != '':
        if master_user.update_user_is_active(is_deleted):
            response_data = SUCCESS.copy()
            response_data["message"] = UPDATED
            response = generic_success_response(response_data)
        else:
            response = ERROR_RESPONSE
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:master_user_id>/is-blocked', methods=['PUT'])
@swag_from("docs/master_user_services/update_master_user_is_blocked.yml")
def update_master_user_is_blocked(master_user_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("is_blocked"): All(int, Range(min=0, max=1))
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    is_blocked = data_request.get('is_blocked')
    master_user = MasterUserDelegate(master_user_id)
    if is_blocked != '':
        if master_user.update_user_is_active(is_blocked):
            response_data = SUCCESS.copy()
            response_data["message"] = UPDATED
            response = generic_success_response(response_data)
        else:
            response = ERROR_RESPONSE
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:master_user_id>/profile-pic', methods=['PUT'])
@swag_from("docs/master_user_services/update_master_user_profile_pic.yml")
def update_master_user_profile_pic(master_user_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("profile_pic"): Url
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    profile_pic = data_request.get('profile_pic')
    master_user = MasterUserDelegate(master_user_id)
    if master_user.update_profile_pic(profile_pic):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:master_user_id>', methods=['GET'])
@swag_from("docs/master_user_services/get_master_user.yml")
def get_master_user(master_user_id=None):
    try:
        master_user = MasterUserDelegate(master_user_id)
        data = master_user.get()
    except:
        response = FAILURE_RESPONSE
        return response
    if data is not None:
        response_data = SUCCESS.copy()
        response_data["data"] = data
        response = generic_success_response(response_data)
    else:
        response_data = ERROR.copy()
        response_data["message"] = INVALID_ID
        response = generic_success_response(response_data)
    return response


@mod.route('/', methods=['GET'])
@swag_from("docs/master_user_services/get_all_master_user.yml")
def get_all_master_user():
    try:
        master_user = MasterUserDelegate()
        data = master_user.get_all()
    except:
        response = FAILURE_RESPONSE
        return response
    if data is not None:
        response_data = SUCCESS.copy()
        if data != EMPTY_LIST:
            response_data["data"] = data
        else:
            response_data["message"] = NO_DATA
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/active', methods=['GET'])
@swag_from("docs/master_user_services/get_active_master_user.yml")
def get_active_master_user():
    try:
        master_user = MasterUserDelegate()
        data = master_user.get_active()
    except:
        response = FAILURE_RESPONSE
        return response
    if data is not None:
        response_data = SUCCESS.copy()
        if data != EMPTY_LIST:
            response_data["data"] = data
        else:
            response_data["message"] = NO_DATA
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/inactive', methods=['GET'])
@swag_from("docs/master_user_services/get_inactive_master_user.yml")
def get_inactive_master_user():
    try:
        master_user = MasterUserDelegate()
        data = master_user.get_inactive()
    except:
        response = FAILURE_RESPONSE
        return response
    if data is not None:
        response_data = SUCCESS.copy()
        if data != EMPTY_LIST:
            response_data["data"] = data
        else:
            response_data["message"] = NO_DATA
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/search/<q>', methods=['GET'])
@swag_from("docs/master_user_services/search_master_user.yml")
def search_master_user(q=None):
    try:
        master_user = MasterUserDelegate()
        data = master_user.search(q)
    except:
        response = FAILURE_RESPONSE
        return response
    if data is not None:
        response_data = SUCCESS.copy()
        if data != EMPTY_LIST:
            response_data["data"] = data
        else:
            response_data["message"] = NO_DATA
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response
