from flask import json
from mgn.repository.user_connections_repository import UserConnectionsRepository
from mgn.utils.helper import Helper


class UserConnectionsDelegate:
    user_connections = None

    def __init__(self, connected_from_id=None, connected_to_id=None):
        self.user_connections = UserConnectionsRepository(connected_from_id, connected_to_id)

    def add(self):
        result = self.user_connections.add()
        return result

    def update_is_accepted(self, is_accepted=None):
        result = self.user_connections.update_is_accepted(is_accepted)
        return result

    def update_is_blocked(self, is_blocked=None):
        result = self.user_connections.update_is_blocked(is_blocked)
        return result

    def update_is_ignored(self, is_ignored=None):
        result = self.user_connections.update_is_ignored(is_ignored)
        return result

    def update_message_thread(self, message_thread_id=None):
        result = self.user_connections.update_message_thread(message_thread_id)
        return result

    def delete(self):
        result = self.user_connections.delete()
        return result

    def get(self):
        result = self.user_connections.get()
        if result is not None:
            return json.dumps(result.serialize)
        return result

    def get_all(self):
        result = self.user_connections.get_all()
        if result is not None:
            return Helper.json_list(result)
        return result
