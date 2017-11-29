import datetime
from mgn import db


class MGNAuthTypeModel(db.Model):
    __tablename__ = 'auth_type'
    __table_args__ = {"schema": "mgn"}
    auth_type_id = db.Column(db.BigInteger, primary_key=True)
    auth_name = db.Column(db.String(45), unique=True, nullable=False)
    auth_desc = db.Column(db.String(100), nullable=False)
    created = db.Column(db.DateTime, nullable=False)

    def __init__(self, auth_name=None, auth_desc=None):
        self.auth_name = auth_name
        self.auth_desc = auth_desc
        self.created = datetime.datetime.utcnow()

    @property
    def id(self):
        return self.auth_type_id

    @property
    def serialize(self):
        return {
            'auth_type_id': self.auth_type_id,
            'auth_name': self.auth_name,
            'auth_desc': self.auth_desc,
            'created': str(self.created)
        }
