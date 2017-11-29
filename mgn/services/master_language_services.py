from flask import Blueprint, request
from mgn.utils.constants import *
from mgn.utils.general_response import *
from mgn.delegates.master_language_delegate import MasterLanguageDelegate
from flasgger.utils import swag_from
from mgn.utils.decorators import requires_login
from voluptuous import Schema, Required, MultipleInvalid, Length, All
from mgn.utils.validations import *

mod = Blueprint('master_language_services', __name__, url_prefix='/master-language')


@mod.route('/', methods=['POST'])
@swag_from("docs/master_language_services/add_master_language.yml")
def add_master_language():
    data_request = request.get_json()
    schema = Schema({
        Required("language_name"): All(string_code, Length(min=3, max=50)),
        Required("language_description"): All(str, Length(min=3, max=100)),
        Required("is_active"): All(int, validate_is_active)
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    name = data_request.get('language_name')
    desc = data_request.get('language_description')
    is_active = data_request.get('is_active')
    master_language = MasterLanguageDelegate()
    if name != ''and desc != '' and is_active is not None:
        if master_language.add(name, desc, is_active):
            response_data = SUCCESS.copy()
            response_data["message"] = ADDED
            response = generic_success_response(response_data)
        else:
            response = ERROR_RESPONSE
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:master_language_id>', methods=['PUT'])
@swag_from("docs/master_language_services/update_master_language_details.yml")
def update_master_language_details(master_language_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("language_name"): All(string_code, Length(min=3, max=50)),
        Required("language_description"): All(str, Length(min=3, max=100))
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    name = data_request.get('language_name')
    desc = data_request.get('language_description')
    master_language = MasterLanguageDelegate(master_language_id)
    if name != '' and desc != '':
        if master_language.update_language_details(name, desc):
            response_data = SUCCESS.copy()
            response_data["message"] = UPDATED
            response = generic_success_response(response_data)
        else:
            response = ERROR_RESPONSE
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:master_language_id>/is-active', methods=['PUT'])
@swag_from("docs/master_language_services/update_master_language_active.yml")
def update_master_language_active(master_language_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("is_active"): All(int, validate_is_active)
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    is_active = data_request.get('is_active')
    master_language = MasterLanguageDelegate(master_language_id)
    if is_active != '':
        if master_language.update_language_is_active(is_active):
            response_data = SUCCESS.copy()
            response_data["message"] = UPDATED
            response = generic_success_response(response_data)
        else:
            response = ERROR_RESPONSE
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:master_language_id>', methods=['GET'])
@swag_from("docs/master_language_services/get_master_language.yml")
def get_master_language(master_language_id=None):
    try:
        master_language = MasterLanguageDelegate(master_language_id)
        data = master_language.get()
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
@swag_from("docs/master_language_services/get_all_master_language.yml")
def get_all_master_language():
    try:
        master_language = MasterLanguageDelegate()
        data = master_language.get_all()
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
@swag_from("docs/master_language_services/get_active_master_language.yml")
def get_active_master_language():
    try:
        master_language = MasterLanguageDelegate()
        data = master_language.get_active()
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
@swag_from("docs/master_language_services/get_inactive_master_language.yml")
def get_inactive_master_language():
    try:
        master_language = MasterLanguageDelegate()
        data = master_language.get_inactive()
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
@swag_from("docs/master_language_services/search_master_language.yml")
def search_master_language(q=None):
    try:
        master_language = MasterLanguageDelegate()
        data = master_language.search(q)
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
