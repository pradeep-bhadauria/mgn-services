import datetime
from mgn import db
from mgn.utils.constants import TRUE, FALSE
from mgn.utils.config import MESSAGE_LIST_PAGINATION_LIMIT
from mgn.models.user_message_thread_participants_model import UserMessageThreadParticipantsModel
from sqlalchemy.sql import and_

class UserMessageThreadParticipantsRepository:
    master_user_id = None
    user_message_thread_id = None

    def __init__(self, master_user_id=None, user_message_thread_id=None):
        self.master_user_id = master_user_id
        self.user_message_thread_id = user_message_thread_id

    def add_self(self):
        try:
            data = UserMessageThreadParticipantsModel(
                    master_user_id=self.master_user_id,
                    user_message_thread_id=self.user_message_thread_id
            )
            db.session.add(data)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def add_participants(self, participant_list=None):
        try:
            for participant in participant_list:
                data = UserMessageThreadParticipantsModel(
                        master_user_id=participant,
                        user_message_thread_id=self.user_message_thread_id
                )
                db.session.add(data)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_is_deleted(self):
        try:
            UserMessageThreadParticipantsModel.query.filter_by(
                    user_message_thread_id=self.user_message_thread_id,
                    master_user_id=self.master_user_id
            ).update(dict(
                    is_deleted=TRUE,
                    delete_timestamp=datetime.datetime.utcnow()
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_is_spam(self, is_spam=None):
        try:
            UserMessageThreadParticipantsModel.query.filter_by(
                    user_message_thread_id=self.user_message_thread_id,
                    master_user_id=self.master_user_id
            ).update(dict(
                    is_spam=is_spam,
                    spam_timestamp=datetime.datetime.utcnow()
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_has_left_group(self):
        try:
            UserMessageThreadParticipantsModel.query.filter_by(
                    user_message_thread_id=self.user_message_thread_id,
                    master_user_id=self.master_user_id
            ).update(dict(
                    has_left_group=TRUE,
                    has_left_group_timestamp=datetime.datetime.utcnow()
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_is_muted(self, is_muted=None):
        try:
            UserMessageThreadParticipantsModel.query.filter_by(
                    user_message_thread_id=self.user_message_thread_id,
                    master_user_id=self.master_user_id
            ).update(dict(
                    is_muted=is_muted,
                    is_muted_timestamp=datetime.datetime.utcnow()
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_is_read(self, is_read=None):
        try:
            UserMessageThreadParticipantsModel.query.filter_by(
                    user_message_thread_id=self.user_message_thread_id,
                    master_user_id=self.master_user_id
            ).update(dict(
                    is_read=is_read
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def archive_thread(self):
        try:
            UserMessageThreadParticipantsModel.query.filter_by(
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

    def unarchive_thread(self):
        try:
            UserMessageThreadParticipantsModel.query.filter_by(
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

    def update_last_read_time(self):
        try:
            UserMessageThreadParticipantsModel.query.filter_by(
                    user_message_thread_id=self.user_message_thread_id,
                    master_user_id=self.master_user_id
            ).update(dict(
                    last_read_timestamp=datetime.datetime.utcnow()
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_unread_count(self):
        try:
            UserMessageThreadParticipantsModel.query.filter_by(
                    user_message_thread_id=self.user_message_thread_id,
                    master_user_id=self.master_user_id
            ).update(dict(
                    unread_message_count=UserMessageThreadParticipantsModel.unread_message_count + 1
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_thread_new_message(self):
        try:
            UserMessageThreadParticipantsModel.query.filter_by(
                    user_message_thread_id=self.user_message_thread_id
            ).update(dict(
                    unread_message_count=UserMessageThreadParticipantsModel.unread_message_count + 1,
                    last_message_timestamp=datetime.datetime.utcnow(),
                    is_read=FALSE

            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_thread_read_messages(self):
        try:
            UserMessageThreadParticipantsModel.query.filter_by(
                    user_message_thread_id=self.user_message_thread_id,
                    master_user_id=self.master_user_id
            ).update(dict(
                    unread_message_count=0,
                    last_read_timestamp=datetime.datetime.utcnow(),
                    is_read=TRUE

            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_last_message_time(self):
        try:
            UserMessageThreadParticipantsModel.query.filter_by(
                    user_message_thread_id=self.user_message_thread_id,
                    master_user_id=self.master_user_id
            ).update(dict(
                    last_message_timestamp=datetime.datetime.utcnow()
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def get_user_threads(self, offset=0):
        try:
            threads = UserMessageThreadParticipantsModel.query.filter(
                    and_(
                            UserMessageThreadParticipantsModel.master_user_id == self.master_user_id,
                            UserMessageThreadParticipantsModel.is_deleted == FALSE,
                            UserMessageThreadParticipantsModel.archive == FALSE,
                            UserMessageThreadParticipantsModel.is_spam == FALSE,
                            UserMessageThreadParticipantsModel.last_message_timestamp != None
                    )
            ).order_by('last_message_timestamp desc').offset(offset).limit(MESSAGE_LIST_PAGINATION_LIMIT)
            return threads
        except:
            db.session.rollback()
            raise

    def get_thread_participants(self, offset=0):
        try:
            participants = UserMessageThreadParticipantsModel.query.filter_by(
                    user_message_thread_id=self.user_message_thread_id
            ).order_by('last_message_timestamp desc').offset(offset).limit(MESSAGE_LIST_PAGINATION_LIMIT)
            return participants
        except:
            db.session.rollback()
            raise

    def get_spam(self, offset=0):
        try:
            threads = UserMessageThreadParticipantsModel.query.filter(
                    and_(
                            UserMessageThreadParticipantsModel.master_user_id == self.master_user_id,
                            UserMessageThreadParticipantsModel.is_deleted == FALSE,
                            UserMessageThreadParticipantsModel.archive == FALSE,
                            UserMessageThreadParticipantsModel.is_spam == TRUE,
                            UserMessageThreadParticipantsModel.last_message_timestamp != None
                    )
            ).order_by('last_message_timestamp desc').offset(offset).limit(MESSAGE_LIST_PAGINATION_LIMIT)
            return threads
        except:
            db.session.rollback()
            raise

    def get_archive(self, offset=0):
        try:
            threads = UserMessageThreadParticipantsModel.query.filter(
                    and_(
                            UserMessageThreadParticipantsModel.master_user_id == self.master_user_id,
                            UserMessageThreadParticipantsModel.is_deleted == FALSE,
                            UserMessageThreadParticipantsModel.archive == TRUE,
                            UserMessageThreadParticipantsModel.is_spam == FALSE,
                            UserMessageThreadParticipantsModel.last_message_timestamp != None
                    )
            ).order_by('last_message_timestamp desc').offset(offset).limit(MESSAGE_LIST_PAGINATION_LIMIT)
            return threads
        except:
            db.session.rollback()
            raise

    def get_unread(self, offset=0):
        try:
            threads = UserMessageThreadParticipantsModel.query.filter(
                    and_(
                            UserMessageThreadParticipantsModel.master_user_id == self.master_user_id,
                            UserMessageThreadParticipantsModel.is_deleted == FALSE,
                            UserMessageThreadParticipantsModel.archive == FALSE,
                            UserMessageThreadParticipantsModel.is_spam == FALSE,
                            UserMessageThreadParticipantsModel.is_read == FALSE,
                            UserMessageThreadParticipantsModel.last_message_timestamp != None
                    )
            ).order_by('last_message_timestamp desc').offset(offset).limit(MESSAGE_LIST_PAGINATION_LIMIT)
            return threads
        except:
            db.session.rollback()
            raise
