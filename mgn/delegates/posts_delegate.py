from flask import json
from mgn.repository.posts_repository import PostsRepository
from mgn.utils.helper import Helper


class PostsDelegate:
    posts = None

    def __init__(self, post_id=None):
        self.posts = PostsRepository(post_id)

    def add(self, master_user_id=None, post_text=None, has_attachment=None, attachment_url=None):
        result = self.posts.add(master_user_id, post_text, has_attachment, attachment_url)
        return result

    def update_comment_count(self, count=None):
        result = self.posts.update_comment_count(count)
        return result

    def update_like_count(self, count=None):
        result = self.posts.update_like_count(count)
        return result

    def update_share_count(self, count=None):
        result = self.posts.update_share_count(count)
        return result

    def update_post_text(self, post_text=None):
        result = self.posts.update_post_text(post_text)
        return result

    def get(self):
        result = self.posts.get()
        if result is not None:
            return json.dumps(result.serialize)
        return result

    def get_my_posts(self, master_user_id=None,offset=0):
        result = self.posts.get_my_posts(master_user_id,offset)
        if result is not None:
            return Helper.json_list(result)
        return result

    def get_posts(self, offset=0):
        result = self.posts.get_posts(offset)
        if result is not None:
            return Helper.json_list(result)
        return result

    def delete(self):
        result = self.posts.delete()
        return result
