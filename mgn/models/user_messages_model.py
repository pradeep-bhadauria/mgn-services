import datetime
from mgn import db
from mgn.models.master_user_model import MasterUserModel
from mgn.utils.constants import FALSE


class UserMessageModel(db.Model):
    __tablename__ = 'user_messages'
    __table_args__ = {"schema": "mgn"}
    user_message_id = db.Column(db.Integer, primary_key=True)
    sent_from_master_user_id = db.Column(db.Integer, db.ForeignKey(MasterUserModel.master_user_id), nullable=False)
    """Thread foreign key removed because of compile exception"""
    user_message_thread_id = db.Column(db.Integer, nullable=False)
    message_text = db.Column(db.String(400), nullable=False)
    has_attachment = db.Column(db.SmallInteger, nullable=False)
    attachment_url = db.Column(db.String(200), nullable=False)
    created = db.Column(db.DateTime, nullable=False)

    sent_from_master_user = db.relationship('MasterUserModel',
                                            backref=db.backref('sent_from_master_user', lazy='dynamic'))

    @property
    def id(self):
        return self.user_message_id

    def __init__(self, sent_from_master_user_id=None, user_message_thread_id=None, message_text=None,
                 has_attachment=FALSE, attachment_url=None):
        self.sent_from_master_user_id = sent_from_master_user_id
        self.user_message_thread_id = user_message_thread_id
        self.message_text = message_text
        self.has_attachment = has_attachment
        self.attachment_url = attachment_url
        self.created = datetime.datetime.utcnow()

    @property
    def serialize(self):
        return {
            'id': self.user_message_id,
            'sent_from_master_user': self.sent_from_master_user.serialize,
            'message_text': self.message_text,
            'has_attachment': self.has_attachment,
            'attachment_url': self.attachment_url,
            'created': str(self.created)
        }
