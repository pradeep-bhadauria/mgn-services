import datetime
from mgn import db


class TimelineActivityTypeModel(db.Model):
    __tablename__ = 'timeline_activity_types'
    __table_args__ = {"schema": "mgn"}
    timeline_activity_type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    created = db.Column(db.DateTime, nullable=False)

    @property
    def id(self):
        return self.timeline_activity_type_id

    def __init__(self, name=None, description=None):
        self.name = name,
        self.description = description,
        self.created = datetime.datetime.utcnow()

    @property
    def serialize(self):
        return {
            'timeline_activity_type_id': self.timeline_activity_type_id,
            'name': self.name,
            'description': self.description,
            'created': str(self.created)
        }
