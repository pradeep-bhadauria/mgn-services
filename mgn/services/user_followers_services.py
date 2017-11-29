from flask import Blueprint, request
from mgn.utils.constants import *
from mgn.utils.general_response import *
from mgn.delegates.user_followers_delegate import UserFollowersDelegate
from flasgger.utils import swag_from
from mgn.utils.decorators import requires_login
from voluptuous import Schema, Required, MultipleInvalid
from mgn.utils.validations import *

mod = Blueprint('user_followers_services', __name__, url_prefix='/<int:follower_id>/following')


@mod.route('/<int:following_id>', methods=['POST'])
def add(follower_id=None, following_id=None):
    user_followers = UserFollowersDelegate(follower_id, following_id)
    if user_followers.add():
        response_data = SUCCESS.copy()
        response_data["message"] = ADDED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:following_id>/block', methods=['PUT'])
def update_is_blocked(follower_id=None, following_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("is_blocked"): validate_is_active
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    is_blocked = data_request.get('is_blocked')
    user_followers = UserFollowersDelegate(follower_id, following_id)
    if user_followers.update_is_blocked(is_blocked):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:following_id>/unfollow', methods=['DELETE'])
def delete(follower_id=None, following_id=None):
    user_followers = UserFollowersDelegate(follower_id, following_id)
    if user_followers.unfollow():
        response_data = SUCCESS.copy()
        response_data["message"] = DELETED
        response = generic_success_response(response_data)
    else:
        response = INVALID_RESPONSE
    return response


@mod.route('/<int:following_id>', methods=['GET'])
def get(follower_id=None, following_id=None):
    try:
        user_followers = UserFollowersDelegate(follower_id, following_id)
        data = user_followers.get()
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
def get_all(follower_id=None):
    try:
        user_followers = UserFollowersDelegate(follower_id)
        data = user_followers.get_all()
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
