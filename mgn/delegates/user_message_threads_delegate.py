from mgn.repository.user_message_threads_repository import UserMessageThreadsRepository


class UserMessageThreadsDelegate:
    user_message_thread = None

    def __init__(self, message_thread_id=None):
        if message_thread_id is not None:
            self.user_message_thread = UserMessageThreadsRepository(message_thread_id)
        else:
            self.user_message_thread = UserMessageThreadsRepository()

    def add(self, master_user_id=None):
        try:
            thread_id = self.user_message_thread.add(master_user_id)
        except:
            return None
        return thread_id

    def update_last_user_message(self, last_message_id=None):
        try:
            self.user_message_thread.update_last_user_message(last_message_id)
        except:
            return False
        return True
