from mgn import db
from mgn.models.user_profile_model import UserProfileModel


class UserProfileRepository:
    master_user_id = None

    def __init__(self, master_user_id=None):
        self.master_user_id = master_user_id

    @staticmethod
    def add(profile_banner_image=None, dob=None, master_gender_id=None, master_user_id=None):
        try:
            data = UserProfileModel(
                    profile_banner_image=profile_banner_image,
                    dob=dob,
                    master_gender_id=master_gender_id,
                    master_user_id=master_user_id
            )
            db.session.add(data)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def get(self):
        user_profile_details = UserProfileModel.query.filter_by(
                master_user_id=self.master_user_id).first()
        return user_profile_details

    def update_profile_banner_image(self, profile_banner_image=None):
        try:
            UserProfileModel.query.filter_by(master_user_id=self.master_user_id).update(dict(
                    profile_banner_image=profile_banner_image
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_dob(self, dob=None):
        try:
            UserProfileModel.query.filter_by(master_user_id=self.master_user_id).update(dict(
                    dob=dob
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_gender(self, master_gender_id=None):
        try:
            UserProfileModel.query.filter_by(master_user_id=self.master_user_id).update(dict(
                    master_gender_id=master_gender_id
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise
