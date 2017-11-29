from mgn import db
from mgn.models.master_gender_model import MasterGenderModel


class MasterGenderRepository:
    master_gender_id = None

    def __init__(self, master_gender_id=None):
        self.master_gender_id = master_gender_id

    @staticmethod
    def add(gender=None):
        try:
            data = MasterGenderModel(
                    gender=gender
            )
            db.session.add(data)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def get(self):
        master_gender_details = MasterGenderModel.query.filter_by(master_gender_id=self.master_gender_id).first()
        return master_gender_details

    @staticmethod
    def get_all():
        list_master_gender_details = MasterGenderModel.query
        return list_master_gender_details

    def update(self, gender=None):
        try:
            MasterGenderModel.query.filter_by(master_gender_id=self.master_gender_id).update(dict(
                    gender=gender
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def delete(self):
        try:
            MasterGenderModel.query.filter_by(master_gender_id=self.master_gender_id).delete()
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise
