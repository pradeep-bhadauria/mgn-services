import datetime
from mgn import db
from mgn.models.master_user_model import MasterUserModel
from mgn.models.user_message_threads_model import UserMessageThreadsModel
from mgn.models.user_messages_model import UserMessageModel
from mgn.utils.constants import FALSE

class UserMessageStatusModel(db.Model):
    __tablename__ = 'user_message_status'
    __table_args__ = {"schema": "mgn"}
    user_message_status_id = db.Column(db.Integer, primary_key=True)
    master_user_id = db.Column(db.Integer, db.ForeignKey(MasterUserModel.master_user_id), nullable=False)
    user_message_thread_id = db.Column(db.Integer, db.ForeignKey(UserMessageThreadsModel.user_message_thread_id),
                                       nullable=False)
    user_message_id = db.Column(db.Integer, db.ForeignKey(UserMessageModel.user_message_id),
                                nullable=False)
    is_deleted = db.Column(db.SmallInteger, nullable=True)
    delete_timestamp = db.Column(db.DateTime, nullable=True)
    is_read = db.Column(db.SmallInteger, nullable=True)
    read_timestamp = db.Column(db.DateTime, nullable=True)
    created = db.Column(db.DateTime, nullable=False)
    archive = db.Column(db.SmallInteger, nullable=True)

    message_thread = db.relationship('UserMessageThreadsModel',
                                     backref=db.backref('message_thread', lazy='dynamic'))
    message_status_master_user = db.relationship('MasterUserModel',
                                                 backref=db.backref('message_status_master_user', lazy='dynamic'))
    user_message = db.relationship('UserMessageModel',
                                   backref=db.backref('user_message', lazy='dynamic'))

    @property
    def id(self):
        return self.user_message_status_id

    def __init__(self, master_user_id=None, user_message_thread_id=None, user_message_id=None,
                 last_message_timestamp=None):
        self.master_user_id = master_user_id
        self.user_message_thread_id = user_message_thread_id
        self.user_message_id = user_message_id
        self.is_read = FALSE
        self.is_deleted = FALSE
        self.archive = FALSE
        self.created = datetime.datetime.utcnow()

    @property
    def serialize(self):
        return {
            'message': self.user_message.serialize,
            'is_deleted': self.is_deleted,
            'delete_timestamp': str(self.delete_timestamp),
            'is_read': self.is_read,
            'read_timestamp': str(self.read_timestamp),
            'created': self.created
        }
