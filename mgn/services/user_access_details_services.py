from flask import Blueprint, request
from user_agents import parse
from voluptuous import Schema, Required,All, MultipleInvalid, Length
from mgn.utils.constants import *
from mgn.utils.validations import *
from mgn.utils.general_response import *
from mgn.delegates.user_access_details_delegate import UserAccessDetailsDelegate

mod = Blueprint('user_access_details_services', __name__, url_prefix='/user-access')


@mod.route('/', methods=['POST'])
def add():
    data_request = request.get_json()
    schema = Schema({
        Required("user_id"): validate_user_by_id,
        Required("latitude"): str,
        Required("longitude"): str,
        Required("city"): All(string_val, Length(max=50)),
        Required("state"): All(string_val, Length(max=50)),
        Required("zipcode"): All(alphanumreic_val, Length(max=15)),
        Required("country_code"): All(string_val, Length(max=5))
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    user_agents = parse(request.user_agent.string)
    data_request = request.get_json()
    master_user_id = data_request.get('user_id')
    latitude = data_request.get('latitude')
    longitude = data_request.get('longitude')
    city = data_request.get('city')
    state = data_request.get('state')
    zipcode = data_request.get('zipcode')
    country_code = data_request.get('country_code')
    browser = str(request.user_agent.browser) + "-" + str(request.user_agent.version)
    device = str(user_agents)
    request_string = request.user_agent.string
    platform = request.user_agent.platform

    user_access_details = UserAccessDetailsDelegate()
    if user_access_details.add(master_user_id, latitude, longitude, city, state, zipcode, country_code,
                               browser, device, request_string, platform):
        response_data = SUCCESS.copy()
        response_data["message"] = ADDED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:master_user_id>', methods=['GET'])
def get(master_user_id=None):
    try:
        user_type = UserAccessDetailsDelegate(master_user_id)
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
        response_data["message"] = INVALID_ID
        response = generic_error_response(response_data)
    return response


@mod.route('/<int:master_user_id>', methods=['PUT'])
def update_user_type(master_user_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("latitude"): str,
        Required("longitude"): str,
        Required("city"): All(string_val, Length(max=50)),
        Required("state"): All(string_val, Length(max=50)),
        Required("zipcode"): All(alphanumreic_val, Length(max=15)),
        Required("country_code"): All(string_val, Length(max=5))
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    user_agents = parse(request.user_agent.string)
    latitude = data_request.get('latitude')
    longitude = data_request.get('longitude')
    city = data_request.get('city')
    state = data_request.get('state')
    zipcode = data_request.get('zipcode')
    country_code = data_request.get('country_code')
    browser = str(request.user_agent.browser) + "-" + str(request.user_agent.version)
    device = str(user_agents)
    request_string = request.user_agent.string
    platform = request.user_agent.platform
    user_access_details = UserAccessDetailsDelegate(master_user_id)
    if user_access_details.update(latitude, longitude, city, state, zipcode, country_code, browser, device,
                                  request_string, platform):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response