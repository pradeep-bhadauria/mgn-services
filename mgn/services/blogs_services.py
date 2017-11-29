from flask import Blueprint, request
from mgn.utils.constants import *
from mgn.utils.general_response import *
from mgn.delegates.blogs_delegate import BlogsDelegate
from flasgger.utils import swag_from
from mgn.utils.decorators import requires_login
from voluptuous import Schema, Required, MultipleInvalid, All
from voluptuous.validators import Length
from mgn.utils.validations import *

mod = Blueprint('blogs_services', __name__, url_prefix='/blogs')


@mod.route('/', methods=['POST'])
def add():
    data_request = request.get_json()
    schema = Schema({
        Required("master_user_id"): validate_user_by_id,
        Required("blog_subject"): All(str, Length(min=20, max=100)),
        Required("blog_body"): All(str),
        Required("tags"): list
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    master_user_id = data_request.get('master_user_id')
    blog_subject = data_request.get('blog_subject')
    blog_body = data_request.get('blog_body')
    tags = data_request.get('tags')
    blogs = BlogsDelegate()
    if blogs.add(master_user_id, blog_subject, blog_body, tags):
        response_data = SUCCESS.copy()
        response_data["message"] = ADDED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:blog_id>/comment-count', methods=['PUT'])
def update_comment_count(blog_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("count"): validate_like_comment_share_count
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    count = data_request.get('count')
    blogs = BlogsDelegate(blog_id)
    if blogs.update_comment_count(count):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:blog_id>/like-count', methods=['PUT'])
def update_like_count(blog_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("count"): validate_like_comment_share_count
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    count = data_request.get('count')
    blogs = BlogsDelegate(blog_id)
    if blogs.update_like_count(count):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:blog_id>/visit-count', methods=['PUT'])
def update_visit_count(blog_id=None):
    blogs = BlogsDelegate(blog_id)
    if blogs.update_visit_count():
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:blog_id>/share-count', methods=['PUT'])
def update_share_count(blog_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("count"): validate_like_comment_share_count
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    count = data_request.get('count')
    blogs = BlogsDelegate(blog_id)
    if blogs.update_share_count(count):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:blog_id>/blog-name', methods=['PUT'])
def update_blog_name(blog_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("blog_name"): All(str, Length(min=20, max=100))
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    blog_name = data_request.get('blog_name')
    blogs = BlogsDelegate(blog_id)
    if blogs.update_blog_name(blog_name):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:blog_id>/blog-subject', methods=['PUT'])
def update_blog_subject(blog_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("blog_subject"): All(str, Length(min=20, max=100))
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    blog_subject = data_request.get('blog_subject')
    blogs = BlogsDelegate(blog_id)
    if blogs.update_blog_subject(blog_subject):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:blog_id>/blog-body', methods=['PUT'])
def update_blog_body(blog_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("blog_body"): str
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    blog_body = data_request.get('blog_body')
    blogs = BlogsDelegate(blog_id)
    if blogs.update_blog_body(blog_body):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:blog_id>/blog-tags', methods=['PUT'])
def update_blog_tags(blog_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("blog_tags"): list
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    blog_tags = data_request.get('blog_tags')
    blogs = BlogsDelegate(blog_id)
    if blogs.update_blog_tags(blog_tags):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<string:blog_name>', methods=['GET'])
def get(blog_name=None):
    try:
        blogs = BlogsDelegate()
        data = blogs.get(blog_name)
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
def get_blogs(offset=None):
    try:
        blogs = BlogsDelegate()
        data = blogs.get_blogs(offset)
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
def get_my_blogs(master_user_id=None, offset=None):
    try:
        blogs = BlogsDelegate()
        data = blogs.get_my_blogs(master_user_id, offset)
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


@mod.route('/<int:blog_id>', methods=['DELETE'])
def delete(blog_id=None):
    blogs = BlogsDelegate(blog_id)
    if blogs.delete():
        response_data = SUCCESS.copy()
        response_data["message"] = DELETED
        response = generic_success_response(response_data)
    else:
        response = INVALID_RESPONSE
    return response
