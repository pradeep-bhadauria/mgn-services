import datetime
from mgn import db


class CommentThreadsModel(db.Model):
    __tablename__ = 'comment_threads'
    __table_args__ = {"schema": "mgn"}
    comment_thread_id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, nullable=True)

    @property
    def id(self):
        return self.comment_thread_id

    def __init__(self):
        self.created = datetime.datetime.utcnow()

    @property
    def serialize(self):
        return {
            'comment_thread_id': self.comment_thread_id,
            'created': str(self.created)
        }
