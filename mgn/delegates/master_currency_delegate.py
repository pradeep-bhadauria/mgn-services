from flask import json
from mgn.repository.master_currency_repository import MasterCurrencyRepository
from mgn.utils.helper import Helper


class MasterCurrencyDelegate:
    master_currency = None

    def __init__(self, master_currency_id=None):
        self.master_currency = MasterCurrencyRepository(master_currency_id)

    def add(self, code=None, name=None, symbol=None, desc=None, is_active=None):
        result = self.master_currency.add(code, name, symbol, desc, is_active)
        return result

    def update_currency_details(self, code=None, name=None, symbol=None, desc=None):
        result = self.master_currency.update_currency_details(code, name, symbol, desc)
        return result

    def update_currency_is_active(self, is_active=None):
        result = self.master_currency.update_currency_is_active(is_active)
        return result

    def get(self):
        result = self.master_currency.get()
        if result is not None:
            return json.dumps(result.serialize)
        return result

    def get_all(self):
        result = self.master_currency.get_all()
        if result is not None:
            return Helper.json_list(result)
        return result

    def get_active(self):
        result = self.master_currency.get_active()
        if result is not None:
            return Helper.json_list(result)
        return result

    def get_inactive(self):
        result = self.master_currency.get_inactive()
        if result is not None:
            return Helper.json_list(result)
        return result

    def search(self, q=None):
        result = self.master_currency.search(q)
        if result is not None:
            return Helper.json_list(result)
        return result
