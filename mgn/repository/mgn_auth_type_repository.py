from mgn import db
from mgn.models.mgn_auth_type_model import MGNAuthTypeModel


class MgnAuthTypeRepository:
    auth_type_id = None

    def __init__(self, auth_type_id=None):
        self.auth_type_id = auth_type_id

    @staticmethod
    def add_new_auth_type(name=None, desc=None):
        try:
            data = MGNAuthTypeModel(
                    auth_name=name,
                    auth_desc=desc
            )
            db.session.add(data)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def get(self):
        auth_type_details = MGNAuthTypeModel.query.filter_by(auth_type_id=self.auth_type_id).first()
        return auth_type_details

    @staticmethod
    def get_all():
        list_auth_type_details = MGNAuthTypeModel.query
        return list_auth_type_details

    def update_auth_type(self, name=None, desc=None):
        try:
            MGNAuthTypeModel.query.filter_by(auth_type_id=self.auth_type_id).update(dict(
                    auth_name=name,
                    auth_desc=desc
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise
