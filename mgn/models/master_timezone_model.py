import datetime
from mgn import db


class MasterTimezoneModel(db.Model):
    __tablename__ = 'master_timezone'
    __table_args__ = {"schema": "mgn"}
    timezone_id = db.Column(db.Integer, primary_key=True)
    timezone_code = db.Column(db.String(10), unique=True, nullable=False)
    timezone_description = db.Column(db.String(50), nullable=False)
    timezone_offset = db.Column(db.String(10), nullable=False)
    timezone_offset_dst = db.Column(db.String(10), nullable=False)
    is_active = db.Column(db.SmallInteger, nullable=False)
    created = db.Column(db.DateTime, nullable=True)

    @property
    def id(self):
        return self.timezone_id

    def __init__(self, timezone_code=None, timezone_description=None, timezone_offset=None, timezone_offset_dst=None,
                 is_active=None):
        self.timezone_code = timezone_code
        self.timezone_description = timezone_description
        self.timezone_offset = timezone_offset
        self.timezone_offset_dst = timezone_offset_dst
        self.is_active = is_active
        self.created = datetime.datetime.utcnow()

    @property
    def serialize(self):
        return {
            'timezone_id': self.timezone_id,
            'timezone_code': self.timezone_code,
            'timezone_description': self.timezone_description,
            'timezone_offset': self.timezone_offset,
            'timezone_offset_dst': self.timezone_offset_dst,
            'is_active': self.is_active,
            'created': str(self.created)
        }
