import datetime
from mgn import db
from mgn.models.comment_threads_model import CommentThreadsModel
from mgn.models.master_user_model import MasterUserModel


class CommentsModel(db.Model):
    __tablename__ = 'comments'
    __table_args__ = {"schema": "mgn"}
    comment_id = db.Column(db.Integer, primary_key=True, nullable=False)
    comment_thread_id = db.Column(db.Integer, db.ForeignKey(CommentThreadsModel.comment_thread_id), nullable=False)
    comment_reply_thread_id = db.Column(db.Integer, db.ForeignKey(CommentThreadsModel.comment_thread_id), nullable=True)
    master_user_id = db.Column(db.Integer, db.ForeignKey(MasterUserModel.master_user_id), nullable=False)
    comment = db.Column(db.String(200), nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    comment_master_user = db.relationship('MasterUserModel', backref=db.backref('comment_master_user', lazy='dynamic'))

    @property
    def id(self):
        return self.comment_id

    def __init__(self, master_user_id=None, comment_thread_id=None, comment_reply_thread_id=None, comment=None):
        self.master_user_id = master_user_id
        self.comment_thread_id = comment_thread_id
        self.comment_reply_thread_id = comment_reply_thread_id
        self.comment = comment
        self.created = datetime.datetime.utcnow()

    @property
    def serialize(self):
        return {
            'user': self.comment_master_user.serialize,
            'comment': self.comment,
            'reply_thread': self.comment_reply_thread_id,
            'created': str(self.created)
        }
