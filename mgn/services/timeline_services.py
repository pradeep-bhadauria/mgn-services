from flask import Blueprint, request
from mgn.utils.constants import *
from mgn.utils.general_response import *
from mgn.delegates.timeline_delegate import TimelineDelegate
from flasgger.utils import swag_from
from mgn.utils.decorators import requires_login

mod = Blueprint('timeline_services', __name__, url_prefix='/<int:master_user_id>')


@mod.route('/timeline/offset/<int:offset>', methods=['GET'])
def get_timeline(master_user_id=None,offset=None):
    try:
        timeline = TimelineDelegate(master_user_id)
        data = timeline.get_timiline(offset)
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

@mod.route('/feeds/offset/<int:offset>', methods=['GET'])
def get_feeds(master_user_id=None,offset=None):
    try:
        timeline = TimelineDelegate(master_user_id)
        data = timeline.get_feeds(offset)
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