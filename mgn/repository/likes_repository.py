from mgn import db
from mgn.models.likes_model import LikesModel
from mgn.utils.config import PAGINATION_LIMIT


class LikesRepository:
    like_id = None

    def __init__(self, like_id=None):
        self.like_id = like_id

    @staticmethod
    def add(master_user_id=None, like_thread_id=None, post_id=None, blog_id=None, share_id=None):
        try:
            data = LikesModel(
                    like_thread_id=like_thread_id,
                    master_user_id=master_user_id,
                    post_id=post_id,
                    blog_id=blog_id,
                    share_id=share_id,
            )
            db.session.add(data)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    @staticmethod
    def get_likes(like_threads_id=None, offset=0):
        likes_details = LikesModel.query.filter_by(
                like_threads_id=like_threads_id).order_by('created desc').offset(offset).limit(
                PAGINATION_LIMIT)
        return likes_details

    @staticmethod
    def get_my_likes(master_user_id=None, offset=0):
        likes_details = LikesModel.query.filter_by(
                master_user_id=master_user_id).order_by('created desc').offset(offset).limit(
                PAGINATION_LIMIT)
        return likes_details

    def unlike(self):
        try:
            LikesModel.query.filter_by(like_id=self.like_id).delete()
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise
