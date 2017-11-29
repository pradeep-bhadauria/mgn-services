import cloudinary

# Clodinary image and file uploads Management.
cloudinary.config(
        cloud_name="doivakz2v",
        api_key="789793767717378",
        api_secret="DDMw68gZ1R_LtT4Hhp1WaIUsips"
)

ALLOWED_EXTENSIONS_IMAGES = set(['png', 'jpg', 'jpeg', 'gif'])
ALLOWED_MESSAGE_ATTACHMENTS = set(['png', 'jpg', 'jpeg', 'gif', 'txt', 'pdf', 'doc', 'docx', 'zip'])


# Max size in mb's
MAX_SIZE_FILE = 5
MAX_SIZE_IMAGE = 3

# Sparkpost Configuration
SPARK_POST_CONTENT_TYPE = "application/json"
SPARK_POST_AUTHORIZATION = "aa08d21fc53c1c95da7fcb9da569248f02f51181"

CONFIRM_MAIL_INPUT = {"options":{"open_tracking":True,"click_tracking":True},"metadata":{"some_useful_metadata":"Email Verification"},"substitution_data":{"signature":"Medical Globalnet"},"recipients":[{"address":{"email":""},"tags":["email_verification"],"substitution_data":{"first_name":"","signature":"Medical Globalnet Team","link":""}}],"content":{"from":{"name":"Medical Globalnet","email":"admin@sendmail.medicalglobalnet.com"},"subject":"Email Verification","text":"Hi {{first_name}}\r\nYou recently registered on MedicalGlobalnet.com !\r\nFollow the link below to verify your account\r\n{{link}}\r\nCongratulations,\r\n{{signature}}","html":"<b>Hi {{first_name}}</b></br><p>You recently registered on MedicalGlobalnet.com</br></p><p>Follow the link below to verify your account</br></p><p>Link : {{link}}</br></p><p>Congratulations,{{signature}}</br></p>"}}
CHANGE_PASSWORD_MAIL_INPUT = {"options":{"open_tracking":True,"click_tracking":True},"metadata":{"some_useful_metadata":"Forgot Password"},"substitution_data":{"signature":"Medical Globalnet"},"recipients":[{"address":{"email":""},"tags":["forgot_password"],"substitution_data":{"first_name":"","signature":"Medical Globalnet Team","link":""}}],"content":{"from":{"name":"Medical Globalnet","email":"admin@sendmail.medicalglobalnet.com"},"subject":"Forgot Password","text":"Hi {{first_name}}\r\n\Follow the link below to change your password\r\n{{link}}\r\nThanks,\r\n{{signature}}","html":"<b>Hi {{first_name}}</b></br><p>Follow the link below to change your password</br></p><p>Link : {{link}}</br></p><p>Thanks,{{signature}}</br></p>"}}
COMFIRM_ACCOUNT_SECRET_KEY = 'cnQBCNKscnAWEUF9E8HSXAWEUH988FY07814R3D23HBK32J4E3BE3'
CONFIRM_ACCOUNT_SECURITY_PASSWORD_SALT = 'medical_global_net'


# Oauth Credentials
OAUTH_CREDENTIALS = {
    'facebook': {
        'id': '242406039534569',
        'secret': '1cd12a6e20440df5e8626c7e8f3ed180',
        'auth_type_id': 2
    }
}

# User Pagination Conf
USER_PAGINATION_LIMIT = 30

# Messages Pagination Conf
MESSAGE_LIST_PAGINATION_LIMIT = 30
MESSAGE_PAGINATION_LIMIT = 10

# Default Pagination Limit
PAGINATION_LIMIT = 10





