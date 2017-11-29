from flask import Blueprint
from mgn.utils.constants import *
from mgn.utils.general_response import *
from mgn.delegates.user_notifications_delegate import UserNotificationsDelegate

mod = Blueprint('user_notifications_services', __name__, url_prefix='/notifications')


@mod.route('/<int:master_user_id>', methods=['GET'])
def get(master_user_id=None):
    user_type = UserNotificationsDelegate(master_user_id)
    data = user_type.get()
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
def update(master_user_id=None):
    user_type = UserNotificationsDelegate(master_user_id)
    data = user_type.update()
    if data is not None:
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response_data = ERROR.copy()
        response_data["message"] = INVALID_ID
        response = generic_error_response(response_data)
    return response