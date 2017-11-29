import datetime
from mgn import db
from mgn.models.like_threads_model import LikeThreadsModel
from mgn.models.posts_model import PostsModel
from mgn.models.blogs_model import BlogsModel
from mgn.models.shares_model import SharesModel
from mgn.models.master_user_model import MasterUserModel


class LikesModel(db.Model):
    __tablename__ = 'likes'
    __table_args__ = {"schema": "mgn"}
    like_id = db.Column(db.Integer, primary_key=True, nullable=False)
    master_user_id = db.Column(db.Integer, db.ForeignKey(MasterUserModel.master_user_id), nullable=False)
    like_thread_id = db.Column(db.Integer, db.ForeignKey(LikeThreadsModel.like_thread_id), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey(PostsModel.user_post_id), nullable=True)
    blog_id = db.Column(db.Integer, db.ForeignKey(BlogsModel.user_blog_id), nullable=True)
    share_id = db.Column(db.Integer, db.ForeignKey(SharesModel.share_id), nullable=True)
    created = db.Column(db.DateTime, nullable=False)

    liked_master_user = db.relationship('MasterUserModel', backref=db.backref('liked_master_user', lazy='dynamic'))
    liked_thread = db.relationship('LikeThreadsModel', backref=db.backref('liked_thread', lazy='dynamic'))
    liked_post = db.relationship('PostsModel', backref=db.backref('liked_post', lazy='dynamic'))
    liked_blog = db.relationship('BlogsModel', backref=db.backref('liked_blog', lazy='dynamic'))
    liked_share = db.relationship('SharesModel', backref=db.backref('liked_share', lazy='dynamic'))


    @property
    def id(self):
        return self.like_id

    def __init__(self,master_user_id=None, like_thread_id=None, post_id=None, blog_id=None, share_id=None):
        self.master_user_id = master_user_id
        self.like_thread_id = like_thread_id
        self.post_id = post_id
        self.blog_id = blog_id
        self.share_id = share_id
        self.created = datetime.datetime.utcnow()

    @property
    def serialize(self):
        return {
            'like_id': self.like_id,
            'liked_master_user': self.liked_master_user.serialize,
            'liked_thread': self.liked_thread.serialize,
            'liked_post': self.liked_post.serialize,
            'liked_blog': self.liked_blog.serialize,
            'liked_share': self.liked_share.serialize,
            'created': str(self.created)
        }
