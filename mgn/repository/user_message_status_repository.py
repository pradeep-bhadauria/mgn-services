import datetime
from mgn import db
from mgn.utils.constants import TRUE, FALSE
from mgn.utils.config import MESSAGE_PAGINATION_LIMIT
from mgn.models.user_message_status_model import UserMessageStatusModel
from mgn.models.user_message_thread_participants_model import UserMessageThreadParticipantsModel


class UserMessageStatusRepository:
    master_user_id = None
    user_message_thread_id = None

    def __init__(self, master_user_id=None, user_message_thread_id=None):
        self.master_user_id = master_user_id
        self.user_message_thread_id = user_message_thread_id

    def add(self, user_message_id=None):
        try:
            participant_list = UserMessageThreadParticipantsModel.query.filter_by(
                user_message_thread_id=self.user_message_thread_id
            ).all()
            for participant in participant_list:
                data = UserMessageStatusModel(
                        master_user_id=participant.master_user_id,
                        user_message_thread_id=self.user_message_thread_id,
                        user_message_id=user_message_id
                )
                db.session.add(data)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_is_deleted(self):
        try:
            UserMessageStatusModel.query.filter_by(
                    user_message_thread_id=self.user_message_thread_id,
                    master_user_id=self.master_user_id,
                    is_deleted=FALSE
            ).update(dict(
                    is_deleted=TRUE,
                    delete_timestamp=datetime.datetime.utcnow()
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_is_read(self):
        try:
            UserMessageStatusModel.query.filter_by(
                    user_message_thread_id=self.user_message_thread_id,
                    master_user_id=self.master_user_id,
                    is_read=FALSE
            ).update(dict(
                    is_read=TRUE,
                    read_timestamp=datetime.datetime.utcnow()
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def archive_messages(self):
        try:
            UserMessageStatusModel.query.filter_by(
                    user_message_thread_id=self.user_message_thread_id,
                    master_user_id=self.master_user_id,
                    archive=FALSE
            ).update(dict(
                    archive=TRUE
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def unarchive_messages(self):
        try:
            UserMessageStatusModel.query.filter_by(
                    user_message_thread_id=self.user_message_thread_id,
                    master_user_id=self.master_user_id,
                    archive=TRUE
            ).update(dict(
                    archive=FALSE
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def get_user_messages(self,offset=0):
        try:
            messages = UserMessageStatusModel.query.filter_by(
                    user_message_thread_id=self.user_message_thread_id,
                    master_user_id=self.master_user_id,
                    is_deleted=FALSE,
                    archive=FALSE
            ).order_by('created desc').offset(offset).limit(MESSAGE_PAGINATION_LIMIT)
            return messages
        except:
            db.session.rollback()
            raise

    def get_archive(self, offset=0):
        try:
            threads = UserMessageStatusModel.query.filter_by(
                    user_message_thread_id=self.user_message_thread_id,
                    master_user_id=self.master_user_id,
                    is_deleted=FALSE,
                    archive=TRUE
            ).order_by('created desc').offset(offset).limit(MESSAGE_PAGINATION_LIMIT)
            return threads
        except:
            db.session.rollback()
            raise
