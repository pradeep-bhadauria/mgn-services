import datetime
from mgn import db
from mgn.models.master_user_model import MasterUserModel
from sqlalchemy.dialects.postgresql import JSONB


class UserAccessDetailsModel(db.Model):
    __tablename__ = 'user_access_details'
    __table_args__ = {"schema": "mgn"}
    user_access_details_id = db.Column(db.Integer, primary_key=True)
    master_user_id = db.Column(db.Integer, db.ForeignKey(MasterUserModel.master_user_id), nullable=False)
    access_history = db.Column(JSONB, nullable=True)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    city = db.Column(db.String(50), nullable=True)
    state = db.Column(db.String(50), nullable=True)
    zipcode = db.Column(db.String(15), nullable=True)
    country_code = db.Column(db.String(5), nullable=True)
    browser = db.Column(db.String(100), nullable=True)
    device = db.Column(db.String(100), nullable=True)
    request_string = db.Column(db.String(150), nullable=True)
    platform = db.Column(db.String(50), nullable=True)
    updated = db.Column(db.DateTime, nullable=False)

    master_user = db.relationship('MasterUserModel', backref=db.backref('access_user', lazy='dynamic'))

    @property
    def id(self):
        return self.user_profile_id

    def __init__(self, master_user_id=None, access_history=None, latitude=None, longitude=None,
                 city=None, state=None, zipcode=None, country_code=None, browser=None, device=None,request_string=None,
                 platform=None):
        self.master_user_id = master_user_id
        self.access_history = access_history
        self.latitude = latitude
        self.longitude = longitude
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.country_code = country_code
        self.browser = browser
        self.device = device
        self.request_string = request_string
        self.platform = platform
        self.updated = datetime.datetime.now()

    @property
    def serialize(self):
        return {
            'user': self.master_user.serialize,
            'access_history': self.access_history,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'city': self.city,
            'state': self.state,
            'zipcode': self.zipcode,
            'country_code': self.country_code,
            'browser': self.browser,
            'device': self.device,
            'request_string': self.request_string,
            'platform': self.platform,
            'updated': str(self.updated)
        }
