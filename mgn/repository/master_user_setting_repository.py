from mgn import db
from mgn.models.master_user_setting_model import MasterUserSettingModel


class MasterUserSettingRepository:
    master_user_id = None

    def __init__(self, master_user_id=None):
        self.master_user_id = master_user_id

    @staticmethod
    def add(master_user_id=None, master_language_id=None, timezone_id=None, master_currency_id=None):
        try:
            data = MasterUserSettingModel(
                    master_user_id=master_user_id,
                    master_language_id=master_language_id,
                    timezone_id=timezone_id,
                    master_currency_id=master_currency_id
            )
            db.session.add(data)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def get(self):
        master_user_setting_details = MasterUserSettingModel.query.filter_by(
                master_user_id=self.master_user_id).first()
        return master_user_setting_details

    def update_language(self, master_language_id=None):
        try:
            MasterUserSettingModel.query.filter_by(master_user_id=self.master_user_id).update(dict(
                    master_language_id=master_language_id
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_timezone(self, timezone_id=None):
        try:
            MasterUserSettingModel.query.filter_by(master_user_id=self.master_user_id).update(dict(
                    timezone_id=timezone_id
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_currency(self, master_currency_id=None):
        try:
            MasterUserSettingModel.query.filter_by(master_user_id=self.master_user_id).update(dict(
                    master_currency_id=master_currency_id
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise
