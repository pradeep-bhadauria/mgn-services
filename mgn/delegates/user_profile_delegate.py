from flask import json
from mgn.repository.user_profile_repository import UserProfileRepository


class UserProfileDelegate:
    user_profile = None

    def __init__(self, master_user_id=None):
        self.user_profile = UserProfileRepository(master_user_id)

    def add(self, profile_banner_image=None, dob=None, master_gender_id=None, master_user_id=None):
        result = self.user_profile.add(profile_banner_image, dob, master_gender_id, master_user_id)
        return result

    def get(self):
        result = self.user_profile.get()
        if result is not None:
            return json.dumps(result.serialize)
        return result

    def update_profile_banner_image(self, profile_banner_image=None):
        result = self.user_profile.update_profile_banner_image(profile_banner_image)
        return result

    def update_dob(self, dob=None):
        result = self.user_profile.update_dob(dob)
        return result

    def update_gender(self, master_gender_id=None):
        result = self.user_profile.update_gender(master_gender_id)
        return result

