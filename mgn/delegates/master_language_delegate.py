from flask import json
from mgn.repository.master_language_repository import MasterLanguageRepository
from mgn.utils.helper import Helper


class MasterLanguageDelegate:
    master_language = None

    def __init__(self, master_language_id=None):
        self.master_language = MasterLanguageRepository(master_language_id)

    def add(self, name=None, desc=None, is_active=None):
        result = self.master_language.add(name, desc, is_active)
        return result

    def update_language_details(self, name=None, desc=None):
        result = self.master_language.update_language_details(name, desc)
        return result

    def update_language_is_active(self, is_active=None):
        result = self.master_language.update_language_is_active(is_active)
        return result

    def get(self):
        result = self.master_language.get()
        if result is not None:
            return json.dumps(result.serialize)
        return result

    def get_all(self):
        result = self.master_language.get_all()
        if result is not None:
            return Helper.json_list(result)
        return result

    def get_active(self):
        result = self.master_language.get_active()
        if result is not None:
            return Helper.json_list(result)
        return result

    def get_inactive(self):
        result = self.master_language.get_inactive()
        if result is not None:
            return Helper.json_list(result)
        return result

    def search(self, q=None):
        result = self.master_language.search(q)
        if result is not None:
            return Helper.json_list(result)
        return result
