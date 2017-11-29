import datetime
from flask import url_for
from mgn import db
from mgn.models.master_user_model import MasterUserModel
from mgn.models.comment_threads_model import CommentThreadsModel
from mgn.models.like_threads_model import LikeThreadsModel
from sqlalchemy.dialects.postgresql import JSONB


class BlogsModel(db.Model):
    __tablename__ = 'user_blogs'
    __table_args__ = {"schema": "mgn"}
    user_blog_id = db.Column(db.Integer, primary_key=True, nullable=False)
    blogger_master_user_id = db.Column(db.Integer, db.ForeignKey(MasterUserModel.master_user_id), nullable=False)
    blog_name = db.Column(db.String(200), nullable=False)
    blog_subject = db.Column(db.String(100), nullable=False)
    blog_body = db.Column(db.String, nullable=False)
    comment_thread_id = db.Column(db.Integer, db.ForeignKey(CommentThreadsModel.comment_thread_id), nullable=False)
    like_thread_id = db.Column(db.Integer, db.ForeignKey(LikeThreadsModel.like_thread_id), nullable=False)
    visit_count = db.Column(db.SmallInteger, nullable=False)
    like_count = db.Column(db.SmallInteger, nullable=False)
    comment_count = db.Column(db.SmallInteger, nullable=False)
    share_count = db.Column(db.SmallInteger, nullable=False)
    tags = db.Column(JSONB, nullable=False)
    updated = db.Column(db.DateTime, nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    blog_master_user = db.relationship('MasterUserModel', backref=db.backref('blog_master_user', lazy='dynamic'))

    @property
    def id(self):
        return self.blog_id

    def __init__(self, master_user_id=None, blog_name=None, blog_subject=None, blog_body=None, comment_thread_id=None,
                 like_thread_id=None, tags=None):
        self.blogger_master_user_id = master_user_id
        self.blog_name = blog_name
        self.blog_subject = blog_subject
        self.blog_body = blog_body
        self.comment_thread_id = comment_thread_id
        self.like_thread_id = like_thread_id
        self.tags = tags
        self.visit_count = 0
        self.like_count = 0
        self.comment_count = 0
        self.share_count = 0
        self.updated = datetime.datetime.utcnow()
        self.created = datetime.datetime.utcnow()

    @property
    def serialize(self):
        return {
            'user': self.blog_master_user.serialize,
            'url': url_for("blogs_services.get", blog_name=self.blog_name),
            'blog_id': self.user_blog_id,
            'blog_subject': self.blog_subject,
            'blog_body': self.blog_body,
            'comment_thread_id': self.comment_thread_id,
            'like_thread_id': self.like_thread_id,
            'tags': self.tags,
            'visit_count': self.visit_count,
            'like_count': self.like_count,
            'comment_count': self.comment_count,
            'share_count': self.share_count,
            'updated': str(self.updated),
            'created': str(self.created)
        }
