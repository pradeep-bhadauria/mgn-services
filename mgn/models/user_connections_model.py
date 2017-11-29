import datetime
from mgn import db
from mgn.models.master_user_model import MasterUserModel
from mgn.models.user_message_thread_participants_model import UserMessageThreadParticipantsModel
from mgn.utils.constants import FALSE


class UserConnectionsModel(db.Model):
    __tablename__ = 'user_connections'
    __table_args__ = {"schema": "mgn"}
    user_connection_id = db.Column(db.Integer, primary_key=True)
    connected_from_id = db.Column(db.Integer, db.ForeignKey(MasterUserModel.master_user_id), nullable=False)
    connected_to_id = db.Column(db.Integer, db.ForeignKey(MasterUserModel.master_user_id), nullable=False)
    user_message_thread_id = db.Column(db.Integer, db.ForeignKey(
            UserMessageThreadParticipantsModel.user_message_thread_id), nullable=True)
    is_accepted = db.Column(db.SmallInteger, nullable=False)
    is_blocked = db.Column(db.SmallInteger, nullable=False)
    is_ignored = db.Column(db.SmallInteger, nullable=False)
    created = db.Column(db.DateTime, nullable=False)

    master_user_from = db.relationship('MasterUserModel', foreign_keys=[connected_from_id],
                                       backref=db.backref('master_user_from', lazy='dynamic'))
    master_user_to = db.relationship('MasterUserModel', foreign_keys=[connected_to_id],
                                     backref=db.backref('master_user_to', lazy='dynamic'))
    connection_message_thread = db.relationship('UserMessageThreadParticipantsModel',
                                                backref=db.backref('connection_message_thread', lazy='dynamic'))

    @property
    def id(self):
        return self.user_connection_id

    def __init__(self, connected_from_id=None, connected_to_id=None):
        self.connected_from_id = connected_from_id
        self.connected_to_id = connected_to_id
        self.is_accepted = FALSE
        self.is_blocked = FALSE
        self.is_ignored = FALSE
        self.created = datetime.datetime.utcnow()

    @property
    def serialize(self):
        return {
            'connection': self.master_user_to.serialize,
            'message_thread': self.user_message_thread_id,
            'accepted': self.is_accepted,
            'blocked': self.is_blocked,
            'ignored': self.is_ignored,
            'created': str(self.created)
        }
