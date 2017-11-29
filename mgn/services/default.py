from flask import Blueprint, request
from mgn.utils.constants import SUCCESS
from mgn.services.constants import LONG_TOKEN_VALIDITY
from mgn.utils.token import confirm_token
from mgn.utils.general_response import *
from user_agents import parse
from flasgger.utils import swag_from

mod = Blueprint('default', __name__, url_prefix='')


@mod.route('/', methods=['GET'])
@swag_from("docs/default/default.yml")
def default():
    response_data = SUCCESS.copy()
    try:
        user_agents = parse(request.user_agent.string)
        response_data["message"] = "Welcome " + confirm_token(request.cookies['EID'], LONG_TOKEN_VALIDITY)
        response_data["platform"] = request.user_agent.platform
        response_data["browser"] = str(request.user_agent.browser) + "-" + str(request.user_agent.version)
        response_data["device"] = str(user_agents)
        response_data["request_string"] = request.user_agent.string
    except:
        user_agents = parse(request.user_agent.string)
        response_data["message"] = "Unauthorized Access!"
        response_data["platform"] = request.user_agent.platform
        response_data["browser"] = str(request.user_agent.browser) + "-" + str(request.user_agent.version)
        response_data["device"] = str(user_agents)
        response_data["request_string"] = request.user_agent.string
    response = generic_success_response(response_data)
    return response
