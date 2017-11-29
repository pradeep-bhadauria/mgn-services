from flask import Blueprint, request
from mgn.utils.constants import *
from mgn.utils.general_response import *
from mgn.delegates.posts_delegate import PostsDelegate
from flasgger.utils import swag_from
from mgn.utils.decorators import requires_login
from voluptuous import Schema, Required, MultipleInvalid, All, Optional
from voluptuous.validators import Length
from mgn.utils.validations import *

mod = Blueprint('posts_services', __name__, url_prefix='/posts')


@mod.route('/', methods=['POST'])
def add():
    data_request = request.get_json()
    schema = Schema({
        Required("master_user_id"): validate_user_by_id,
        Required("post_text"): All(str, Length(min=20, max=100)),
        Required("has_attachment"): validate_is_active,
        Optional("attachment_url"): Url
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    master_user_id = data_request.get('master_user_id')
    post_text = data_request.get('post_text')
    has_attachment = data_request.get('has_attachment')
    try:
        attachment_url = data_request.get('attachment_url')
    except:
        attachment_url = None
    if has_attachment == TRUE and attachment_url == None:
        response_data = ERROR.copy()
        response_data["message"] = "Attachment URL missing!"
        response = generic_success_response(response_data)
        return response

    posts = PostsDelegate()
    if posts.add(master_user_id, post_text, has_attachment, attachment_url):
        response_data = SUCCESS.copy()
        response_data["message"] = ADDED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:post_id>/comment-count', methods=['PUT'])
def update_comment_count(post_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("count"): validate_like_comment_share_count
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    count = data_request.get('count')
    posts = PostsDelegate(post_id)
    if posts.update_comment_count(count):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:post_id>/like-count', methods=['PUT'])
def update_like_count(post_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("count"): validate_like_comment_share_count
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    count = data_request.get('count')
    posts = PostsDelegate(post_id)
    if posts.update_like_count(count):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:post_id>/share-count', methods=['PUT'])
def update_share_count(post_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("count"): validate_like_comment_share_count
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    count = data_request.get('count')
    posts = PostsDelegate(post_id)
    if posts.update_share_count(count):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:post_id>', methods=['PUT'])
def update_post_text(post_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("post_text"): All(str, Length(min=1, max=200))
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    post_text = data_request.get('post_text')
    posts = PostsDelegate(post_id)
    if posts.update_post_text(post_text):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:post_id>', methods=['GET'])
def get(post_id=None):
    try:
        posts = PostsDelegate(post_id)
        data = posts.get()
    except:
        response = FAILURE_RESPONSE
        return response
    if data is not None:
        response_data = SUCCESS.copy()
        response_data["data"] = data
        response = generic_success_response(response_data)
    else:
        response_data = ERROR.copy()
        response_data["message"] = INVALID
        response = generic_success_response(response_data)
    return response


@mod.route('/offset/<int:offset>', methods=['GET'])
def get_posts(offset=None):
    try:
        posts = PostsDelegate()
        data = posts.get_posts(offset)
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
def get_my_posts(master_user_id=None, offset=None):
    try:
        posts = PostsDelegate()
        data = posts.get_my_posts(master_user_id, offset)
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


@mod.route('/<int:post_id>', methods=['DELETE'])
def delete(post_id=None):
    posts = PostsDelegate(post_id)
    if posts.delete():
        response_data = SUCCESS.copy()
        response_data["message"] = DELETED
        response = generic_success_response(response_data)
    else:
        response = INVALID_RESPONSE
    return response
