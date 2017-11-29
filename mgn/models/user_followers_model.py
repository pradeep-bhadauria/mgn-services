import datetime
from mgn import db
from mgn.models.master_user_model import MasterUserModel
from mgn.utils.constants import FALSE


class UserFollowersModel(db.Model):
    __tablename__ = 'user_followers'
    __table_args__ = {"schema": "mgn"}
    user_follower_id = db.Column(db.Integer, primary_key=True)
    follower = db.Column(db.Integer, db.ForeignKey(MasterUserModel.master_user_id), nullable=False)
    following = db.Column(db.Integer, db.ForeignKey(MasterUserModel.master_user_id), nullable=False)
    is_blocked = db.Column(db.SmallInteger, nullable=False)
    created = db.Column(db.DateTime, nullable=True)

    follower_user = db.relationship('MasterUserModel', foreign_keys=[follower],
                                    backref=db.backref('follower_user', lazy='dynamic'))
    following_user = db.relationship('MasterUserModel', foreign_keys=[following],
                                     backref=db.backref('following_user', lazy='dynamic'))

    @property
    def id(self):
        return self.user_follower_id

    def __init__(self, follower=None, following=None):
        self.follower = follower
        self.following = following
        self.is_blocked = FALSE
        self.created = datetime.datetime.utcnow()

    @property
    def serialize(self):
        return {
            'id': self.user_follower_id,
            'follower': self.follower_user.serialize,
            'following': self.following_user.serialize,
            'blocked': self.is_blocked,
            'created': str(self.created)
        }
