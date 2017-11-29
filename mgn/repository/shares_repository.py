from mgn import db
from mgn.models.shares_model import SharesModel
from mgn.repository.comment_thread_repository import CommentThreadsRepository
from mgn.repository.like_threads_repository import LikeThreadsRepository
from mgn.utils.config import PAGINATION_LIMIT


class SharesRepository:
    share_id = None

    def __init__(self, share_id=None):
        self.share_id = share_id

    @staticmethod
    def add(master_user_id=None, post_id=None, blog_id=None, url=None):
        try:
            likes = LikeThreadsRepository()
            like_thread_id = likes.add()
            comment_thread = CommentThreadsRepository()
            comment_thread_id = comment_thread.add()
            data = SharesModel(
                    master_user_id=master_user_id,
                    post_id=post_id,
                    blog_id=blog_id,
                    url=url,
                    comment_thread_id=comment_thread_id,
                    like_thread_id=like_thread_id,
            )
            db.session.add(data)
            db.session.flush()
            share_id = data.share_id
            db.session.commit()
            return share_id
        except:
            db.session.rollback()
            raise

    def get(self):
        share_details = SharesModel.query.filter_by(
                share_id=self.share_id).first()
        return share_details

    @staticmethod
    def get_shares(offset=0):
        shares_details = SharesModel.query.order_by('created desc').offset(offset).limit(PAGINATION_LIMIT)
        return shares_details

    @staticmethod
    def get_my_shares(master_user_id=None, offset=0):
        shares_details = SharesModel.query.filter_by(
                master_user_id=master_user_id
        ).order_by('created desc').offset(offset).limit(PAGINATION_LIMIT)
        return shares_details

    def update_like_count(self, count=None):
        try:
            if count == 1:
                SharesModel.query.filter_by(
                        share_id=self.share_id
                ).update(dict(
                        like_count=SharesModel.like_count + 1
                ))
            else:
                SharesModel.query.filter_by(
                        share_id=self.share_id
                ).update(dict(
                        like_count=SharesModel.like_count - 1
                ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_comment_count(self, count=None):
        try:
            if count == 1:
                SharesModel.query.filter_by(
                        share_id=self.share_id
                ).update(dict(
                        comment_count=SharesModel.comment_count + 1
                ))
            else:
                SharesModel.query.filter_by(
                        share_id=self.share_id
                ).update(dict(
                        comment_count=SharesModel.comment_count - 1
                ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_share_count(self, count=None):
        try:
            if count == 1:
                SharesModel.query.filter_by(
                        share_id=self.share_id
                ).update(dict(
                        share_count=SharesModel.share_count + 1
                ))
            else:
                SharesModel.query.filter_by(
                        share_id=self.share_id
                ).update(dict(
                        share_count=SharesModel.share_count - 1
                ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def delete(self):
        try:
            SharesModel.query.filter_by(share_id=self.share_id).delete()
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise
