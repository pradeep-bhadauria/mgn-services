import datetime
from mgn import db


class MGNUserTypeModel(db.Model):
    __tablename__ = 'mgn_user_type'
    __table_args__ = {"schema": "mgn"}
    mgn_user_type_id = db.Column(db.BigInteger, primary_key=True)
    user_type = db.Column(db.String(10), unique=True, nullable=False)
    user_type_desc = db.Column(db.String(30), nullable=False)
    created = db.Column(db.DateTime, nullable=False)

    def __init__(self, user_type=None, user_type_desc=None):
        self.user_type = user_type
        self.user_type_desc = user_type_desc
        self.created = datetime.datetime.utcnow()

    @property
    def id(self):
        return self.mgn_user_type_id

    @property
    def serialize(self):
        return {
            'user_type_id': self.mgn_user_type_id,
            'user_type': self.user_type,
            'user_type_desc': self.user_type_desc,
            'created': str(self.created)
        }
