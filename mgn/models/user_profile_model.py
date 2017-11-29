import datetime
from mgn import db
from mgn.models.master_gender_model import MasterGenderModel
from mgn.models.master_user_model import MasterUserModel
from sqlalchemy.dialects.postgresql import JSONB


class UserProfileModel(db.Model):
    __tablename__ = 'user_profile'
    __table_args__ = {"schema": "mgn"}
    user_profile_id = db.Column(db.Integer, primary_key=True)
    profile_banner_image = db.Column(db.String(200), nullable=True)
    dob = db.Column(db.Date, nullable=True)
    master_gender_id = db.Column(db.SmallInteger, db.ForeignKey(MasterGenderModel.master_gender_id), nullable=False)
    master_user_id = db.Column(db.Integer, db.ForeignKey(MasterUserModel.master_user_id), nullable=False)

    master_gender = db.relationship('MasterGenderModel', backref=db.backref('master_gender', lazy='dynamic'))
    master_user = db.relationship('MasterUserModel', backref=db.backref('master_user', lazy='dynamic'))

    @property
    def id(self):
        return self.user_profile_id

    def __init__(self, profile_pic=None, profile_banner_image=None, dob=None, master_gender_id=None,
                 master_user_id=None):
        self.profile_banner_image = profile_banner_image
        self.dob = dob
        self.master_gender_id = master_gender_id
        self.master_user_id = master_user_id

    @property
    def serialize(self):
        return {
            'profile_banner_image': self.profile_banner_image,
            'dob': str(self.dob),
            'gender': self.master_gender.serialize,
            'user': self.master_user.serialize
        }
