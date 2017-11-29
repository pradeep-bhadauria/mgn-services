from flask import Blueprint, request
from mgn.utils.constants import *
from mgn.utils.general_response import *
from mgn.delegates.timeline_activity_type_delegate import TimelineActivityTypeDelegate
from flasgger.utils import swag_from
from mgn.utils.decorators import requires_login
from voluptuous import Schema, Required, MultipleInvalid, Length, All
from mgn.utils.validations import *

mod = Blueprint('timeline_activity_type_services', __name__, url_prefix='/timeline-activity-type')


@mod.route('/', methods=['POST'])
def add():
    data_request = request.get_json()
    schema = Schema({
        Required("name"): All(string_val, Length(min=3, max=10)),
        Required("description"): All(str, Length(min=3, max=100))
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    name = data_request.get('name')
    description = data_request.get('description')
    timeline_activity_type = TimelineActivityTypeDelegate()
    tat = timeline_activity_type.get_by_name(name)
    if tat is not None:
        response_data = SUCCESS.copy()
        response_data["message"] = "Activity type name already exists"
        response = generic_success_response(response_data)
        return response
    if timeline_activity_type.add(name, description):
        response_data = SUCCESS.copy()
        response_data["message"] = ADDED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:timeline_activity_type_id>', methods=['PUT'])
def update(timeline_activity_type_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("name"): All(string_val, Length(min=3, max=10)),
        Required("description"): All(str, Length(min=3, max=100))
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        multiple_invalid_response(e)
    name = data_request.get('name')
    description = data_request.get('description')
    timeline_activity_type = TimelineActivityTypeDelegate(timeline_activity_type_id)
    tat = timeline_activity_type.get_by_name(name)
    if tat is not None:
        if tat.timeline_activity_type_id != timeline_activity_type_id:
            response_data = SUCCESS.copy()
            response_data["message"] = "Activity type name already exists"
            response = generic_success_response(response_data)
            return response
    if timeline_activity_type.update(name, description):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:timeline_activity_type_id>', methods=['DELETE'])
def delete(timeline_activity_type_id=None):
    timeline_activity_type = TimelineActivityTypeDelegate(timeline_activity_type_id)
    if timeline_activity_type.delete():
        response_data = SUCCESS.copy()
        response_data["message"] = DELETED
        response = generic_success_response(response_data)
    else:
        response = INVALID_RESPONSE
    return response


@mod.route('/<int:timeline_activity_type_id>', methods=['GET'])
def get(timeline_activity_type_id=None):
    try:
        timeline_activity_type = TimelineActivityTypeDelegate(timeline_activity_type_id)
        data = timeline_activity_type.get()
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
def get_all():
    try:
        timeline_activity_type = TimelineActivityTypeDelegate()
        data = timeline_activity_type.get_all()
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
