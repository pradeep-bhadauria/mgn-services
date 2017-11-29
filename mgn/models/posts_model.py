import datetime
from mgn import db
from mgn.models.master_user_model import MasterUserModel
from mgn.models.comment_threads_model import CommentThreadsModel
from mgn.models.like_threads_model import LikeThreadsModel


class PostsModel(db.Model):
    __tablename__ = 'user_posts'
    __table_args__ = {"schema": "mgn"}
    user_post_id = db.Column(db.Integer, primary_key=True, nullable=False)
    post_text = db.Column(db.String(200), nullable=False)
    has_attachment = db.Column(db.SmallInteger, nullable=False)
    attachment_url = db.Column(db.String(200), nullable=False)
    comment_thread_id = db.Column(db.Integer, db.ForeignKey(CommentThreadsModel.comment_thread_id), nullable=False)
    like_thread_id = db.Column(db.Integer, db.ForeignKey(LikeThreadsModel.like_thread_id), nullable=False)
    created_by_master_user_id = db.Column(db.Integer, db.ForeignKey(MasterUserModel.master_user_id), nullable=False)
    like_count = db.Column(db.SmallInteger, nullable=True)
    comment_count = db.Column(db.SmallInteger, nullable=True)
    share_count = db.Column(db.SmallInteger, nullable=True)
    created = db.Column(db.DateTime, nullable=False)

    post_master_user = db.relationship('MasterUserModel', backref=db.backref('post_master_user', lazy='dynamic'))

    @property
    def id(self):
        return self.post_id

    def __init__(self, created_by_master_user_id=None, post_text=None, has_attachment=None, attachment_url=None,
                 comment_thread_id=None, like_thread_id=None):
        self.created_by_master_user_id = created_by_master_user_id
        self.post_text = post_text
        self.has_attachment = has_attachment
        self.attachment_url = attachment_url
        self.comment_thread_id = comment_thread_id
        self.like_thread_id = like_thread_id
        self.like_count = 0
        self.comment_count = 0
        self.share_count = 0
        self.created = datetime.datetime.utcnow()

    @property
    def serialize(self):
        return {
            'post_id': self.user_post_id,
            'user': self.post_master_user.serialize,
            'post': self.post_text,
            'attachment_url': self.attachment_url,
            'comment_thread_id': self.comment_thread_id,
            'like_thread_id': self.like_thread_id,
            'like_count': self.like_count,
            'comment_count': self.comment_count,
            'share_count': self.share_count,
            'created': str(self.created)
        }

