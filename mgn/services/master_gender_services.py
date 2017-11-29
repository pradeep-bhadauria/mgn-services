from flask import Blueprint, request
from mgn.utils.constants import *
from mgn.utils.general_response import *
from mgn.delegates.master_gender_delegate import MasterGenderDelegate
from flasgger.utils import swag_from
from mgn.utils.decorators import requires_login
from voluptuous import Schema, Required, MultipleInvalid, Length, All
from mgn.utils.validations import *

mod = Blueprint('master_gender_services', __name__, url_prefix='/master-gender')


@mod.route('/', methods=['POST'])
@requires_login
@swag_from("docs/master_gender_services/add_master_gender.yml")
def add_master_gender():
    data_request = request.get_json()
    schema = Schema({
        Required("gender"): All(string_val, Length(min=3, max=10))
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    gender = data_request.get('gender')
    master_gender = MasterGenderDelegate()
    if gender != "":
        if master_gender.add(gender):
            response_data = SUCCESS.copy()
            response_data["message"] = ADDED
            response = generic_success_response(response_data)
        else:
            response = ERROR_RESPONSE
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:master_gender_id>', methods=['PUT'])
@requires_login
@swag_from("docs/master_gender_services/update_master_gender.yml")
def update_master_gender(master_gender_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("gender"): All(string_val, Length(min=3, max=10))
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        multiple_invalid_response(e)
    gender = data_request.get('gender')
    master_gender = MasterGenderDelegate(master_gender_id)
    if gender != "":
        if master_gender.update(gender):
            response_data = SUCCESS.copy()
            response_data["message"] = UPDATED
            response = generic_success_response(response_data)
        else:
            response = ERROR_RESPONSE
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:master_gender_id>', methods=['DELETE'])
@requires_login
@swag_from("docs/master_gender_services/delete_master_gender.yml")
def delete_master_gender(master_gender_id=None):
    master_gender = MasterGenderDelegate(master_gender_id)
    if master_gender.delete():
        response_data = SUCCESS.copy()
        response_data["message"] = DELETED
        response = generic_success_response(response_data)
    else:
        response = INVALID_RESPONSE
    return response


@mod.route('/<int:master_gender_id>', methods=['GET'])
@requires_login
@swag_from("docs/master_gender_services/get_master_gender.yml")
def get_master_gender(master_gender_id=None):
    try:
        master_gender = MasterGenderDelegate(master_gender_id)
        data = master_gender.get()
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
@requires_login
@swag_from("docs/master_gender_services/get_all_master_gender.yml")
def get_all_master_gender():
    try:
        master_gender = MasterGenderDelegate()
        data = master_gender.get_all()
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
