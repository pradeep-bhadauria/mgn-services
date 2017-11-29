from flask import json
from mgn.repository.mgn_user_type_repository import MgnUserTypeRepository
from mgn.utils.helper import Helper


class MgnUserTypeDelegate:
    mgn_user_type = None

    def __init__(self, mgn_user_type_id=None):
        if mgn_user_type_id is not None:
            self.mgn_user_type = MgnUserTypeRepository(mgn_user_type_id)
        else:
            self.mgn_user_type = MgnUserTypeRepository()

    def add(self, type=None, desc=None):
        result = self.mgn_user_type.add_new_user_type(type, desc)
        return result

    def get(self):
        result = self.mgn_user_type.get()
        if result is not None:
            return json.dumps(result.serialize)
        return result

    def get_all(self):
        result = self.mgn_user_type.get_all()
        if result is not None:
            return Helper.json_list(result)
        return result

    def update(self, type=None, desc=None):
        result = self.mgn_user_type.update_user_type(type, desc)
        return result
