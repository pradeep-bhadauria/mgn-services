from flask import json
from mgn.repository.user_followers_repository import UserFollowersRepository
from mgn.utils.helper import Helper


class UserFollowersDelegate:
    user_followers = None

    def __init__(self, follower=None, following=None):
        self.user_followers = UserFollowersRepository(follower, following)

    def add(self):
        result = self.user_followers.add()
        return result

    def update_is_blocked(self, is_blocked=None):
        result = self.user_followers.update_is_blocked(is_blocked)
        return result

    def unfollow(self):
        result = self.user_followers.unfollow()
        return result

    def get(self):
        result = self.user_followers.get()
        if result is not None:
            return json.dumps(result.serialize)
        return result

    def get_all(self):
        result = self.user_followers.get_all()
        if result is not None:
            return Helper.json_list(result)
        return result
