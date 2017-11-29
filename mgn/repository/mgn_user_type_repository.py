from mgn import db
from mgn.models.mgn_user_type_model import MGNUserTypeModel


class MgnUserTypeRepository:
    mgn_user_type_id = None

    def __init__(self, mgn_user_type_id=None):
        self.mgn_user_type_id = mgn_user_type_id

    @staticmethod
    def add_new_user_type(type=None, desc=None):
        try:
            data = MGNUserTypeModel(
                    user_type=type,
                    user_type_desc=desc
            )
            db.session.add(data)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def get(self):
        user_type_details = MGNUserTypeModel.query.filter_by(mgn_user_type_id=self.mgn_user_type_id).first()
        return user_type_details

    @staticmethod
    def get_all():
        list_user_type_details = MGNUserTypeModel.query
        return list_user_type_details

    def update_user_type(self, type=None, desc=None):
        try:
            MGNUserTypeModel.query.filter_by(mgn_user_type_id=self.mgn_user_type_id).update(dict(
                    user_type=type,
                    user_type_desc=desc
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise
