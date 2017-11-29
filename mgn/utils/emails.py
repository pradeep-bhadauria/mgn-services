import requests
from mgn.utils.config import *


def account_verification(first_name=None, email=None, token=None):
    CONFIRM_MAIL_INPUT["recipients"][0]['substitution_data']['first_name'] = first_name
    CONFIRM_MAIL_INPUT["recipients"][0]['address']['email'] = email
    CONFIRM_MAIL_INPUT["recipients"][0]['substitution_data'][
        'link'] = "http://www.medicalglobalnet.com/confirm-email?email=" + email + "&token=" + token
    return requests.post(
            'https://api.sparkpost.com/api/v1/transmissions',
            headers={'Authorization': SPARK_POST_AUTHORIZATION,
                     'Content-Type': SPARK_POST_CONTENT_TYPE},
            json=CONFIRM_MAIL_INPUT)


def change_password_verification(first_name=None, email=None, token=None):
    CHANGE_PASSWORD_MAIL_INPUT["recipients"][0]['substitution_data']['first_name'] = first_name
    CHANGE_PASSWORD_MAIL_INPUT["recipients"][0]['address']['email'] = email
    CHANGE_PASSWORD_MAIL_INPUT["recipients"][0]['substitution_data'][
        'link'] = "http://www.medicalglobalnet.com/change-password?email=" + email + "&token=" + token
    return requests.post(
            'https://api.sparkpost.com/api/v1/transmissions',
            headers={'Authorization': SPARK_POST_AUTHORIZATION,
                     'Content-Type': SPARK_POST_CONTENT_TYPE},
            json=CHANGE_PASSWORD_MAIL_INPUT)