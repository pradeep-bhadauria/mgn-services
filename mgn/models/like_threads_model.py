import datetime
from mgn import db


class LikeThreadsModel(db.Model):
    __tablename__ = 'like_threads'
    __table_args__ = {"schema": "mgn"}
    like_thread_id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, nullable=True)

    @property
    def id(self):
        return self.like_thread_id

    def __init__(self):
        self.created = datetime.datetime.utcnow()

    @property
    def serialize(self):
        return {
            'like_thread_id': self.like_thread_id,
            'created': str(self.created)
        }
