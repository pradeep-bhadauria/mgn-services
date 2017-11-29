from flask import json
from mgn.repository.master_user_setting_repository import MasterUserSettingRepository


class MasterUserSettingDelegate:
    master_user_setting = None

    def __init__(self, master_user_id=None):
        self.master_user_setting = MasterUserSettingRepository(master_user_id)

    def add(self, master_user_id=None, master_language_id=None, master_timezone_id=None, master_currency_id=None):
        result = self.master_user_setting.add(master_user_id, master_language_id, master_timezone_id, master_currency_id)
        return result

    def get(self):
        result = self.master_user_setting.get()
        if result is not None:
            return json.dumps(result.serialize)
        return result

    def update_language(self, language_id=None):
        result = self.master_user_setting.update_language(language_id)
        return result

    def update_timezone(self, timezone_id=None):
        result = self.master_user_setting.update_timezone(timezone_id)
        return result

    def update_currency(self, currency_id=None):
        result = self.master_user_setting.update_currency(currency_id)
        return result

