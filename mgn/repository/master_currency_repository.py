from mgn import db
from sqlalchemy.sql import or_
from mgn.utils.constants import ACTIVE, INACTIVE
from mgn.models.master_currency_model import MasterCurrencyModel


class MasterCurrencyRepository:
    master_currency_id = None

    def __init__(self, master_currency_id=None):
        self.master_currency_id = master_currency_id

    @staticmethod
    def add(code=None, name=None, symbol=None, desc=None, is_active=None):
        try:
            data = MasterCurrencyModel(
                    currency_code=code,
                    currency_name=name,
                    currency_symbol=symbol,
                    currency_description=desc,
                    is_active=is_active
            )
            db.session.add(data)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def get(self):
        master_currency_details = MasterCurrencyModel.query.filter_by(
                master_currency_id=self.master_currency_id).first()
        return master_currency_details

    @staticmethod
    def get_all():
        list_master_currency_details = MasterCurrencyModel.query
        return list_master_currency_details

    @staticmethod
    def get_active():
        list_master_currency_details = MasterCurrencyModel.query.filter_by(is_active=ACTIVE)
        return list_master_currency_details

    @staticmethod
    def get_inactive():
        list_master_currency_details = MasterCurrencyModel.query.filter_by(is_active=INACTIVE)
        return list_master_currency_details

    @staticmethod
    def search(q=None):
        list_master_currency_details = MasterCurrencyModel.query.filter(
                or_(MasterCurrencyModel.currency_code.ilike('%' + q + '%'),
                    MasterCurrencyModel.currency_name.ilike('%' + q + '%')
                    )
        )
        return list_master_currency_details

    def update_currency_details(self, code=None, name=None, symbol=None, desc=None):
        try:
            MasterCurrencyModel.query.filter_by(master_currency_id=self.master_currency_id).update(dict(
                    currency_code=code,
                    currency_name=name,
                    currency_symbol=symbol,
                    currency_description=desc
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_currency_is_active(self, is_active=None):
        try:
            MasterCurrencyModel.query.filter_by(master_currency_id=self.master_currency_id).update(dict(
                    is_active=is_active
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise
