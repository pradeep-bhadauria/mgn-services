from threading import Thread
from functools import wraps
from mgn.utils.token import confirm_token
from flask import request
from mgn.utils.general_response import UNAUTHENTICATED_RESPONSE
from mgn.services.constants import LONG_TOKEN_VALIDITY


def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()

    return wrapper


def requires_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            header_email = request.headers["Email"]
            header_uid = request.headers["Id"]
            cookie_email = request.cookies["EID"]
            cookie_uid = request.cookies["UID"]
            if str(header_email) == str(confirm_token(cookie_email, LONG_TOKEN_VALIDITY)) and str(header_uid) == str(
                    confirm_token(cookie_uid, LONG_TOKEN_VALIDITY)):
                return f(*args, **kwargs)
            return UNAUTHENTICATED_RESPONSE
        except:
            return UNAUTHENTICATED_RESPONSE

    return decorated_function
