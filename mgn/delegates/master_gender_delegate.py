from flask import json
from mgn.repository.master_gender_repository import MasterGenderRepository
from mgn.utils.helper import Helper


class MasterGenderDelegate:
    master_gender = None

    def __init__(self, master_gender_id=None):
        self.master_gender = MasterGenderRepository(master_gender_id)

    def add(self, gender=None):
        result = self.master_gender.add(gender)
        return result

    def update(self, gender=None):
        result = self.master_gender.update(gender)
        return result

    def delete(self):
        result = self.master_gender.delete()
        return result

    def get(self):
        result = self.master_gender.get()
        if result is not None:
            return json.dumps(result.serialize)
        return result

    def get_all(self):
        result = self.master_gender.get_all()
        if result is not None:
            return Helper.json_list(result)
        return result
