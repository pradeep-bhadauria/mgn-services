from flask import Blueprint, request
from mgn.utils.constants import *
from mgn.utils.general_response import *
from mgn.delegates.comments_delegate import CommentsDelegate
from mgn.delegates.comment_threads_delegate import CommentThreadsDelegate
from flasgger.utils import swag_from
from mgn.utils.decorators import requires_login
from voluptuous import Schema, Required, MultipleInvalid, Optional, All
from voluptuous.validators import Length
from mgn.utils.validations import *

mod = Blueprint('comments_services', __name__, url_prefix='/comments')


# Comment Threads
@mod.route('/thread', methods=['POST'])
def add_thread():
    comment_thread = CommentThreadsDelegate()
    if comment_thread.add():
        response_data = SUCCESS.copy()
        response_data["message"] = ADDED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/thread/<int:thread_id>', methods=['GET'])
def get_thread(thread_id=None):
    comment_thread = CommentThreadsDelegate(thread_id)
    if comment_thread.get():
        response_data = SUCCESS.copy()
        response_data["message"] = ADDED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


# Comments
@mod.route('/', methods=['POST'])
def add():
    data_request = request.get_json()
    schema = Schema({
        Required("master_user_id"): validate_user_by_id,
        Required("comment_thread_id"): int,
        Optional("comment_reply_thread_id"): int,
        Required("comment"): All(str, Length(min=1, max=200))
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    master_user_id = data_request.get('master_user_id')
    comment_thread_id = data_request.get('comment_thread_id')
    comment = data_request.get('comment')
    try:
        comment_reply_thread_id = data_request.get('comment_reply_thread_id')
    except:
        comment_reply_thread_id = None
    comments = CommentsDelegate()
    if comments.add(master_user_id, comment_thread_id, comment_reply_thread_id, comment):
        response_data = SUCCESS.copy()
        response_data["message"] = ADDED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:comment_id>', methods=['PUT'])
def update_comment(comment_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("comment"): All(str, Length(min=1, max=200))
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    comment = data_request.get('comment')
    comments = CommentsDelegate(comment_id)
    if comments.update(comment):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:comments_thread_id>/offset/<int:offset>', methods=['GET'])
def get_comments(comments_thread_id=None, offset=None):
    try:
        comments = CommentsDelegate()
        data = comments.get_comments(comments_thread_id, offset)
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
def get_my_comments(master_user_id=None, offset=None):
    try:
        comments = CommentsDelegate()
        data = comments.get_my_comments(master_user_id, offset)
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


@mod.route('/<int:comment_id>', methods=['GET'])
def get(comment_id=None):
    try:
        comments = CommentsDelegate(comment_id)
        data = comments.get()
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


@mod.route('/<int:comment_id>', methods=['DELETE'])
def delete(comment_id=None):
    comments = CommentsDelegate(comment_id)
    if comments.delete():
        response_data = SUCCESS.copy()
        response_data["message"] = DELETED
        response = generic_success_response(response_data)
    else:
        response = INVALID_RESPONSE
    return response
