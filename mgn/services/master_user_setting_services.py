from flask import Blueprint, request
from mgn.utils.constants import *
from mgn.utils.general_response import *
from mgn.delegates.master_user_setting_delegate import MasterUserSettingDelegate
from voluptuous import Schema, Required, MultipleInvalid
from flasgger.utils import swag_from
from mgn.utils.decorators import requires_login

mod = Blueprint('master_user_setting_services', __name__, url_prefix='/settings')


@mod.route('/', methods=['POST'])
@swag_from("docs/master_user_setting_services/add_master_user_setting.yml")
def add_master_user_setting():
    data_request = request.get_json()
    schema = Schema({
        Required("user_id"): int,
        Required("language_id"): int,
        Required("timezone_id"): int,
        Required("currency_id"): int
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    user_id = data_request.get('user_id')
    language_id = data_request.get('language_id')
    timezone_id = data_request.get('timezone_id')
    currency_id = data_request.get('currency_id')
    master_user_setting = MasterUserSettingDelegate()
    if master_user_setting.add(user_id, language_id, timezone_id, currency_id):
        response_data = SUCCESS.copy()
        response_data["message"] = ADDED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:master_user_id>/language', methods=['PUT'])
@swag_from("docs/master_user_setting_services/update_master_language.yml")
def update_master_language(master_user_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("language_id"): int
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    language_id = data_request.get('language_id')
    master_user_setting = MasterUserSettingDelegate(master_user_id)
    if master_user_setting.update_language(language_id):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:master_user_id>/timezone', methods=['PUT'])
@swag_from("docs/master_user_setting_services/update_timezone.yml")
def update_timezone(master_user_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("timezone_id"): int
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    timezone_id = data_request.get('timezone_id')
    master_user_setting = MasterUserSettingDelegate(master_user_id)
    if master_user_setting.update_timezone(timezone_id):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:master_user_id>/currency', methods=['PUT'])
@swag_from("docs/master_user_setting_services/update_currency.yml")
def update_currency(master_user_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("currency_id"): int
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    currency_id = data_request.get('currency_id')
    master_user_setting = MasterUserSettingDelegate(master_user_id)
    if master_user_setting.update_currency(currency_id):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:master_user_id>', methods=['GET'])
@swag_from("docs/master_user_setting_services/get_master_user_setting.yml")
def get_master_user_setting(master_user_id=None):
    try:
        master_user_setting = MasterUserSettingDelegate(master_user_id)
        data = master_user_setting.get()
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
