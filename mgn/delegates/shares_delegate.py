from flask import json
from mgn.repository.shares_repository import SharesRepository
from mgn.utils.helper import Helper


class SharesDelegate:
    shares = None

    def __init__(self, share_id=None):
        self.shares = SharesRepository(share_id)

    def add(self, master_user_id=None, post_id=None, blog_id=None, url=None):
        result = self.shares.add(master_user_id, post_id, blog_id, url)
        return result

    def update_comment_count(self, count=None):
        result = self.shares.update_comment_count(count)
        return result

    def update_like_count(self, count=None):
        result = self.shares.update_like_count(count)
        return result

    def update_share_count(self, count=None):
        result = self.shares.update_share_count(count)
        return result

    def get(self):
        result = self.shares.get()
        if result is not None:
            return json.dumps(result.serialize)
        return result

    def get_my_shares(self, master_user_id=None, offset=0):
        result = self.shares.get_my_shares(master_user_id, offset)
        if result is not None:
            return Helper.json_list(result)
        return result

    def get_shares(self, offset=0):
        result = self.shares.get_shares(offset)
        if result is not None:
            return Helper.json_list(result)
        return result

    def delete(self):
        result = self.shares.delete()
        return result
