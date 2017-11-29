from mgn.repository.comments_repository import CommentsRepository
from mgn.utils.helper import Helper


class CommentsDelegate:
    comments = None

    def __init__(self, comment_id=None):
        self.comments = CommentsRepository(comment_id)

    def add(self, master_user_id=None, comment_thread_id=None, comment_reply_thread_id=None, comment=None):
        result = self.comments.add(master_user_id, comment_thread_id, comment_reply_thread_id, comment)
        return result

    def update(self, comment=None):
        result = self.comments.update(comment)
        return result

    def get(self):
        result = self.comments.get()
        if result is not None:
            return Helper.json_list(result)
        return result

    def get_comments(self, comments_thread_id=None, offset=0):
        result = self.comments.get_comments(comments_thread_id, offset)
        if result is not None:
            return Helper.json_list(result)
        return result

    def get_my_comments(self, master_user_id=None, offset=0):
        result = self.comments.get_my_comments(master_user_id, offset)
        if result is not None:
            return Helper.json_list(result)
        return result

    def delete(self):
        result = self.comments.delete()
        return result
