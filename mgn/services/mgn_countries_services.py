from flask import Blueprint, request
from mgn.utils.constants import SUCCESS, ADDED, UPDATED
from mgn.utils.general_response import *
from mgn.delegates.mgn_countries_delegate import MgnCountriesDelegate

mod = Blueprint('mgn_countries_services', __name__, url_prefix='/countries')


@mod.route('/', methods=['POST'])
def add_country():
    data_request = request.get_json()
    short_name = data_request.get('short_name')
    full_name = data_request.get('full_name')
    isd_codes = data_request.get('isd_codes')
    states = data_request.get('states')
    cities = data_request.get('cities')
    is_active = data_request.get('is_active')
    countries = MgnCountriesDelegate()
    if short_name != "" and full_name != "" and isd_codes != "" and states != "" and cities != "" and is_active:
        if countries.add(short_name, full_name, isd_codes, states, cities, is_active):
            response_data = SUCCESS.copy()
            response_data["message"] = ADDED
            response = generic_success_response(response_data)
        else:
            response = ERROR_RESPONSE
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:country_id>', methods=['GET'])
def get_country(country_id=None):
    try:
        country = MgnCountriesDelegate(country_id)
        data = country.get()
    except:
        response = FAILURE_RESPONSE
        return response
    if data is not None:
        response_data = SUCCESS.copy()
        response_data["data"] = data
        response = generic_success_response(response_data)
    else:
        ERROR["message"] = "Country doesn't exist"
        response = generic_error_response(ERROR)
    return response


@mod.route('/', methods=['GET'])
def get_all_countries():
    try:
        countries = MgnCountriesDelegate()
        data = countries.get_all()
    except:
        response = FAILURE_RESPONSE
        return response
    if data is not None:
        response_data = SUCCESS.copy()
        response_data["data"] = data
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/country/<int:country_id>', methods=['PUT'])
def update_country(country_id=None):
    try:
        data_request = request.get_json()
        short_name = data_request.get('short_name')
        full_name = data_request.get('full_name')
        isd_code = data_request.get('isd_code')
        country = MgnCountriesDelegate(country_id)
        if short_name != "" and full_name != "" and isd_code != "":
            if country.update_country(short_name, full_name, isd_code):
                response_data = SUCCESS.copy()
                response_data["message"] = UPDATED
                response = generic_success_response(response_data)
            else:
                response = ERROR_RESPONSE
        else:
            response = ERROR_RESPONSE
        return response
    except:
        response = FAILURE_RESPONSE
        return response


@mod.route('/country/<int:country_id>/active', methods=['PUT'])
def update_is_active(country_id=None):
    try:
        data_request = request.get_json()
        is_active = data_request.get('is_active')
        country = MgnCountriesDelegate(country_id)
        if is_active is not None:
            if country.update_is_active(is_active):
                response_data = SUCCESS.copy()
                response_data["message"] = UPDATED
                response = generic_success_response(response_data)
            else:
                response = ERROR_RESPONSE
        else:
            response = ERROR_RESPONSE
        return response
    except:
        response = FAILURE_RESPONSE
        return response


@mod.route('/country/<int:country_id>/states', methods=['PUT'])
def update_states(country_id=None):
    try:
        data_request = request.get_json()
        states = data_request.get('states')
        country = MgnCountriesDelegate(country_id)
        if states is not None:
            if country.update_is_active(states):
                response_data = SUCCESS.copy()
                response_data["message"] = UPDATED
                response = generic_success_response(response_data)
            else:
                response = ERROR_RESPONSE
        else:
            response = ERROR_RESPONSE
        return response
    except:
        response = FAILURE_RESPONSE
        return response


@mod.route('/country/<int:country_id>/cities', methods=['PUT'])
def update_cities(country_id=None):
    try:
        data_request = request.get_json()
        cities = data_request.get('cities')
        country = MgnCountriesDelegate(country_id)
        if cities is not None:
            if country.update_is_active(cities):
                response_data = SUCCESS.copy()
                response_data["message"] = UPDATED
                response = generic_success_response(response_data)
            else:
                response = ERROR_RESPONSE
        else:
            response = ERROR_RESPONSE
        return response
    except:
        response = FAILURE_RESPONSE
        return response
