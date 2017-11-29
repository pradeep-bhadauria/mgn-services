from itsdangerous import URLSafeTimedSerializer
from mgn.utils.config import COMFIRM_ACCOUNT_SECRET_KEY, CONFIRM_ACCOUNT_SECURITY_PASSWORD_SALT


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(COMFIRM_ACCOUNT_SECRET_KEY)
    return serializer.dumps(email, salt=CONFIRM_ACCOUNT_SECURITY_PASSWORD_SALT)


def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(COMFIRM_ACCOUNT_SECRET_KEY)
    try:
        email = serializer.loads(
                token,
                salt=CONFIRM_ACCOUNT_SECURITY_PASSWORD_SALT,
                max_age=expiration
        )
    except:
        return False
    return email
