from flask import json, Response
from mgn.utils.constants import UNAUTHENTICATED, UNAUTHORIZED, ERROR, INVALID, FAILURE


def prepare_response(data, status):
    response = Response(json.dumps(data), status=status, mimetype='application/json')
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Origin, X-Requested-With, Content-Type, Accept, Cache-Control, Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE, OPTIONS')
    return response


def generic_success_response(data):
    return prepare_response(data, 200)


def generic_error_response(data):
    return prepare_response(data, 400)


ERROR_RESPONSE = prepare_response(ERROR, 400)

INVALID_RESPONSE = prepare_response(INVALID, 400)

UNAUTHENTICATED_RESPONSE = prepare_response(UNAUTHENTICATED, 401)

UNAUTHORIZED_RESPONSE = prepare_response(UNAUTHORIZED, 403)

FAILURE_RESPONSE = prepare_response(FAILURE, 500)


def multiple_invalid_response(e=None):
    response_data = ERROR.copy()
    response_data["message"] = e.msg
    response_data["attribute"] = str(e.path[0])
    response = generic_error_response(response_data)
    return response
