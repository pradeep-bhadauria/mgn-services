from mgn import db
from mgn.models.master_user_model import MasterUserModel
from sqlalchemy.dialects.postgresql import JSONB


class UserNotificationsModel(db.Model):
    __tablename__ = 'user_notifications'
    __table_args__ = {"schema": "mgn"}
    user_notification_id = db.Column(db.Integer, primary_key=True)
    master_user_id = db.Column(db.Integer, db.ForeignKey(MasterUserModel.master_user_id), nullable=False)
    notifications = db.Column(JSONB, nullable=False)

    notification_user = db.relationship('MasterUserModel', backref=db.backref('notification_user', lazy='dynamic'))
    
    @property
    def id(self):
        return self.user_notification_id

    def __init__(self, master_user_id=None, notifications=None):
        self.master_user_id = master_user_id
        self.notifications = notifications

    @property
    def serialize(self):
        return {
            'id': self.user_notification_id,
            'user': self.notification_user.serialize,
            'notifications': self.notifications
        }
