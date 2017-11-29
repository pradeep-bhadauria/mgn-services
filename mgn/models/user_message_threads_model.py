import datetime
from mgn import db
from mgn.models.master_user_model import MasterUserModel
from mgn.models.user_messages_model import UserMessageModel


class UserMessageThreadsModel(db.Model):
    __tablename__ = 'user_message_threads'
    __table_args__ = {"schema": "mgn"}
    user_message_thread_id = db.Column(db.Integer, primary_key=True)
    thread_creator_master_user_id = db.Column(db.Integer, db.ForeignKey(MasterUserModel.master_user_id), nullable=False)
    last_user_message_id = db.Column(db.Integer, db.ForeignKey(UserMessageModel.user_message_id),
                                     nullable=True)
    created = db.Column(db.DateTime, nullable=False)

    last_user_message = db.relationship('UserMessageModel',
                                        backref=db.backref('last_user_message', lazy='dynamic'))
    message_thread_creator = db.relationship('MasterUserModel',
                                             backref=db.backref('message_thread_creator', lazy='dynamic'))

    @property
    def id(self):
        return self.user_message_thread_id

    def __init__(self, thread_creator_master_user_id=None):
        self.thread_creator_master_user_id = thread_creator_master_user_id
        self.created = datetime.datetime.utcnow()

    @property
    def serialize(self):
        if self.last_user_message is not None:
            return {
                'message_thread_creator': self.message_thread_creator.serialize,
                'last_user_message': self.last_user_message.serialize,
                'created': str(self.created),
                'id': self.user_message_thread_id
            }
        else:
            return {
                'message_thread_creator': self.message_thread_creator.serialize,
                'last_user_message': self.last_user_message,
                'created': str(self.created),
                'id': self.user_message_thread_id
            }
