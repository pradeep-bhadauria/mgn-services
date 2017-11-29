from flask import json
from mgn.repository.mgn_auth_type_repository import MgnAuthTypeRepository
from mgn.utils.helper import Helper


class MgnAuthTypeDelegate:
    mgn_auth_type = None

    def __init__(self, auth_type_id=None):
        if auth_type_id is not None:
            self.mgn_auth_type = MgnAuthTypeRepository(auth_type_id)
        else:
            self.mgn_auth_type = MgnAuthTypeRepository()

    def add(self, name=None, desc=None):
        result = self.mgn_auth_type.add_new_auth_type(name, desc)
        return result

    def get(self):
        result = self.mgn_auth_type.get()
        if result is not None:
            return json.dumps(result.serialize)
        return result

    def get_all(self):
        result = self.mgn_auth_type.get_all()
        if result is not None:
            return Helper.json_list(result)
        return result

    def update(self, name=None, desc=None):
        result = self.mgn_auth_type.update_auth_type(name, desc)
        return result
