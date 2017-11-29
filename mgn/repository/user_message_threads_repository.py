from mgn import db
from mgn.models.user_message_threads_model import UserMessageThreadsModel


class UserMessageThreadsRepository:
    user_message_thread_id = None

    def __init__(self, user_message_thread_id=None):
        self.user_message_thread_id = user_message_thread_id

    def add(self, thread_creator_master_user_id=None):
        try:
            data = UserMessageThreadsModel(
                    thread_creator_master_user_id=thread_creator_master_user_id
            )
            db.session.add(data)
            db.session.flush()
            thread_id = data.user_message_thread_id
            db.session.commit()
            return thread_id
        except:
            db.session.rollback()
            raise

    def update_last_user_message(self, last_user_message_id=None):
        try:
            UserMessageThreadsModel.query.filter_by(user_message_thread_id=self.user_message_thread_id).update(dict(
                    last_user_message_id=last_user_message_id
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise
