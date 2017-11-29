from flask import json
from mgn.repository.blogs_repository import BlogsRepository
from mgn.utils.helper import Helper


class BlogsDelegate:
    blogs = None

    def __init__(self, blog_id=None):
        self.blogs = BlogsRepository(blog_id)

    def add(self, master_user_id=None, blog_subject=None, blog_body=None, tags=None):
        result = self.blogs.add(master_user_id, blog_subject, blog_body, tags)
        return result

    def update_comment_count(self, count=None):
        result = self.blogs.update_comment_count(count)
        return result

    def update_visit_count(self):
        result = self.blogs.update_visit_count()
        return result

    def update_like_count(self, count=None):
        result = self.blogs.update_like_count(count)
        return result

    def update_share_count(self, count=None):
        result = self.blogs.update_share_count(count)
        return result

    def update_blog_name(self, blog_name=None):
        result = self.blogs.update_blog_name(blog_name)
        return result

    def update_blog_subject(self, blog_subject=None):
        result = self.blogs.update_blog_subject(blog_subject)
        return result

    def update_blog_body(self, blog_body=None):
        result = self.blogs.update_blog_body(blog_body)
        return result

    def update_blog_tags(self, tags=None):
        result = self.blogs.update_blog_tags(tags)
        return result

    def get(self, blog_name=None):
        result = self.blogs.get(blog_name)
        if result is not None:
            return json.dumps(result.serialize)
        return result

    def get_my_blogs(self, master_user_id=None, offset=0):
        result = self.blogs.get_my_blogs(master_user_id, offset)
        if result is not None:
            return Helper.json_list(result)
        return result

    def get_blogs(self, offset=0):
        result = self.blogs.get_blogs(offset)
        if result is not None:
            return Helper.json_list(result)
        return result

    def delete(self):
        result = self.blogs.delete()
        return result
