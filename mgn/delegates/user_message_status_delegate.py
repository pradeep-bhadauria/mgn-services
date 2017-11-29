from mgn.repository.user_message_status_repository import UserMessageStatusRepository
from mgn.utils.helper import Helper


class UserMessageStatusDelegate:
    user_message_status = None

    def __init__(self, master_user_id=None, user_message_thread_id=None):
        if master_user_id is not None and user_message_thread_id is not None:
            self.user_message_status = UserMessageStatusRepository(master_user_id, user_message_thread_id)
        else:
            self.user_message_status = UserMessageStatusRepository()

    def add(self, user_message_id=None):
        try:
            self.user_message_status.add(user_message_id)
        except:
            return False
        return True

    def update_is_deleted(self):
        try:
            self.user_message_status.update_is_deleted()
        except:
            return False
        return True

    def update_is_read(self):
        try:
            self.user_message_status.update_is_read()
        except:
            return False
        return True

    def archive_messages(self):
        try:
            self.user_message_status.archive_messages()
        except:
            return False
        return True

    def unarchive_messages(self):
        try:
            self.user_message_status.unarchive_messages()
        except:
            return False
        return True

    def get_user_messages(self, offset=0):
        result = self.user_message_status.get_user_messages(offset)
        if result is not None:
            return Helper.json_list(result)
        return result

    def get_archive(self, offset=0):
        result = self.user_message_status.get_archive(offset)
        if result is not None:
            return Helper.json_list(result)
        return result
