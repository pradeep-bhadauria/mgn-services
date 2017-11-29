from mgn import db
from mgn.models.like_threads_model import LikeThreadsModel


class LikeThreadsRepository:
    like_threads_id = None

    def __init__(self, like_threads_id=None):
        self.like_threads_id = like_threads_id

    @staticmethod
    def add():
        try:
            data = LikeThreadsModel()
            db.session.add(data)
            db.session.flush()
            like_thread_id = data.like_thread_id
            db.session.commit()
            return like_thread_id
        except:
            db.session.rollback()
            raise

    def get(self):
        like_threads_details = LikeThreadsModel.query.filter_by(
                like_threads_id=self.like_threads_id).first()
        return like_threads_details
