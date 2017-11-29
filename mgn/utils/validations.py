import re
from mgn.utils.constants import ACTIVE, INACTIVE, ADMIN, GENERAL, PROFESSIONAL, EMAIL, FACEBOOK, GMAIL, MALE, FEMALE, \
    TRANS, MAX_MESSAGE_PARTICIPANT_COUNT
from mgn.models.master_user_model import MasterUserModel
from mgn.delegates.master_user_delegate import MasterUserDelegate
from mgn.repository.master_user_repository import MasterUserRepository
from voluptuous import Invalid
from voluptuous.validators import Url


def validate_name(name=None):
    if not re.match("^[A-Za-z0-9_-]*$", name):
        raise Invalid("Can contain A-Z a-z 0-9 _ -")
    if int(len(str(name))) not in range(3, 45, 1):
        raise Invalid("Should be between 3 to 45 char long")
    return name


def string_val(string_val=None):
    if not re.match("^[A-Za-z_-]*$", string_val):
        raise Invalid("Can contain A-Z a-z _ -")
    return string_val


def alphanumreic_val(alphanumreic_val=None):
    if not re.match("^[A-Za-z0-9]*$", alphanumreic_val):
        raise Invalid("Can contain A-Z a-z 0-9")
    return alphanumreic_val


def string_code(string_val=None):
    if not re.match("^[A-Za-z_-]*$", string_val):
        raise Invalid("Can contain A-Z a-z _ -")
    return string_val


def validate_password(pwd=None):
    if not re.match("^[-A-Za-z0-9_!@#$%&*()]*$", pwd):
        raise Invalid("Can contain A-Z a-z 0-9 _ - ! @ # $ % & * ( )")
    if len(pwd) not in range(7, 30, 1):
        raise Invalid("Should be between 7 to 30 char long")
    return pwd


def validate_email(email=None):
    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        raise Invalid("Email address not valid")
    if MasterUserModel.query.filter_by(email=email).first() is not None:
        raise Invalid("Email address already in use. Try forgot password.")
    return email


def validate_username(username=None):
    if not re.match("^[A-Za-z0-9_-]*$", username):
        raise Invalid("Can contain A-Z a-z 0-9 _ -")
    if int(len(str(username))) not in range(7, 45, 1):
        raise Invalid("Should be between 7 to 45 char long")
    new_name = MasterUserRepository.make_unique_username(username)
    if new_name != username:
        raise Invalid(username + " not available." + new_name + " is available.")
    return username


def validate_date(date=None):
    if not re.match("\d\d\d\d-\d\d-\d\d", date):
        raise Invalid("Should be in format YYYY-MM-DD")
    return date


def validate_url(url=None):
    if url == "":
        pass
    if Url(url):
        raise Invalid("Invalid URL")
    return url


def validate_gender(gender=None):
    if gender not in [MALE, FEMALE, TRANS]:
        raise Invalid("Invalid Gender")
    return gender


def validate_auth_type(auth_type=None):
    if auth_type not in [EMAIL, FACEBOOK, GMAIL]:
        raise Invalid("Invalid authentication type")
    return auth_type


def validate_is_active(is_active=None):
    if is_active not in [ACTIVE, INACTIVE]:
        raise Invalid("Invalid value")
    return is_active


def validate_like_comment_share_count(count=None):
    if count not in [1, -1]:
        raise Invalid("Invalid value. 1 or -1 expected")
    return count


def validate_user_type(user_type=None):
    if user_type not in [GENERAL, PROFESSIONAL, ADMIN]:
        raise Invalid("Invalid user type")
    return user_type


def validate_user_by_id(master_user_id=None):
    master_user = MasterUserDelegate(master_user_id).get()
    if master_user is None:
        raise Invalid("Invalid user id")
    return master_user_id


def validate_message_participant_list(participant_list=None):
    if len(participant_list) > MAX_MESSAGE_PARTICIPANT_COUNT:
        raise Invalid("Participants can't be more than " + str(MAX_MESSAGE_PARTICIPANT_COUNT))
    return participant_list
