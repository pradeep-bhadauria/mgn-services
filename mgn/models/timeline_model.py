import datetime
from mgn import db
from mgn.models.posts_model import PostsModel
from mgn.models.blogs_model import BlogsModel
from mgn.models.shares_model import SharesModel
from mgn.models.master_user_model import MasterUserModel
from mgn.models.comments_model import CommentsModel
from mgn.models.likes_model import LikesModel
from mgn.models.timeline_activity_type_model import TimelineActivityTypeModel


class TimelineModel(db.Model):
    __tablename__ = 'timeline'
    __table_args__ = {"schema": "mgn"}
    timeline_id = db.Column(db.Integer, primary_key=True, nullable=False)
    master_user_id = db.Column(db.Integer, db.ForeignKey(MasterUserModel.master_user_id), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey(PostsModel.user_post_id), nullable=True)
    blog_id = db.Column(db.Integer, db.ForeignKey(BlogsModel.user_blog_id), nullable=True)
    share_id = db.Column(db.Integer, db.ForeignKey(SharesModel.share_id), nullable=True)
    comment_id = db.Column(db.Integer, db.ForeignKey(CommentsModel.comment_id), nullable=False)
    like_id = db.Column(db.Integer, db.ForeignKey(LikesModel.like_id), nullable=False)
    timeline_activity_type_id = db.Column(db.Integer,
                                          db.ForeignKey(TimelineActivityTypeModel.timeline_activity_type_id),
                                          nullable=False)
    created = db.Column(db.DateTime, nullable=False)

    timeline_user = db.relationship('MasterUserModel', backref=db.backref('timeline_user', lazy='dynamic'))
    timeline_post = db.relationship('PostsModel', backref=db.backref('timeline_post', lazy='dynamic'))
    timeline_blog = db.relationship('BlogsModel', backref=db.backref('timeline_blog', lazy='dynamic'))
    timeline_comment = db.relationship('CommentsModel', backref=db.backref('timeline_comment', lazy='dynamic'))
    timeline_like = db.relationship('LikesModel', backref=db.backref('timeline_like', lazy='dynamic'))
    timeline_share = db.relationship('SharesModel', backref=db.backref('timeline_share', lazy='dynamic'))
    timeline_activity = db.relationship('TimelineActivityTypeModel',
                                        backref=db.backref('timeline_activity', lazy='dynamic'))

    @property
    def id(self):
        return self.timeline_id

    def __init__(self, master_user_id=None, post_id=None, blog_id=None, share_id=None, comment_id=None,
                 like_id=None, timeline_activity_type_id=None):
        self.master_user_id = master_user_id
        self.post_id = post_id
        self.blog_id = blog_id
        self.share_id = share_id
        self.comment_id = comment_id
        self.timeline_activity_type_id = timeline_activity_type_id
        self.like_id = like_id
        self.created = datetime.datetime.utcnow()

    @property
    def serialize(self):
        if self.timelined_post is not None:
            return {
                'timeline_id': self.timeline_id,
                'timelinetimeline_activity_type_id': self.timeline_activity_type_id,
                'user': self.timelined_master_user.serialize,
                'timelined_post': self.timelined_post.serialize,
                'created': str(self.created)
            }
        elif self.timelined_blog is not None:
            return {
                'timeline_id': self.timeline_id,
                'timelinetimeline_activity_type_id': self.timeline_activity_type_id,
                'user': self.timelined_master_user.serialize,
                'timelined_blog': self.timelined_blog.serialize,
                'created': str(self.created)
            }
        elif self.timeline_share is not None:
            return {
                'timeline_id': self.timeline_id,
                'timelinetimeline_activity_type_id': self.timeline_activity_type_id,
                'user': self.timelined_master_user.serialize,
                'timeline_share': self.timeline_share.serialize,
                'created': str(self.created)
            }
        elif self.timeline_comment is not None:
            return {
                'timeline_id': self.timeline_id,
                'timelinetimeline_activity_type_id': self.timeline_activity_type_id,
                'user': self.timelined_master_user.serialize,
                'timeline_comment': self.timeline_comment.serialize,
                'created': str(self.created)
            }
        elif self.timeline_like is not None:
            return {
                'timeline_id': self.timeline_id,
                'timelinetimeline_activity_type_id': self.timeline_activity_type_id,
                'user': self.timelined_master_user.serialize,
                'timeline_like': self.timeline_like.serialize,
                'created': str(self.created)
            }
