from flask import Blueprint, request
from voluptuous.schema_builder import Schema, Required, Optional
from voluptuous.validators import All, MultipleInvalid, Length, LengthInvalid
from mgn.utils.constants import *
from mgn.utils.general_response import *
from mgn.utils.validations import *
from mgn.delegates.user_messages_delegate import UserMessageDelegate
from mgn.delegates.user_message_threads_delegate import UserMessageThreadsDelegate
from mgn.delegates.user_message_thread_participants_delegate import UserMessageThreadParticipantsDelegate
from mgn.delegates.user_message_status_delegate import UserMessageStatusDelegate

mod = Blueprint('user_messages_services', __name__,
                url_prefix='/<int:master_user_id>/message-threads')

""" User Message Module """


@mod.route('/<int:thread_id>/message', methods=['POST'])
def add_message(master_user_id=None, thread_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("message_text"): All(str, Length(min=1, max=400)),
        Required("has_attachment"): All(int, validate_is_active),
        Optional("attachment_url"): Url
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    message_text = data_request.get('message_text')
    has_attachment = data_request.get('has_attachment')
    try:
        attachment_url = data_request.get('attachment_url')
    except:
        attachment_url = ""
    message = UserMessageDelegate(master_user_id, thread_id)
    message_id = message.add(message_text, has_attachment, attachment_url)
    if message_id is not None:
        message_status = UserMessageStatusDelegate(master_user_id, thread_id)
        if message_status.add(message_id):
            thread = UserMessageThreadsDelegate(thread_id)  # update threads last message
            updated_last_user_message = thread.update_last_user_message(message_id)
            thread_participants = UserMessageThreadParticipantsDelegate(master_user_id,
                                                                        thread_id)  # update thread for new message info
            updated_thread_participant_new_message = thread_participants.update_thread_new_message()
            if updated_last_user_message and updated_thread_participant_new_message:
                response_data = SUCCESS.copy()  # return success response
                response_data["message"] = ADDED
                response = generic_success_response(response_data)
            else:
                response = FAILURE_RESPONSE
        else:
            response = ERROR_RESPONSE
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:thread_id>/messages/offset/<int:offset>', methods=['GET'])
def get_messages(master_user_id=None, thread_id=None, offset=0):
    messages = UserMessageStatusDelegate(master_user_id, thread_id)
    thread = UserMessageThreadParticipantsDelegate(master_user_id, thread_id)
    data = messages.get_user_messages(offset)
    updated_thread_read_messages = thread.update_thread_read_messages()
    updated_message_is_read = messages.update_is_read()
    if data is not None and updated_thread_read_messages and updated_message_is_read:
        response_data = SUCCESS.copy()
        response_data["data"] = data
        response = generic_success_response(response_data)
    else:
        response = FAILURE_RESPONSE
    return response


""" User Message Thread Module """


@mod.route('/', methods=['POST'])
def add_thread(master_user_id=None):
    thread = UserMessageThreadsDelegate()
    thread_id = thread.add(master_user_id)
    if thread_id is not None:
        thread_participant = UserMessageThreadParticipantsDelegate(master_user_id, thread_id)
        if thread_participant.add_self():
            response_data = SUCCESS.copy()
            response_data["data"] = thread_id
            response_data["message"] = ADDED
            response = generic_success_response(response_data)
        else:
            response = INVALID_RESPONSE
    else:
        response = INVALID_RESPONSE
    return response


@mod.route('/<int:thread_id>/participants', methods=['POST'])
def add_thread_participants(master_user_id=None, thread_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("participant_list"): All(validate_message_participant_list)
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    participant_list = data_request.get('participant_list')
    thread_participant = UserMessageThreadParticipantsDelegate(master_user_id, thread_id)
    if thread_participant.add_participants(participant_list):
        response_data = SUCCESS.copy()
        response_data["message"] = ADDED
        response = generic_success_response(response_data)
    else:
        response = INVALID_RESPONSE
    return response


@mod.route('/<int:thread_id>/spam', methods=['PUT'])
def update_is_spam(master_user_id=None, thread_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("is_spam"): All(int, validate_is_active)
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    is_spam = data_request.get('is_spam')
    thread = UserMessageThreadParticipantsDelegate(master_user_id, thread_id)
    if thread.update_is_spam(is_spam):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:thread_id>/mute', methods=['PUT'])
def update_is_mute(master_user_id=None, thread_id=None):
    data_request = request.get_json()
    schema = Schema({
        Required("is_muted"): All(int, validate_is_active)
    })
    try:
        schema(data_request)
    except MultipleInvalid as e:
        return multiple_invalid_response(e)
    is_muted = data_request.get('is_muted')
    thread = UserMessageThreadParticipantsDelegate(master_user_id, thread_id)
    if thread.update_is_muted(is_muted):
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:thread_id>/archive', methods=['PUT'])
def archive(master_user_id=None, thread_id=None):
    thread = UserMessageThreadParticipantsDelegate(master_user_id, thread_id)
    if thread.archive_thread():
        messages = UserMessageStatusDelegate(master_user_id)
        if messages.archive_messages():
            response_data = SUCCESS.copy()
            response_data["message"] = UPDATED
            response = generic_success_response(response_data)
        else:
            response = ERROR_RESPONSE
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:thread_id>/unarchive', methods=['PUT'])
def unarchive(master_user_id=None, thread_id=None):
    thread = UserMessageThreadParticipantsDelegate(master_user_id, thread_id)
    if thread.unarchive_thread():
        messages = UserMessageStatusDelegate(master_user_id)
        if messages.unarchive_messages():
            response_data = SUCCESS.copy()
            response_data["message"] = UPDATED
            response = generic_success_response(response_data)
        else:
            response = ERROR_RESPONSE
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:thread_id>/exit', methods=['PUT'])
def update_has_left_group(master_user_id=None, thread_id=None):
    thread = UserMessageThreadParticipantsDelegate(master_user_id, thread_id)
    if thread.update_has_left_group():
        response_data = SUCCESS.copy()
        response_data["message"] = UPDATED
        response = generic_success_response(response_data)
    else:
        response = ERROR_RESPONSE
    return response


@mod.route('/<int:thread_id>', methods=['DELETE'])
def update_is_deleted(master_user_id=None, thread_id=None):
    thread = UserMessageThreadParticipantsDelegate(master_user_id, thread_id)
    if thread.update_is_deleted():
        messages = UserMessageStatusDelegate(master_user_id)
        if messages.update_is_deleted():
            response_data = SUCCESS.copy()
            response_data["message"] = DELETED
            response = generic_success_response(response_data)
        else:
            response = FAILURE_RESPONSE
    else:
        response = FAILURE_RESPONSE
    return response


@mod.route('/offset/<int:offset>', methods=['GET'])
def get_user_threads(master_user_id=None, offset=0):
    try:
        mt = UserMessageThreadParticipantsDelegate(master_user_id)
        data = mt.get_user_threads(offset)
    except:
        response = FAILURE_RESPONSE
        return response
    if data is not None:
        response_data = SUCCESS.copy()
        response_data["data"] = data
        response = generic_success_response(response_data)
    else:
        response = INVALID_RESPONSE
    return response


@mod.route('/unread/offset/<int:offset>', methods=['GET'])
def get_unread_threads(master_user_id=None, offset=0):
    try:
        mt = UserMessageThreadParticipantsDelegate(master_user_id)
        data = mt.get_unread(offset)
    except:
        response = FAILURE_RESPONSE
        return response
    if data is not None:
        response_data = SUCCESS.copy()
        response_data["data"] = data
        response = generic_success_response(response_data)
    else:
        response = INVALID_RESPONSE
    return response


@mod.route('/spam/offset/<int:offset>', methods=['GET'])
def get_spam_threads(master_user_id=None, offset=0):
    try:
        mt = UserMessageThreadParticipantsDelegate(master_user_id)
        data = mt.get_spam(offset)
    except:
        response = FAILURE_RESPONSE
        return response
    if data is not None:
        response_data = SUCCESS.copy()
        response_data["data"] = data
        response = generic_success_response(response_data)
    else:
        response = INVALID_RESPONSE
    return response


@mod.route('/archive/offset/<int:offset>', methods=['GET'])
def get_archive_threads(master_user_id=None, offset=0):
    try:
        mt = UserMessageThreadParticipantsDelegate(master_user_id)
        data = mt.get_archive(offset)
    except:
        response = FAILURE_RESPONSE
        return response
    if data is not None:
        response_data = SUCCESS.copy()
        response_data["data"] = data
        response = generic_success_response(response_data)
    else:
        response = INVALID_RESPONSE
    return response


@mod.route('/<int:thread_id>/participants/offset/<int:offset>', methods=['GET'])
def get_thread_participants(master_user_id=None, thread_id=None, offset=0):
    try:
        mtp = UserMessageThreadParticipantsDelegate(master_user_id, thread_id)
        data = mtp.get_thread_participants(offset)
    except:
        response = FAILURE_RESPONSE
        return response
    if data is not None:
        response_data = SUCCESS.copy()
        response_data["data"] = data
        response = generic_success_response(response_data)
    else:
        response = INVALID_RESPONSE
    return response
