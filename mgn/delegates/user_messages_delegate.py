from mgn.repository.user_message_repository import UserMessageRepository
from mgn.utils.helper import Helper


class UserMessageDelegate:
    user_message = None

    def __init__(self, master_user_id=None, thread_id=None):
        if master_user_id is not None and thread_id is not None:
            self.user_message = UserMessageRepository(master_user_id, thread_id)
        else:
            self.user_message = UserMessageRepository()

    def add(self, message_text=None, has_attachment=None,attachment_url=None):
        try:
            message_id = self.user_message.add(message_text, has_attachment,attachment_url)
        except:
            raise #return None
        return message_id
