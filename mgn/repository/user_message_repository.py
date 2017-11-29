import datetime
from mgn import db
from mgn.models.user_messages_model import UserMessageModel
from sqlalchemy.sql import or_, and_
from mgn.utils.constants import FALSE
from sqlalchemy.types import Integer


class UserMessageRepository:
    master_user_id = None
    thread_id = None

    def __init__(self, master_user_id=None, thread_id=None):
        self.master_user_id = master_user_id
        self.thread_id = thread_id

    def add(self, message_text=None, has_attachment=None, attachment_url=None):
        try:
            data = UserMessageModel(
                    sent_from_master_user_id=self.master_user_id,
                    user_message_thread_id=self.thread_id,
                    message_text=message_text,
                    has_attachment=has_attachment,
                    attachment_url=attachment_url
            )
            db.session.add(data)
            db.session.flush()
            message_id = data.user_message_id
            db.session.commit()
            return message_id
        except:
            db.session.rollback()
            raise
