from flask import json
from mgn.repository.user_access_details_repository import UserAccessDetailsRepository
from mgn.utils.helper import Helper


class UserAccessDetailsDelegate:
    user_access_details = None

    def __init__(self, master_user_id=None):
        if master_user_id is not None:
            self.user_access_details = UserAccessDetailsRepository(master_user_id)
        else:
            self.user_access_details = UserAccessDetailsRepository()

    def add(self, master_user_id=None, latitude=None, longitude=None, city=None, state=None, zipcode=None,
            country_code=None, browser=None, device=None, request_string=None, platform=None):
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
        access_history_list = list()
        access_history_list.append(new_access)
        access_history = {'access_history_list': access_history_list}
        result = self.user_access_details.add(master_user_id, access_history , latitude, longitude, city, state,
                                              zipcode, country_code, browser, device, request_string, platform)
        return result

    def get(self):
        result = self.user_access_details.get()
        if result is not None:
            return json.dumps(result.serialize)
        return result

    def update(self, latitude=None, longitude=None, city=None, state=None, zipcode=None, country_code=None,
               browser=None, device=None, request_string=None, platform=None):
        result = self.user_access_details.update(latitude, longitude, city, state, zipcode, country_code, browser,
                                                 device, request_string, platform)
        return result
