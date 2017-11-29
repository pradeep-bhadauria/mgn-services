from flask import Blueprint, request
from mgn.utils.constants import *
from mgn.utils.general_response import *
from mgn.delegates.user_connections_delegate import UserConnectionsDelegate
from flasgger.utils import swag_from
from mgn.utils.decorators import requires_login
from voluptuous import Schema, Required, MultipleInvalid
from mgn.utils.validations import *

mod = Blueprint('user_connections_services', __name__, url_prefix='/<int:connected_from_id>/connection')


@mod.route('/<int:connected_to_id>', methods=['POST'])
def add(connected_from_id=None, connected_to_id=None):
    user_connections = UserConnectionsDelegate(connected_from_id, connected_to_id)
    if user_connections.add():
        response_data = SUCCESS.copy()
        response_data["message"] = ADDED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:connected_to_id>/accept', methods=['PUT'])
def update_is_accepted(connected_from_id=None, connected_to_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("is_accepted"): validate_is_active
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    is_accepted = data_request.get('is_accepted')
    user_connections = UserConnectionsDelegate(connected_from_id, connected_to_id)
    if user_connections.update_is_accepted(is_accepted):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:connected_to_id>/block', methods=['PUT'])
def update_is_blocked(connected_from_id=None, connected_to_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("is_blocked"): validate_is_active
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    is_blocked = data_request.get('is_blocked')
    user_connections = UserConnectionsDelegate(connected_from_id, connected_to_id)
    if user_connections.update_is_blocked(is_blocked):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:connected_to_id>/ignore', methods=['PUT'])
def update_is_ignored(connected_from_id=None, connected_to_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("is_ignored"): validate_is_active
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    is_ignored = data_request.get('is_ignored')
    user_connections = UserConnectionsDelegate(connected_from_id, connected_to_id)
    if user_connections.update_is_ignored(is_ignored):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:connected_to_id>/message-thread', methods=['PUT'])
def update_message_thread(connected_from_id=None, connected_to_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("message_thread_id"): int
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    message_thread_id = data_request.get('message_thread_id')
    if message_thread_id == 0:
        message_thread_id = None
    user_connections = UserConnectionsDelegate(connected_from_id, connected_to_id)
    if user_connections.update_message_thread(message_thread_id):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:connected_to_id>/delete', methods=['DELETE'])
def delete(connected_from_id=None, connected_to_id=None):
    user_connections = UserConnectionsDelegate(connected_from_id, connected_to_id)
    if user_connections.delete():
        response_data = SUCCESS.copy()
        response_data["message"] = DELETED
        response = generic_success_response(response_data)
    else:
        response = INVALID_RESPONSE
    return response


@mod.route('/<int:connected_to_id>', methods=['GET'])
def get(connected_from_id=None, connected_to_id=None):
    try:
        user_connections = UserConnectionsDelegate(connected_from_id, connected_to_id)
        data = user_connections.get()
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
def get_all(connected_from_id=None):
    try:
        user_connections = UserConnectionsDelegate(connected_from_id)
        data = user_connections.get_all()
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
