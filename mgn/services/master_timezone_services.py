from flask import Blueprint, request
from mgn.utils.constants import *
from mgn.utils.general_response import *
from mgn.delegates.master_timezone_delegate import MasterTimezoneDelegate
from flasgger.utils import swag_from
from mgn.utils.decorators import requires_login
from voluptuous import Schema, Required, MultipleInvalid, Length, All
from mgn.utils.validations import *

mod = Blueprint('master_timezone_services', __name__, url_prefix='/master-timezone')


@mod.route('/', methods=['POST'])
@swag_from("docs/master_timezone_services/add_master_timezone.yml")
def add_master_timezone():
    data_request = request.get_json()
    schema = Schema({
        Required("timezone_code"): All(string_code, Length(min=3, max=10)),
        Required("timezone_description"): All(str, Length(min=3, max=50)),
        Required("timezone_offset"): All(str, Length(min=3, max=10)),
        Required("timezone_offset_dst"): All(str, Length(min=3, max=10)),
        Required("is_active"): All(int, validate_is_active)
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    code = data_request.get('timezone_code')
    desc = data_request.get('timezone_description')
    offset = data_request.get('timezone_offset')
    offset_dst = data_request.get('timezone_offset_dst')
    is_active = data_request.get('is_active')
    master_timezone = MasterTimezoneDelegate()
    if code != '' and offset != '' and offset_dst != '' and desc != '' and is_active is not None:
        if master_timezone.add(code, desc, offset, offset_dst, is_active):
            response_data = SUCCESS.copy()
            response_data["message"] = ADDED
            response = generic_success_response(response_data)
        else:
            response = ERROR_RESPONSE
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:timezone_id>', methods=['PUT'])
@swag_from("docs/master_timezone_services/update_master_timezone_details.yml")
def update_master_timezone_details(timezone_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("timezone_code"): All(string_code, Length(min=3, max=10)),
        Required("timezone_description"): All(str, Length(min=3, max=50)),
        Required("timezone_offset"): All(str, Length(min=3, max=10)),
        Required("timezone_offset_dst"): All(str, Length(min=3, max=10))
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    code = data_request.get('timezone_code')
    offset = data_request.get('timezone_offset')
    offset_dst = data_request.get('timezone_offset_dst')
    desc = data_request.get('timezone_description')
    master_timezone = MasterTimezoneDelegate(timezone_id)
    if code != '' and offset != '' and offset_dst != '' and desc != '':
        if master_timezone.update_timezone_details(code, desc, offset, offset_dst):
            response_data = SUCCESS.copy()
            response_data["message"] = UPDATED
            response = generic_success_response(response_data)
        else:
            response = ERROR_RESPONSE
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:timezone_id>/is-active', methods=['PUT'])
@swag_from("docs/master_timezone_services/update_master_timezone_active.yml")
def update_master_timezone_active(timezone_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("is_active"): All(int, validate_is_active)
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    is_active = data_request.get('is_active')
    master_timezone = MasterTimezoneDelegate(timezone_id)
    if is_active != '':
        if master_timezone.update_timezone_is_active(is_active):
            response_data = SUCCESS.copy()
            response_data["message"] = UPDATED
            response = generic_success_response(response_data)
        else:
            response = ERROR_RESPONSE
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:timezone_id>', methods=['GET'])
@swag_from("docs/master_timezone_services/get_master_timezone.yml")
def get_master_timezone(timezone_id=None):
    try:
        master_timezone = MasterTimezoneDelegate(timezone_id)
        data = master_timezone.get()
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
@swag_from("docs/master_timezone_services/get_all_master_timezone.yml")
def get_all_master_timezone():
    try:
        master_timezone = MasterTimezoneDelegate()
        data = master_timezone.get_all()
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
@swag_from("docs/master_timezone_services/get_active_master_timezone.yml")
def get_active_master_timezone():
    try:
        master_timezone = MasterTimezoneDelegate()
        data = master_timezone.get_active()
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
@swag_from("docs/master_timezone_services/get_inactive_master_timezone.yml")
def get_inactive_master_timezone():
    try:
        master_timezone = MasterTimezoneDelegate()
        data = master_timezone.get_inactive()
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
@swag_from("docs/master_timezone_services/search_master_timezone.yml")
def search_master_timezone(q=None):
    try:
        master_timezone = MasterTimezoneDelegate()
        data = master_timezone.search(q)
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
