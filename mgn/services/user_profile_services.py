from flask import Blueprint, request
from mgn.utils.constants import *
from mgn.utils.general_response import *
from mgn.utils.validations import *
from mgn.delegates.user_profile_delegate import UserProfileDelegate
from voluptuous import Schema, Required, MultipleInvalid, Optional, All, Url

mod = Blueprint('user_profile_services', __name__, url_prefix='/user-profile')


@mod.route('/', methods=['POST'])
def add_user_profile():
    data_request = request.get_json()
    schema = Schema({
        Optional("profile_banner_image"): Url,
        Required("dob"): validate_date,
        Required("gender"): validate_gender,
        Required("user"): validate_user_by_id
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    dob = data_request.get('dob')
    gender = data_request.get('gender')
    user = data_request.get('user')
    try:
        profile_banner_image = data_request.get('profile_banner_image')
    except:
        profile_banner_image = None
    user_profile = UserProfileDelegate()
    if user_profile.add(profile_banner_image, dob, gender, user):
        response = generic_success_response(SUCCESS)
    else:
        response = FAILURE_RESPONSE
    return response


@mod.route('/<int:master_user_id>/profile-banner', methods=['PUT'])
def update_user_profile_banner(master_user_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("profile_banner_image"): Url
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    profile_banner_image = data_request.get('profile_banner_image')
    user_profile = UserProfileDelegate(master_user_id)
    if user_profile.update_profile_banner_image(profile_banner_image):
        response = generic_success_response(SUCCESS)
    else:
        response = FAILURE_RESPONSE
    return response


@mod.route('/<int:master_user_id>/gender', methods=['PUT'])
def update_gender(master_user_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("gender"): validate_gender
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    gender = data_request.get('gender')
    user_profile = UserProfileDelegate(master_user_id)
    if user_profile.update_gender(gender):
        response = generic_success_response(SUCCESS)
    else:
        response = FAILURE_RESPONSE
    return response


@mod.route('/<int:master_user_id>/dob', methods=['PUT'])
def update_dob(master_user_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("dob"): validate_date
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    dob = data_request.get('dob')
    user_profile = UserProfileDelegate(master_user_id)
    if user_profile.update_dob(dob):
        response = generic_success_response(SUCCESS)
    else:
        response = FAILURE_RESPONSE
    return response


@mod.route('/<int:master_user_id>', methods=['GET'])
def get_user_profile(master_user_id=None):
    user_profile = UserProfileDelegate(master_user_id)
    data = user_profile.get()
    if data is not None:
        response_data = SUCCESS.copy()
        response_data["data"] = data
        response = generic_success_response(response_data)
    else:
        response_data = ERROR.copy()
        response_data["message"] = INVALID_ID
        response = generic_error_response(response_data)
    return response
