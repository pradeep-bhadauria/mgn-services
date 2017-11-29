from mgn import db
from mgn.models.timeline_model import TimelineModel
from mgn.models.user_followers_model import UserFollowersModel
from mgn.utils.config import PAGINATION_LIMIT
from mgn.utils.constants import TIMELINE


class TimelineRepository:
    master_user_id = None

    def __init__(self, master_user_id=None):
        self.master_user_id = master_user_id

    def add(self, post_id=None, blog_id=None, share_id=None, comment_id=None,
            like_id=None, timeline_activity_type_id=None):
        try:
            data = TimelineModel(
                    master_user_id=self.master_user_id,
                    post_id=post_id,
                    blog_id=blog_id,
                    share_id=share_id,
                    comment_id=comment_id,
                    timeline_activity_type_id=timeline_activity_type_id,
                    like_id=like_id
            )
            db.session.add(data)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def get_timeline(self, offset=0):
        timeline_details = TimelineModel.query.filter_by(
                master_user_id=self.master_user_id).order_by('created desc').offset(offset).limit(PAGINATION_LIMIT)
        return timeline_details

    def get_feeds(self, offset=0):
        feeds = TimelineModel.query.join(UserFollowersModel,
                                         TimelineModel.master_user_id == UserFollowersModel.following).filter(
                UserFollowersModel.follower == self.master_user_id
        ).order_by('timeline.created desc').offset(offset).limit(PAGINATION_LIMIT)
        return feeds

    def delete(self, delete_id=None, delete_type=None):
        try:
            if delete_type == TIMELINE["blog"]:
                TimelineModel.query.filter_by(
                        master_user_id=self.master_user_id,
                        blog_id=delete_id).delete()
            elif delete_type == TIMELINE["comment"]:
                TimelineModel.query.filter_by(
                        master_user_id=self.master_user_id,
                        comment_id=delete_id).delete()
            elif delete_type == TIMELINE["like"]:
                TimelineModel.query.filter_by(
                        master_user_id=self.master_user_id,
                        like_id=delete_id).delete()
            elif delete_type == TIMELINE["share"]:
                TimelineModel.query.filter_by(
                        master_user_id=self.master_user_id,
                        share_id=delete_id).delete()
            elif delete_type == TIMELINE["post"]:
                TimelineModel.query.filter_by(
                        master_user_id=self.master_user_id,
                        post_id=delete_id).delete()
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise
