from mgn import db
from mgn.models.user_access_details_model import UserAccessDetailsModel


class UserAccessDetailsRepository:
    master_user_id = None

    def __init__(self, master_user_id=None):
        self.master_user_id = master_user_id

    @staticmethod
    def add(master_user_id=None, access_history=None, latitude=None, longitude=None, city=None, state=None,
            zipcode=None, country_code=None, browser=None, device=None, request_string=None, platform=None):
        try:
            data = UserAccessDetailsModel(
                    master_user_id=master_user_id,
                    access_history=access_history,
                    latitude=latitude,
                    longitude=longitude,
                    city=city,
                    state=state,
                    zipcode=zipcode,
                    country_code=country_code,
                    browser=browser,
                    device=device,
                    request_string=request_string,
                    platform=platform
            )
            db.session.add(data)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def get(self):
        user_type_details = UserAccessDetailsModel.query.filter_by(master_user_id=self.master_user_id).first()
        return user_type_details

    def update(self, latitude=None, longitude=None, city=None, state=None, zipcode=None, country_code=None,
               browser=None, device=None, request_string=None, platform=None):
        try:
            new_access = dict(
                    latitude=latitude,
                    longitude=longitude,
                    city=city,
                    state=state,
                    zipcode=zipcode,
                    country_code=country_code,
                    browser=browser,
                    device=device,
                    request_string=request_string,
                    platform=platform
            )
            user_type_details = UserAccessDetailsModel.query.filter_by(master_user_id=self.master_user_id).first()
            access_history_list = user_type_details.__dict__['access_history']['access_history_list']
            if len(access_history_list) == 30:
                access_history_list.pop(0)
            access_history_list.append(new_access)
            access_history = {'access_history_list': access_history_list}
            UserAccessDetailsModel.query.filter_by(master_user_id=self.master_user_id).update(dict(
                    access_history=access_history,
                    latitude=latitude,
                    longitude=longitude,
                    city=city,
                    state=state,
                    zipcode=zipcode,
                    country_code=country_code,
                    browser=browser,
                    device=device,
                    request_string=request_string,
                    platform=platform
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise
