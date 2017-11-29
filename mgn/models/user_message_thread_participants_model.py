import datetime
from flask import json
from mgn import db
from mgn.utils.constants import FALSE
from mgn.models.master_user_model import MasterUserModel
from mgn.models.user_message_threads_model import UserMessageThreadsModel
from sqlalchemy.sql import and_

class UserMessageThreadParticipantsModel(db.Model):
    __tablename__ = 'user_message_thread_participants'
    __table_args__ = {"schema": "mgn"}
    user_message_thread_participants_id = db.Column(db.Integer, primary_key=True)
    master_user_id = db.Column(db.Integer, db.ForeignKey(MasterUserModel.master_user_id), nullable=False)
    user_message_thread_id = db.Column(db.Integer, db.ForeignKey(UserMessageThreadsModel.user_message_thread_id),
                                       nullable=False)
    is_deleted = db.Column(db.SmallInteger, nullable=True)
    delete_timestamp = db.Column(db.DateTime, nullable=True)
    is_spam = db.Column(db.SmallInteger, nullable=True)
    spam_timestamp = db.Column(db.DateTime, nullable=True)
    has_left_group = db.Column(db.SmallInteger, nullable=True)
    has_left_group_timestamp = db.Column(db.DateTime, nullable=True)
    is_muted = db.Column(db.SmallInteger, nullable=True)
    is_muted_timestamp = db.Column(db.DateTime, nullable=True)
    is_read = db.Column(db.SmallInteger, nullable=True)
    last_read_timestamp = db.Column(db.DateTime, nullable=True)
    unread_message_count = db.Column(db.SmallInteger, nullable=True)
    last_message_timestamp = db.Column(db.DateTime, nullable=True)
    archive = db.Column(db.SmallInteger, nullable=True)

    participants_message_thread = db.relationship('UserMessageThreadsModel',
                                     backref=db.backref('participants_message_thread', lazy='dynamic'))
    message_thread_master_user = db.relationship('MasterUserModel',
                                                 backref=db.backref('message_thread_master_user', lazy='dynamic'))

    @property
    def id(self):
        return self.user_message_thread_participants_id

    def __init__(self, master_user_id=None, user_message_thread_id=None):
        self.master_user_id = master_user_id
        self.user_message_thread_id = user_message_thread_id
        self.is_deleted = FALSE
        self.is_spam = FALSE
        self.is_muted = FALSE
        self.is_read = FALSE
        self.has_left_group = FALSE
        self.archive = FALSE
        self.unread_message_count = 0

    @staticmethod
    def get_participants(thread_id=None, master_user_id=None):
        data = UserMessageThreadParticipantsModel.query.filter(
            and_(
                UserMessageThreadParticipantsModel.user_message_thread_id == thread_id,
                UserMessageThreadParticipantsModel.master_user_id != master_user_id
            )
        )
        result = [i.serialize_participants for i in data.all()]
        return json.dumps(result)


    @property
    def serialize(self):
        return {
            'message_thread_master_user': self.message_thread_master_user.serialize,
            'message_thread': self.participants_message_thread.serialize,
            'is_deleted': self.is_deleted,
            'delete_timestamp': str(self.delete_timestamp),
            'is_spam': self.is_spam,
            'spam_timestamp': str(self.spam_timestamp),
            'has_left_group': self.has_left_group,
            'has_left_group_timestamp': str(self.has_left_group_timestamp),
            'is_muted': self.is_muted,
            'is_muted_timestamp': str(self.is_muted_timestamp),
            'is_read': self.is_read,
            'last_read_timestamp': str(self.last_read_timestamp),
            'unread_message_count': self.unread_message_count,
            'last_message_timestamp': self.last_message_timestamp,
            'participants': str(self.get_participants(self.user_message_thread_id, self.master_user_id))
        }

    @property
    def serialize_participants(self):
        return self.message_thread_master_user.serialize
