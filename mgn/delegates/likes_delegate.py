from mgn.repository.likes_repository import LikesRepository
from mgn.utils.helper import Helper


class LikesDelegate:
    likes = None

    def __init__(self, like_id=None):
        self.likes = LikesRepository(like_id)

    def add(self, master_user_id=None, like_thread_id=None, post_id=None, blog_id=None, share_id=None):
        result = self.likes.add(master_user_id, like_thread_id, post_id, blog_id, share_id)
        return result

    def get_my_likes(self, master_user_id=None, offset=0):
        result = self.likes.get_my_likes(master_user_id, offset)
        if result is not None:
            return Helper.json_list(result)
        return result

    def get_likes(self, likes_thread_id=None, offset=0):
        result = self.likes.get_likes(likes_thread_id, offset)
        if result is not None:
            return Helper.json_list(result)
        return result

    def unlike(self):
        result = self.likes.unlike()
        return result
