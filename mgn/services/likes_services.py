from flask import Blueprint, request
from mgn.utils.constants import *
from mgn.utils.general_response import *
from mgn.delegates.likes_delegate import LikesDelegate
from mgn.delegates.like_threads_delegate import LikeThreadsDelegate
from flasgger.utils import swag_from
from mgn.utils.decorators import requires_login
from voluptuous import Schema, Required, MultipleInvalid, Optional
from mgn.utils.validations import *

mod = Blueprint('likes_services', __name__, url_prefix='/likes')


# Like Threads
@mod.route('/thread', methods=['POST'])
def add_thread():
    like_thread = LikeThreadsDelegate()
    if like_thread.add():
        response_data = SUCCESS.copy()
        response_data["message"] = ADDED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/thread/<int:thread_id>', methods=['GET'])
def get_thread(thread_id=None):
    like_thread = LikeThreadsDelegate(thread_id)
    if like_thread.get():
        response_data = SUCCESS.copy()
        response_data["message"] = ADDED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


# Likes
@mod.route('/', methods=['POST'])
def add():
    data_request = request.get_json()
    schema = Schema({
        Required("master_user_id"): validate_user_by_id,
        Required("like_thread_id"): int,
        Optional("post_id"): int,
        Optional("blog_id"): int,
        Optional("share_id"): int
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    master_user_id = data_request.get('master_user_id')
    like_thread_id = data_request.get('like_thread_id')
    try:
        post_id = data_request.get('post_id')
    except:
        post_id = None
    try:
        blog_id = data_request.get('blog_id')
    except:
        blog_id = None
    try:
        share_id = data_request.get('share_id')
    except:
        share_id = None
    if post_id is None and blog_id is None and share_id is None:
        response = INVALID_RESPONSE
        return response
    likes = LikesDelegate()
    if likes.add(master_user_id, like_thread_id, post_id, blog_id, share_id):
        response_data = SUCCESS.copy()
        response_data["message"] = ADDED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:likes_thread_id>/offset/<int:offset>', methods=['GET'])
def get_likes(likes_thread_id=None, offset=None):
    try:
        likes = LikesDelegate()
        data = likes.get_likes(likes_thread_id, offset)
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


@mod.route('/user/<int:master_user_id>/offset/<int:offset>', methods=['GET'])
def get_my_likes(master_user_id=None, offset=None):
    try:
        likes = LikesDelegate()
        data = likes.get_my_likes(master_user_id, offset)
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


@mod.route('/<int:like_id>', methods=['DELETE'])
def delete(like_id=None):
    likes = LikesDelegate(like_id)
    if likes.unlike():
        response_data = SUCCESS.copy()
        response_data["message"] = DELETED
        response = generic_success_response(response_data)
    else:
        response = INVALID_RESPONSE
    return response
