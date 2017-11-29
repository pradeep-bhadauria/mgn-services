from flask import Blueprint, request
from mgn.utils.constants import *
from mgn.utils.general_response import *
from mgn.delegates.shares_delegate import SharesDelegate
from flasgger.utils import swag_from
from mgn.utils.decorators import requires_login
from voluptuous import Schema, Required, MultipleInvalid, All, Optional
from voluptuous.validators import Length
from mgn.utils.validations import *

mod = Blueprint('shares_services', __name__, url_prefix='/shares')


@mod.route('/', methods=['POST'])
def add():
    data_request = request.get_json()
    schema = Schema({
        Required("master_user_id"): validate_user_by_id,
        Optional("post_id"): int,
        Optional("blog_id"): int,
        Optional("url"): Url
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    master_user_id = data_request.get('master_user_id')
    try:
        post_id = data_request.get('post_id')
    except:
        post_id = None
    try:
        blog_id = data_request.get('blog_id')
    except:
        blog_id = None
    try:
        url = data_request.get('url')
    except:
        url = None
    if post_id is None and blog_id is None and url is None:
        response = INVALID_RESPONSE
        return response
    shares = SharesDelegate()
    if shares.add(master_user_id, post_id, blog_id, url):
        response_data = SUCCESS.copy()
        response_data["message"] = ADDED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:share_id>/comment-count', methods=['PUT'])
def update_comment_count(share_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("count"): validate_like_comment_share_count
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    count = data_request.get('count')
    shares = SharesDelegate(share_id)
    if shares.update_comment_count(count):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:share_id>/like-count', methods=['PUT'])
def update_like_count(share_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("count"): validate_like_comment_share_count
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    count = data_request.get('count')
    shares = SharesDelegate(share_id)
    if shares.update_like_count(count):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:share_id>/share-count', methods=['PUT'])
def update_share_count(share_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("count"): validate_like_comment_share_count
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    count = data_request.get('count')
    shares = SharesDelegate(share_id)
    if shares.update_share_count(count):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/offset/<int:offset>', methods=['GET'])
def get_shares(offset=None):
    try:
        shares = SharesDelegate()
        data = shares.get_shares(offset)
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
def get_my_shares(master_user_id=None, offset=None):
    try:
        shares = SharesDelegate()
        data = shares.get_my_shares(master_user_id, offset)
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


@mod.route('/<int:share_id>', methods=['GET'])
def get(share_id=None):
    try:
        shares = SharesDelegate(share_id)
        data = shares.get()
    except:
        response = FAILURE_RESPONSE
        return response
    if data is not None:
        response_data = SUCCESS.copy()
        if data != EMPTY_LIST:
            response_data["data"] = data
        else:
            response_data["message"] = INVALID_ID
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:share_id>', methods=['DELETE'])
def delete(share_id=None):
    shares = SharesDelegate(share_id)
    if shares.delete():
        response_data = SUCCESS.copy()
        response_data["message"] = DELETED
        response = generic_success_response(response_data)
    else:
        response = INVALID_RESPONSE
    return response
