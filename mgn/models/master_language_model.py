import datetime
from mgn import db


class MasterLanguageModel(db.Model):
    __tablename__ = 'master_language'
    __table_args__ = {"schema": "mgn"}
    master_language_id = db.Column(db.Integer, primary_key=True)
    language_name = db.Column(db.String(50), nullable=False)
    language_description = db.Column(db.String(100), nullable=False)
    is_active = db.Column(db.SmallInteger, nullable=False)
    created = db.Column(db.DateTime, nullable=True)

    @property
    def id(self):
        return self.master_language_id

    def __init__(self, language_name=None, language_description=None, is_active=None):
        self.language_name = language_name
        self.language_description = language_description
        self.is_active = is_active
        self.created = datetime.datetime.utcnow()

    @property
    def serialize(self):
        return {
            'language_id': self.master_language_id,
            'language_name': self.language_name,
            'language_description': self.language_description,
            'is_active': self.is_active,
            'created': str(self.created)
        }
