import datetime
from mgn import db
from mgn.services.constants import *
from mgn.models.mgn_countries_model import MgnCountriesModel


class MgnCountriesRepository:
    country_id = None

    def __init__(self, country_id=None):
        self.country_id = country_id

    @staticmethod
    def add_new_country(short_name=None, full_name=None, isd_codes=None, states=None, cities=None,
            is_active=None):
        try:
            data = MgnCountriesModel(
                    short_name=short_name,
                    full_name=full_name,
                    isd_code=isd_codes,
                    states=states,
                    cities=cities,
                    is_active=is_active
            )
            db.session.add(data)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def get(self):
        country_details = MgnCountriesModel.query.filter_by(country_id=self.country_id).first()
        return country_details

    @staticmethod
    def get_all():
        list_country_details = MgnCountriesModel.query.filter_by(is_active=ACTIVE)
        return list_country_details

    def update_is_active(self,is_active=None):
        try:
            MgnCountriesModel.query.filter_by(country_id=self.country_id).update(dict(
                    is_active=is_active
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_country(self, short_name=None, full_name=None, isd_codes=None):
        try:
            MgnCountriesModel.query.filter_by(country_id=self.country_id).update(dict(
                    short_name=short_name,
                    full_name=full_name,
                    isd_code=isd_codes
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_states(self, states=None):
        try:
            MgnCountriesModel.query.filter_by(country_id=self.country_id).update(dict(
                    states=states
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_cities(self, cities=None):
        try:
            MgnCountriesModel.query.filter_by(country_id=self.country_id).update(dict(
                cities=cities
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise