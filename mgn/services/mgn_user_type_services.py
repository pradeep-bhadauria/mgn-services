from flask import Blueprint, request
from mgn.utils.constants import *
from mgn.utils.general_response import *
from mgn.delegates.mgn_user_type_delegate import MgnUserTypeDelegate
from flasgger.utils import swag_from
from mgn.utils.decorators import requires_login
from voluptuous import Schema, Required, MultipleInvalid, Length, All
from mgn.utils.validations import *

mod = Blueprint('mgn_user_type_services', __name__, url_prefix='/user-type')


@mod.route('/', methods=['POST'])
@swag_from("docs/mgn_user_type/add_user_type.yml")
def add_user_type():
    data_request = request.get_json()
    schema = Schema({
        Required("user_type"): All(string_code, Length(min=3, max=10)),
        Required("user_desc"): All(str, Length(min=3, max=30))
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    user_type = data_request.get('user_type')
    user_desc = data_request.get('user_desc')
    mgn_user_type = MgnUserTypeDelegate()
    if user_type != "" and user_desc != "":
        if mgn_user_type.add(user_type, user_desc):
            response_data = SUCCESS.copy()
            response_data["message"] = ADDED
            response = generic_success_response(response_data)
        else:
            response = ERROR_RESPONSE
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:user_type_id>', methods=['GET'])
@swag_from("docs/mgn_user_type/get_user_type.yml")
def get_user_type(user_type_id=None):
    try:
        user_type = MgnUserTypeDelegate(user_type_id)
        data = user_type.get()
    except:
        response = FAILURE_RESPONSE
        return response
    if data is not None:
        response_data = SUCCESS.copy()
        response_data["data"] = data
        response = generic_success_response(response_data)
    else:
        response_data = ERROR.copy()
        response_data["message"] = "Invalid id"
        response = generic_error_response(response_data)
    return response


@mod.route('/', methods=['GET'])
@swag_from("docs/mgn_user_type/get_all_user_type.yml")
def get_all_user_types():
    try:
        user_types = MgnUserTypeDelegate()
        data = user_types.get_all()
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


@mod.route('/<int:user_type_id>', methods=['PUT'])
@swag_from("docs/mgn_user_type/update_user_type.yml")
def update_user_type(user_type_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("user_type"): All(string_code, Length(min=3, max=10)),
        Required("user_desc"): All(str, Length(min=3, max=30))
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    user_type = data_request.get('user_type')
    user_desc = data_request.get('user_desc')
    mgn_user_type = MgnUserTypeDelegate(user_type_id)
    if user_type != "" and user_desc != "":
        if mgn_user_type.update(user_type, user_desc):
            response_data = SUCCESS.copy()
            response_data["message"] = UPDATED
            response = generic_success_response(response_data)
        else:
            response = ERROR_RESPONSE
    else:
        response = ERROR_RESPONSE
    return response
