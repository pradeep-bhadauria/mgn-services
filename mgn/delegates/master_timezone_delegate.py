from flask import json
from mgn.repository.master_timezone_repository import MasterTimezoneRepository
from mgn.utils.helper import Helper


class MasterTimezoneDelegate:
    master_timezone = None

    def __init__(self, timezone_id=None):
        self.master_timezone = MasterTimezoneRepository(timezone_id)

    def add(self, code=None, desc=None, offset=None, offset_dst=None, is_active=None):
        result = self.master_timezone.add(code, desc, offset, offset_dst, is_active)
        return result

    def update_timezone_details(self, code=None, desc=None, offset=None, offset_dst=None):
        result = self.master_timezone.update_timezone_details(code, offset, offset_dst, desc)
        return result

    def update_timezone_is_active(self, is_active=None):
        result = self.master_timezone.update_timezone_is_active(is_active)
        return result

    def get(self):
        result = self.master_timezone.get()
        if result is not None:
            return json.dumps(result.serialize)
        return result

    def get_all(self):
        result = self.master_timezone.get_all()
        if result is not None:
            return Helper.json_list(result)
        return result

    def get_active(self):
        result = self.master_timezone.get_active()
        if result is not None:
            return Helper.json_list(result)
        return result

    def get_inactive(self):
        result = self.master_timezone.get_inactive()
        if result is not None:
            return Helper.json_list(result)
        return result

    def search(self, q=None):
        result = self.master_timezone.search(q)
        if result is not None:
            return Helper.json_list(result)
        return result
