import datetime
from mgn import db
from mgn.models.posts_model import PostsModel
from mgn.models.blogs_model import BlogsModel
from mgn.models.master_user_model import MasterUserModel
from mgn.models.comment_threads_model import CommentThreadsModel
from mgn.models.like_threads_model import LikeThreadsModel


class SharesModel(db.Model):
    __tablename__ = 'shares'
    __table_args__ = {"schema": "mgn"}
    share_id = db.Column(db.Integer, primary_key=True, nullable=False)
    master_user_id = db.Column(db.Integer, db.ForeignKey(MasterUserModel.master_user_id), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey(PostsModel.user_post_id), nullable=True)
    blog_id = db.Column(db.Integer, db.ForeignKey(BlogsModel.user_blog_id), nullable=True)
    url = db.Column(db.String(200), nullable=True)
    comment_thread_id = db.Column(db.Integer, db.ForeignKey(CommentThreadsModel.comment_thread_id), nullable=False)
    like_thread_id = db.Column(db.Integer, db.ForeignKey(LikeThreadsModel.like_thread_id), nullable=False)
    like_count = db.Column(db.SmallInteger, nullable=True)
    comment_count = db.Column(db.SmallInteger, nullable=True)
    share_count = db.Column(db.SmallInteger, nullable=True)
    created = db.Column(db.DateTime, nullable=False)

    shared_master_user = db.relationship('MasterUserModel', backref=db.backref('share_master_user', lazy='dynamic'))
    shared_post = db.relationship('PostsModel', backref=db.backref('shared_post', lazy='dynamic'))
    shared_blog = db.relationship('BlogsModel', backref=db.backref('shared_blog', lazy='dynamic'))

    @property
    def id(self):
        return self.share_id

    def __init__(self, master_user_id=None, post_id=None, blog_id=None, url=None, comment_thread_id=None,
                 like_thread_id=None):
        self.master_user_id = master_user_id
        self.post_id = post_id
        self.blog_id = blog_id
        self.url = url
        self.comment_thread_id = comment_thread_id
        self.like_thread_id = like_thread_id
        self.like_count = 0
        self.comment_count = 0
        self.share_count = 0
        self.created = datetime.datetime.utcnow()

    @property
    def serialize(self):
        if self.shared_post is not None:
            return {
                'share_id': self.share_id,
                'share_type': 'post',
                'user': self.shared_master_user.serialize,
                'shared_post': self.shared_post.serialize,
                'comment_thread_id': self.comment_thread_id,
                'like_thread_id': self.like_thread_id,
                'like_count': self.like_count,
                'comment_count': self.comment_count,
                'share_count': self.share_count,
                'created': str(self.created)
            }
        elif self.shared_blog is not None:
            return {
                'share_id': self.share_id,
                'share_type': 'blog',
                'user': self.shared_master_user.serialize,
                'shared_blog': self.shared_blog.serialize,
                'comment_thread_id': self.comment_thread_id,
                'like_thread_id': self.like_thread_id,
                'like_count': self.like_count,
                'comment_count': self.comment_count,
                'share_count': self.share_count,
                'created': str(self.created)
            }
        elif self.url is not None:
            return {
                'share_id': self.share_id,
                'share_type': 'url',
                'user': self.shared_master_user.serialize,
                'shared_url': self.url,
                'comment_thread_id': self.comment_thread_id,
                'like_thread_id': self.like_thread_id,
                'like_count': self.like_count,
                'comment_count': self.comment_count,
                'share_count': self.share_count,
                'created': str(self.created)
            }
