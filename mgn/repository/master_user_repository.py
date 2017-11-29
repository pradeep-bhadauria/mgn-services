import datetime
from mgn import db
from sqlalchemy.sql import or_
from mgn.utils.constants import ACTIVE, INACTIVE
from mgn.models.master_user_model import MasterUserModel
from werkzeug import generate_password_hash


class MasterUserRepository:
    master_user_id = None

    def __init__(self, master_user_id=None):
        self.master_user_id = master_user_id

    @staticmethod
    def make_unique_username(username=None):
        if MasterUserModel.query.filter_by(username=username).first() is None:
            return username
        version = 2
        while True:
            new_name = username + str(version)
            if MasterUserModel.query.filter_by(username=new_name).first() is None:
                break
            version += 1
        return new_name

    @staticmethod
    def register(first_name=None, last_name=None, email=None, password=None, auth_type_id=None, mgn_user_type_id=None,
                 profile_pic=None,social_id=None):
        try:
            username = MasterUserRepository.make_unique_username(first_name + last_name)
            data = MasterUserModel(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=username,
                    password=generate_password_hash(password),
                    auth_type_id=auth_type_id,
                    mgn_user_type_id=mgn_user_type_id,
                    profile_pic=profile_pic,
                    social_id=social_id
            )
            db.session.add(data)
            db.session.flush()
            uuid = data.auth_type_id
            db.session.commit()
            return uuid
        except:
            db.session.rollback()
            raise

    def get(self):
        master_user_details = MasterUserModel.query.filter_by(
                master_user_id=self.master_user_id).first()
        return master_user_details

    @staticmethod
    def get_by_email(email=None):
        master_user_details = MasterUserModel.query.filter_by(email=email).first()
        return master_user_details

    @staticmethod
    def get_by_username(username=None):
        master_user_details = MasterUserModel.query.filter_by(username=username).first()
        return master_user_details

    @staticmethod
    def get_all():
        list_master_user_details = MasterUserModel.query
        return list_master_user_details

    @staticmethod
    def get_active():
        list_master_user_details = MasterUserModel.query.filter_by(is_active=ACTIVE)
        return list_master_user_details

    @staticmethod
    def get_inactive():
        list_master_user_details = MasterUserModel.query.filter_by(is_active=INACTIVE)
        return list_master_user_details

    @staticmethod
    def search(q=None):
        list_master_user_details = MasterUserModel.query.filter(
                MasterUserModel.full_name.ilike('%' + q + '%')
        )
        return list_master_user_details

    def update_name(self, first_name=None, last_name=None):
        try:
            MasterUserModel.query.filter_by(master_user_id=self.master_user_id).update(dict(
                    first_name=first_name,
                    last_name=last_name,
                    full_name=first_name + " " + last_name,
                    updated=datetime.datetime.utcnow()
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_user_email(self, email=None):
        try:
            MasterUserModel.query.filter_by(master_user_id=self.master_user_id).update(dict(
                    email=email,
                    updated=datetime.datetime.utcnow()
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_user_username(self, username=None):
        try:
            MasterUserModel.query.filter_by(master_user_id=self.master_user_id).update(dict(
                    username=username,
                    updated=datetime.datetime.utcnow()
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_user_password(self, password=None):
        try:
            MasterUserModel.query.filter_by(master_user_id=self.master_user_id).update(dict(
                    password=generate_password_hash(password),
                    updated=datetime.datetime.utcnow()
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_user_is_active(self, is_active=None):
        try:
            MasterUserModel.query.filter_by(master_user_id=self.master_user_id).update(dict(
                    is_active=is_active,
                    updated=datetime.datetime.utcnow()
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_user_is_deleted(self, is_deleted=None):
        try:
            MasterUserModel.query.filter_by(master_user_id=self.master_user_id).update(dict(
                    is_deleted=is_deleted,
                    updated=datetime.datetime.utcnow()
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_user_is_blocked(self, is_blocked=None):
        try:
            MasterUserModel.query.filter_by(master_user_id=self.master_user_id).update(dict(
                    is_blocked=is_blocked,
                    updated=datetime.datetime.utcnow()
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_profile_pic(self, profile_pic=None):
        try:
            MasterUserModel.query.filter_by(master_user_id=self.master_user_id).update(dict(
                    profile_pic=profile_pic,
                    updated=datetime.datetime.utcnow()
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise
