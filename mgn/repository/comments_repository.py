from mgn import db
from mgn.models.comments_model import CommentsModel
from mgn.utils.config import PAGINATION_LIMIT


class CommentsRepository:
    comment_id = None

    def __init__(self, comment_id=None):
        self.comment_id = comment_id

    @staticmethod
    def add(master_user_id=None, comment_thread_id=None, comment_reply_thread_id=None, comment=None):
        try:
            data = CommentsModel(
                    comment_thread_id=comment_thread_id,
                    comment_reply_thread_id=comment_reply_thread_id,
                    master_user_id=master_user_id,
                    comment=comment
            )
            db.session.add(data)
            db.session.flush()
            comment_id = data.comment_id
            db.session.commit()
            return comment_id
        except:
            db.session.rollback()
            raise

    def get(self):
        comment_details = CommentsModel.query.filter_by(
                comment_id=self.comment_id).first()
        return comment_details

    @staticmethod
    def get_comments(comment_threads_id=None, offset=0):
        comments_details = CommentsModel.query.filter_by(
                comment_threads_id=comment_threads_id).order_by('created desc').offset(offset).limit(
                PAGINATION_LIMIT)
        return comments_details

    @staticmethod
    def get_my_comments(master_user_id=None, offset=0):
        comments_details = CommentsModel.query.filter_by(
                master_user_id=master_user_id).order_by('created desc').offset(offset).limit(
                PAGINATION_LIMIT)
        return comments_details

    def update(self, comment=None):
        try:
            CommentsModel.query.filter_by(comment_id=self.comment_id).update(dict(
                    comment=comment
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def delete(self):
        try:
            CommentsModel.query.filter_by(comment_id=self.comment_id).delete()
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise
