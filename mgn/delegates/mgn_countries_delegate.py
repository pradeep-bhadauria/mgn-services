from flask import json
from mgn.repository.mgn_countries_repository import MgnCountriesRepository
from mgn.utils.helper import Helper


class MgnCountriesDelegate:
    country = None

    def __init__(self, country_id=None):
        if country_id is not None:
            self.country = MgnCountriesRepository(country_id)
        else:
            self.country = MgnCountriesRepository()

    def add(self, short_name=None, full_name=None, isd_codes=None, states=None, cities=None,
            is_active=None):
        result = self.country.add(short_name, full_name, isd_codes, states, cities,
                                  is_active)
        return result

    def get(self):
        result = self.country.get()
        if result is not None:
            return json.dumps(result.serialize)
        return result

    def get_all(self):
        result = self.country.get_all()
        if result is not None:
            return Helper.json_list(result)
        return result

    def update_is_active(self, is_active=None):
        result = self.country.update(is_active)
        return result

    def update_country(self, short_name=None, full_name=None, isd_codes=None):
        result = self.country.update(short_name, full_name, isd_codes)
        return result

    def update_states(self, states=None):
        result = self.country.update(states)
        return result

    def update_cities(self, cities=None):
        result = self.country.update(cities)
        return result