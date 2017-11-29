from mgn import db
from mgn.utils.constants import ACTIVE, INACTIVE
from mgn.models.master_timezone_model import MasterTimezoneModel


class MasterTimezoneRepository:
    timezone_id = None

    def __init__(self, timezone_id=None):
        self.timezone_id = timezone_id

    @staticmethod
    def add(code=None, desc=None, offset=None, offset_dst=None, is_active=None):
        try:
            data = MasterTimezoneModel(
                    timezone_code=code,
                    timezone_description=desc,
                    timezone_offset=offset,
                    timezone_offset_dst=offset_dst,
                    is_active=is_active
            )
            db.session.add(data)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def get(self):
        master_timezone_details = MasterTimezoneModel.query.filter_by(
                timezone_id=self.timezone_id).first()
        return master_timezone_details

    @staticmethod
    def get_all():
        list_master_timezone_details = MasterTimezoneModel.query
        return list_master_timezone_details

    @staticmethod
    def get_active():
        list_master_timezone_details = MasterTimezoneModel.query.filter_by(is_active=ACTIVE)
        return list_master_timezone_details

    @staticmethod
    def get_inactive():
        list_master_timezone_details = MasterTimezoneModel.query.filter_by(is_active=INACTIVE)
        return list_master_timezone_details

    @staticmethod
    def search(q=None):
        list_master_timezone_details = MasterTimezoneModel.query.filter(
                MasterTimezoneModel.timezone_code.ilike('%' + q + '%')
        )
        return list_master_timezone_details

    def update_timezone_details(self, code=None, desc=None, offset=None, offset_dst=None):
        try:
            MasterTimezoneModel.query.filter_by(timezone_id=self.timezone_id).update(dict(
                    timezone_code=code,
                    timezone_description=desc,
                    timezone_offset=offset,
                    timezone_offset_dst=offset_dst
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_timezone_is_active(self, is_active=None):
        try:
            MasterTimezoneModel.query.filter_by(timezone_id=self.timezone_id).update(dict(
                    is_active=is_active
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise
