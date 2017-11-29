from flask import json, logging
from mgn.repository.master_user_repository import MasterUserRepository
from mgn.utils.helper import Helper


class MasterUserDelegate:
    master_user = None

    def __init__(self, master_user_id=None):
        self.master_user = MasterUserRepository(master_user_id)

    def register(self, first_name=None, last_name=None, email=None, password=None, auth_type_id=None,
                 mgn_user_type_id=None, profile_pic=None,social_id=None):
        try:
            result = self.master_user.register(first_name, last_name, email, password, auth_type_id, mgn_user_type_id,
                                               profile_pic,social_id)
        except:
            return None
        return result

    def update_user_name(self, first_name=None, last_name=None):
        result = self.master_user.update_name(first_name, last_name)
        return result

    def update_user_username(self, username=None):
        result = self.master_user.update_user_username(username)
        return result

    def update_user_email(self, email=None):
        result = self.master_user.update_user_email(email)
        return result

    def update_user_password(self, password=None):
        result = self.master_user.update_user_password(password)
        return result

    def update_user_is_active(self, is_active=None):
        result = self.master_user.update_user_is_active(is_active)
        return result

    def update_user_is_deleted(self, is_deleted=None):
        result = self.master_user.update_user_email(is_deleted)
        return result

    def update_profile_pic(self, profile_pic=None):
        result = self.master_user.update_profile_pic(profile_pic)
        return result

    def update_user_is_blocked(self, is_blocked=None):
        result = self.master_user.update_user_is_blocked(is_blocked)
        return result

    def get(self):
        result = self.master_user.get()
        if result is not None:
            return json.dumps(result.serialize)
        return result

    def get_by_email(self, email):
        result = self.master_user.get_by_email(email)
        return result

    def get_by_username(self, username):
        result = self.master_user.get_by_username(username)
        if result is not None:
            return json.dumps(result.serialize)
        return result

    def get_all(self):
        result = self.master_user.get_all()
        if result is not None:
            return Helper.json_list(result)
        return result

    def get_active(self):
        result = self.master_user.get_active()
        if result is not None:
            return Helper.json_list(result)
        return result

    def get_inactive(self):
        result = self.master_user.get_inactive()
        if result is not None:
            return Helper.json_list(result)
        return result

    def search(self, fullname=None):
        result = self.master_user.search(fullname)
        if result is not None:
            return Helper.json_list(result)
        return result
