from mgn import db
from mgn.utils.constants import ACTIVE, INACTIVE
from mgn.models.master_language_model import MasterLanguageModel


class MasterLanguageRepository:
    master_language_id = None

    def __init__(self, master_language_id=None):
        self.master_language_id = master_language_id

    @staticmethod
    def add(name=None, desc=None, is_active=None):
        try:
            data = MasterLanguageModel(
                    language_name=name,
                    language_description=desc,
                    is_active=is_active
            )
            db.session.add(data)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def get(self):
        master_language_details = MasterLanguageModel.query.filter_by(
                master_language_id=self.master_language_id).first()
        return master_language_details

    @staticmethod
    def get_all():
        list_master_language_details = MasterLanguageModel.query
        return list_master_language_details

    @staticmethod
    def get_active():
        list_master_language_details = MasterLanguageModel.query.filter_by(is_active=ACTIVE)
        return list_master_language_details

    @staticmethod
    def get_inactive():
        list_master_language_details = MasterLanguageModel.query.filter_by(is_active=INACTIVE)
        return list_master_language_details

    @staticmethod
    def search(q=None):
        list_master_language_details = MasterLanguageModel.query.filter(
                MasterLanguageModel.language_name.ilike('%' + q + '%')

        )
        return list_master_language_details

    def update_language_details(self, name=None, desc=None):
        try:
            MasterLanguageModel.query.filter_by(master_language_id=self.master_language_id).update(dict(
                    language_name=name,
                    language_description=desc
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_language_is_active(self, is_active=None):
        try:
            MasterLanguageModel.query.filter_by(master_language_id=self.master_language_id).update(dict(
                    is_active=is_active
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise
