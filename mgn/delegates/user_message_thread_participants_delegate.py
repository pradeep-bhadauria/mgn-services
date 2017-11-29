from mgn.repository.user_message_thread_participants_repository import UserMessageThreadParticipantsRepository
from mgn.utils.helper import Helper


class UserMessageThreadParticipantsDelegate:
    user_message_thread = None

    def __init__(self, master_user_id=None, user_message_thread_id=None):
        if master_user_id is not None and user_message_thread_id is not None:
            self.user_message_thread = UserMessageThreadParticipantsRepository(master_user_id, user_message_thread_id)
        elif master_user_id is not None:
            self.user_message_thread = UserMessageThreadParticipantsRepository(master_user_id)
        else:
            self.user_message_thread = UserMessageThreadParticipantsRepository()

    def add_self(self):
        try:
            self.user_message_thread.add_self()
        except:
            return False
        return True

    def add_participants(self, participant_list=None):
        try:
            self.user_message_thread.add_participants(participant_list)
        except:
            return False
        return True

    def update_is_deleted(self):
        try:
            self.user_message_thread.update_is_deleted()
        except:
            return False
        return True

    def update_is_spam(self, is_spam=None):
        try:
            self.user_message_thread.update_is_spam(is_spam)
        except:
            return False
        return True

    def update_has_left_group(self):
        try:
            self.user_message_thread.update_has_left_group()
        except:
            return False
        return True

    def update_is_muted(self, is_muted=None):
        try:
            self.user_message_thread.update_is_muted(is_muted)
        except:
            return False
        return True

    def update_is_read(self, is_read=None):
        try:
            self.user_message_thread.update_is_read(is_read)
        except:
            return False
        return True

    def update_unread_count(self):
        try:
            self.user_message_thread.update_unread_count()
        except:
            raise  # return False
        return True

    def update_last_message_time(self):
        try:
            self.user_message_thread.update_last_message_time()
        except:
            return False
        return True

    def update_thread_new_message(self):
        try:
            self.user_message_thread.update_thread_new_message()
        except:
            return False
        return True

    def update_thread_read_messages(self):
        try:
            self.user_message_thread.update_thread_read_messages()
        except:
            return False
        return True

    def update_last_read_time(self):
        try:
            self.user_message_thread.update_last_read_time()
        except:
            return False
        return True

    def archive_thread(self):
        try:
            self.user_message_thread.archive_thread()
        except:
            return False
        return True

    def unarchive_thread(self):
        try:
            self.user_message_thread.unarchive_thread()
        except:
            return False
        return True

    def get_user_threads(self, offset=0):
        result = self.user_message_thread.get_user_threads(offset)
        if result is not None:
            return Helper.json_list(result)
        return result

    def get_thread_participants(self, offset=0):
        result = self.user_message_thread.get_thread_participants(offset)
        if result is not None:
            return Helper.json_list(result)
        return result

    def get_unread(self, offset=0):
        result = self.user_message_thread.get_unread(offset)
        if result is not None:
            return Helper.json_list(result)
        return result

    def get_spam(self, offset=0):
        result = self.user_message_thread.get_spam(offset)
        if result is not None:
            return Helper.json_list(result)
        return result

    def get_archive(self, offset=0):
        result = self.user_message_thread.get_archive(offset)
        if result is not None:
            return Helper.json_list(result)
        return result
