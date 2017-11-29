from flask import Blueprint, request
from mgn.utils.constants import *
from mgn.utils.general_response import *
from mgn.delegates.mgn_auth_type_delegate import MgnAuthTypeDelegate
from flasgger.utils import swag_from
from mgn.utils.decorators import requires_login
from voluptuous import Schema, Required, MultipleInvalid, Length, All
from mgn.utils.validations import *

mod = Blueprint('mgn_auth_type_services', __name__, url_prefix='/auth-type')


@mod.route('/', methods=['POST'])
@swag_from("docs/mgn_auth_type/add_auth_type.yml")
def add_auth_type():
    data_request = request.get_json()
    schema = Schema({
        Required("auth_name"): All(string_code, Length(min=3, max=45)),
        Required("auth_desc"): All(str, Length(min=3, max=100))
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    auth_name = data_request.get('auth_name')
    auth_desc = data_request.get('auth_desc')
    mgn_auth_type = MgnAuthTypeDelegate()
    if mgn_auth_type.add(auth_name, auth_desc):
        response_data = SUCCESS.copy()
        response_data["message"] = ADDED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:auth_type_id>', methods=['GET'])
@swag_from("docs/mgn_auth_type/get_auth_type.yml")
def get_auth_type(auth_type_id=None):
    try:
        auth_name = MgnAuthTypeDelegate(auth_type_id)
        data = auth_name.get()
    except:
        response = FAILURE_RESPONSE
        return response
    if data is not None:
        response_data = SUCCESS.copy()
        response_data["data"] = data
        response = generic_success_response(response_data)
    else:
        response_data = ERROR.copy()
        response_data["message"] = "Invalid Auth Type"
        response = generic_error_response(response_data)
    return response


@mod.route('/', methods=['GET'])
@swag_from("docs/mgn_auth_type/get_all_auth_type.yml")
def get_all_auth_types():
    try:
        auth_types = MgnAuthTypeDelegate()
        data = auth_types.get_all()
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


@mod.route('/<int:auth_type_id>', methods=['PUT'])
@swag_from("docs/mgn_auth_type/update_auth_type.yml")
def update_auth_type(auth_type_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("auth_name"): All(string_code, Length(min=3, max=45)),
        Required("auth_desc"): All(str, Length(min=3, max=100))
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    auth_name = data_request.get('auth_name')
    auth_desc = data_request.get('auth_desc')
    mgn_auth_type = MgnAuthTypeDelegate(auth_type_id)
    if mgn_auth_type.update(auth_name, auth_desc):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response
