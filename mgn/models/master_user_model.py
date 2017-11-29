import datetime
from mgn import db
from mgn.utils.constants import TRUE, FALSE

class MasterUserModel(db.Model):
    __tablename__ = 'master_user'
    __table_args__ = {"schema": "mgn"}
    master_user_id = db.Column(db.BigInteger, primary_key=True)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    profile_pic = db.Column(db.String(100), nullable=True)
    is_email_confirmed = db.Column(db.String(100))
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=True)
    is_active = db.Column(db.String(100), nullable=False)
    is_deleted = db.Column(db.String(100), nullable=False)
    is_blocked = db.Column(db.String(100), nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    updated = db.Column(db.DateTime, nullable=False)
    auth_type_id = db.Column(db.Integer, nullable=False)
    mgn_user_type_id = db.Column(db.Integer, nullable=False)
    social_id = db.Column(db.String(100), nullable=True)

    def __init__(self, first_name=None, last_name=None, email=None, password=None, username=None, auth_type_id=None,
                 mgn_user_type_id=None,profile_pic=None,social_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name
        self.email = email
        self.is_email_confirmed = FALSE
        self.username = username
        self.password = password
        self.is_active = FALSE
        self.is_deleted = FALSE
        self.is_blocked = FALSE
        self.updated = datetime.datetime.utcnow()
        self.created = datetime.datetime.utcnow()
        self.auth_type_id = auth_type_id
        self.mgn_user_type_id = mgn_user_type_id
        self.profile_pic = profile_pic
        self.social_id = social_id

    @property
    def id(self):
        return self.master_user_id

    @property
    def serialize(self):
        return {
            'id': self.master_user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'full_name': self.full_name,
            'email': self.email,
            'profile_pic': self.profile_pic,
            'social_id': self.social_id,
            'username': self.username,
            'created': str(self.created)
        }

