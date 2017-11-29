from mgn import db
from mgn.models.posts_model import PostsModel
from mgn.repository.comment_thread_repository import CommentThreadsRepository
from mgn.repository.like_threads_repository import LikeThreadsRepository
from mgn.utils.config import PAGINATION_LIMIT


class PostsRepository:
    user_post_id = None

    def __init__(self, user_post_id=None):
        self.user_post_id = user_post_id

    @staticmethod
    def add(master_user_id=None, post_text=None, has_attachment=None, attachment_url=None):
        try:
            likes = LikeThreadsRepository()
            like_thread_id = likes.add()
            comment_thread = CommentThreadsRepository()
            comment_thread_id = comment_thread.add()
            data = PostsModel(
                    post_text=post_text,
                    has_attachment=has_attachment,
                    attachment_url=attachment_url,
                    comment_thread_id=comment_thread_id,
                    like_thread_id=like_thread_id,
                    created_by_master_user_id=master_user_id
            )
            db.session.add(data)
            db.session.flush()
            user_post_id = data.user_post_id
            db.session.commit()
            return user_post_id
        except:
            db.session.rollback()
            raise

    def get(self):
        post_details = PostsModel.query.filter_by(
                user_post_id=self.user_post_id).first()
        return post_details

    @staticmethod
    def get_posts(offset=0):
        posts_details = PostsModel.query.order_by('created desc').offset(offset).limit(PAGINATION_LIMIT)
        return posts_details

    @staticmethod
    def get_my_posts(master_user_id=None, offset=0):
        posts_details = PostsModel.query.filter_by(
                created_by_master_user_id=master_user_id
        ).order_by('created desc').offset(offset).limit(PAGINATION_LIMIT)
        return posts_details

    def update_post_text(self, post_text=None):
        try:
            PostsModel.query.filter_by(user_post_id=self.user_post_id).update(dict(
                    post_text=post_text
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_like_count(self, count=None):
        try:
            if count == 1:
                PostsModel.query.filter_by(
                        user_post_id=self.user_post_id
                ).update(dict(
                        like_count=PostsModel.like_count + 1
                ))
            else:
                PostsModel.query.filter_by(
                        user_post_id=self.user_post_id
                ).update(dict(
                        like_count=PostsModel.like_count - 1
                ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_comment_count(self, count=None):
        try:
            if count == 1:
                PostsModel.query.filter_by(
                        user_post_id=self.user_post_id
                ).update(dict(
                        comment_count=PostsModel.comment_count + 1
                ))
            else:
                PostsModel.query.filter_by(
                        user_post_id=self.user_post_id
                ).update(dict(
                        comment_count=PostsModel.comment_count - 1
                ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_share_count(self, count=None):
        try:
            if count == 1:
                PostsModel.query.filter_by(
                        user_post_id=self.user_post_id
                ).update(dict(
                        share_count=PostsModel.share_count + 1
                ))
            else:
                PostsModel.query.filter_by(
                    user_post_id=self.user_post_id
            ).update(dict(
                    share_count=PostsModel.share_count - 1
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def delete(self):
        try:
            PostsModel.query.filter_by(user_post_id=self.user_post_id).delete()
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise
