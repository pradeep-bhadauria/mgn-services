from flask import Blueprint, request
from mgn.utils.constants import *
from mgn.utils.general_response import *
from mgn.utils.validations import *
from mgn.utils.decorators import requires_login
from voluptuous import Schema, Required, MultipleInvalid, All, Length
from flasgger.utils import swag_from
from mgn.delegates.master_currency_delegate import MasterCurrencyDelegate

mod = Blueprint('master_currency_services', __name__, url_prefix='/master-currency')


@mod.route('/', methods=['POST'])
@requires_login
@swag_from("docs/master_currency_services/add_master_currency.yml")
def add_master_currency():
    data_request = request.get_json()
    schema = Schema({
        Required("currency_code"): All(string_val, Length(max=10)),
        Required("currency_name"): All(string_val, Length(max=50)),
        Required("currency_symbol"): All(str, Length(max=30)),
        Required("currency_description"): All(str, Length(max=100)),
        Required("is_active"): validate_is_active,
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        multiple_invalid_response(e)
    code = data_request.get('currency_code')
    name = data_request.get('currency_name')
    symbol = data_request.get('currency_symbol')
    desc = data_request.get('currency_description')
    is_active = data_request.get('is_active')
    master_currency = MasterCurrencyDelegate()
    if master_currency.add(code, name, symbol, desc, is_active):
        response_data = SUCCESS.copy()
        response_data["message"] = ADDED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:master_currency_id>', methods=['PUT'])
@requires_login
@swag_from("docs/master_currency_services/update_master_currency_details.yml")
def update_master_currency_details(master_currency_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("currency_code"): All(string_val, Length(max=10)),
        Required("currency_name"): All(string_val, Length(max=50)),
        Required("currency_symbol"): All(str, Length(max=30)),
        Required("currency_description"): All(str, Length(max=100))
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        multiple_invalid_response(e)
    code = data_request.get('currency_code')
    name = data_request.get('currency_name')
    symbol = data_request.get('currency_symbol')
    desc = data_request.get('currency_description')
    master_currency = MasterCurrencyDelegate(master_currency_id)
    if code != '' and name != '' and symbol != '' and desc != '':
        if master_currency.update_currency_details(code, name, symbol, desc):
            response_data = SUCCESS.copy()
            response_data["message"] = UPDATED
            response = generic_success_response(response_data)
        else:
            response = ERROR_RESPONSE
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:master_currency_id>/is-active', methods=['PUT'])
@requires_login
@swag_from("docs/master_currency_services/update_master_currency_active.yml")
def update_master_currency_active(master_currency_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("is_active"): validate_is_active
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    is_active = data_request.get('is_active')
    master_currency = MasterCurrencyDelegate(master_currency_id)
    if is_active != '':
        if master_currency.update_currency_is_active(is_active):
            response_data = SUCCESS.copy()
            response_data["message"] = UPDATED
            response = generic_success_response(response_data)
        else:
            response = ERROR_RESPONSE
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:master_currency_id>', methods=['GET'])
@requires_login
@swag_from("docs/master_currency_services/get_master_currency.yml")
def get_master_currency(master_currency_id=None):
    try:
        master_currency = MasterCurrencyDelegate(master_currency_id)
        data = master_currency.get()
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
@swag_from("docs/master_currency_services/get_all_master_currency.yml")
def get_all_master_currency():
    try:
        master_currency = MasterCurrencyDelegate()
        data = master_currency.get_all()
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
@requires_login
@swag_from("docs/master_currency_services/get_active_master_currency.yml")
def get_active_master_currency():
    try:
        master_currency = MasterCurrencyDelegate()
        data = master_currency.get_active()
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
@requires_login
@swag_from("docs/master_currency_services/get_inactive_master_currency.yml")
def get_inactive_master_currency():
    try:
        master_currency = MasterCurrencyDelegate()
        data = master_currency.get_inactive()
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
@requires_login
@swag_from("docs/master_currency_services/search_master_currency.yml")
def search_master_currency(q=None):
    try:
        master_currency = MasterCurrencyDelegate()
        data = master_currency.search(q)
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
