from mgn import db
from mgn.models.user_followers_model import UserFollowersModel


class UserFollowersRepository:
    follower = None
    following = None

    def __init__(self, follower=None, following=None):
        self.follower = follower
        self.following = following

    def add(self):
        try:
            data = UserFollowersModel(
                    follower=self.follower,
                    following=self.following
            )
            db.session.add(data)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def get(self):
        user_following_details = UserFollowersModel.query.filter_by(
                follower=self.follower,
                following=self.following
        ).first()
        return user_following_details

    def get_all(self):
        list_user_following_details = UserFollowersModel.query.filter_by(
                follower=self.follower
        )
        return list_user_following_details

    def update_is_blocked(self, is_blocked=None):
        try:
            UserFollowersModel.query.filter_by(
                    follower=self.follower,
                    following=self.following
            ).update(dict(
                    is_blocked=is_blocked
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def unfollow(self):
        try:
            UserFollowersModel.query.filter_by(
                follower=self.follower,
                following=self.following
            ).delete()
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise