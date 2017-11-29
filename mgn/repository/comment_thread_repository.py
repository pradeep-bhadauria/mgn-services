from mgn import db
from mgn.models.comment_threads_model import CommentThreadsModel


class CommentThreadsRepository:
    comment_threads_id = None

    def __init__(self, comment_threads_id=None):
        self.comment_threads_id = comment_threads_id

    @staticmethod
    def add():
        try:
            data = CommentThreadsModel()
            db.session.add(data)
            db.session.flush()
            comment_thread_id = data.comment_thread_id
            db.session.commit()
            return comment_thread_id
        except:
            db.session.rollback()
            raise

    def get(self):
        comment_threads_details = CommentThreadsModel.query.filter_by(
                comment_threads_id=self.comment_threads_id).first()
        return comment_threads_details
