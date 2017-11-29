from mgn import db
from mgn.models.blogs_model import BlogsModel
from mgn.repository.comment_thread_repository import CommentThreadsRepository
from mgn.repository.like_threads_repository import LikeThreadsRepository
from mgn.utils.config import PAGINATION_LIMIT


class BlogsRepository:
    user_blog_id = None

    def __init__(self, user_blog_id=None):
        self.user_blog_id = user_blog_id

    @staticmethod
    def make_unique_blog_name(blog_name=None):
        if BlogsModel.query.filter_by(blog_name=blog_name).first() is None:
            return blog_name
        version = 2
        while True:
            new_name = blog_name + "_" + str(version)
            if BlogsModel.query.filter_by(blog_name=new_name).first() is None:
                break
            version += 1
        return new_name

    @staticmethod
    def add(master_user_id=None, blog_subject=None, blog_body=None, tags=None):
        try:
            likes = LikeThreadsRepository()
            like_thread_id = likes.add()
            comment_thread = CommentThreadsRepository()
            comment_thread_id = comment_thread.add()
            blog_name = BlogsRepository.make_unique_blog_name(blog_subject.replace(" ", "-")[:100])
            data = BlogsModel(
                    master_user_id=master_user_id,
                    blog_name=blog_name,
                    blog_subject=blog_subject,
                    blog_body=blog_body,
                    comment_thread_id=comment_thread_id,
                    like_thread_id=like_thread_id,
                    tags=tags
            )
            db.session.add(data)
            db.session.flush()
            user_blog_id = data.user_blog_id
            db.session.commit()
            return user_blog_id
        except:
            db.session.rollback()
            raise

    @staticmethod
    def get(blog_name=None):
        blog_details = BlogsModel.query.filter_by(
                blog_name=blog_name).first()
        return blog_details

    @staticmethod
    def get_blogs(offset=0):
        blogs_details = BlogsModel.query.order_by('created desc').offset(offset).limit(PAGINATION_LIMIT)
        return blogs_details

    @staticmethod
    def get_my_blogs(master_user_id=None, offset=0):
        blogs_details = BlogsModel.query.filter_by(
                created_by_master_user_id=master_user_id
        ).order_by('created desc').offset(offset).limit(PAGINATION_LIMIT)
        return blogs_details

    def update_blog_name(self, blog_name=None):
        try:
            blog_name = BlogsRepository.make_unique_blog_name(blog_name.replace(" ", "-")[:100])
            BlogsModel.query.filter_by(user_blog_id=self.user_blog_id).update(dict(
                    blog_name=blog_name
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_blog_subject(self, blog_subject=None):
        try:
            BlogsModel.query.filter_by(user_blog_id=self.user_blog_id).update(dict(
                    blog_subject=blog_subject
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_blog_body(self, blog_body=None):
        try:
            BlogsModel.query.filter_by(user_blog_id=self.user_blog_id).update(dict(
                    blog_body=blog_body
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_blog_tags(self, tags=None):
        try:
            BlogsModel.query.filter_by(user_blog_id=self.user_blog_id).update(dict(
                    tags=tags
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_like_count(self, count=None):
        try:
            if count == 1:
                BlogsModel.query.filter_by(
                        user_blog_id=self.user_blog_id
                ).update(dict(
                        like_count=BlogsModel.like_count + 1
                ))
            else:
                BlogsModel.query.filter_by(
                        user_blog_id=self.user_blog_id
                ).update(dict(
                        like_count=BlogsModel.like_count - 1
                ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_comment_count(self, count=None):
        try:
            if count == 1:
                BlogsModel.query.filter_by(
                        user_blog_id=self.user_blog_id
                ).update(dict(
                        comment_count=BlogsModel.comment_count + 1
                ))
            else:
                BlogsModel.query.filter_by(
                        user_blog_id=self.user_blog_id
                ).update(dict(
                        like_count=BlogsModel.like_count - 1
                ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_share_count(self, count=None):
        try:
            if count == 1:
                BlogsModel.query.filter_by(
                        user_blog_id=self.user_blog_id
                ).update(dict(
                        share_count=BlogsModel.share_count + 1
                ))
            else:
                BlogsModel.query.filter_by(
                        user_blog_id=self.user_blog_id
                ).update(dict(
                        like_count=BlogsModel.like_count - 1
                ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_visit_count(self):
        try:
            BlogsModel.query.filter_by(
                    user_blog_id=self.user_blog_id
            ).update(dict(
                    visit_count=BlogsModel.visit_count + 1
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def delete(self):
        try:
            BlogsModel.query.filter_by(user_blog_id=self.user_blog_id).delete()
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise
