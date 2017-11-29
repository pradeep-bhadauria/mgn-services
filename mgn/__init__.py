import os
import sys
from config import _basedir
from mgn.utils.token import confirm_token

from mgn.utils.constants import SUCCESS
from mgn.utils.general_response import generic_success_response

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

mgn = Flask(__name__)
mgn.config['SWAGGER'] = {
    "swagger_version": "2.0",
    "title": "MGN",
    "headers": [
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Methods', "GET, POST, PUT, DELETE, OPTIONS"),
        ('Access-Control-Allow-Credentials', "true"),
    ],
    "specs": [
        {
            "version": "0.0.1",
            "title": "MGN API v1",
            "endpoint": 'v1_spec',
            "description": 'This is the version 1 of MGN API',
            "route": '/v1/spec'
        }
    ]
}
Swagger(mgn)

mgn.config.from_object('config')

db = SQLAlchemy(mgn)


@mgn.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()


@mgn.before_request
def before_request():
    response_data = SUCCESS.copy()
    if request.method == "OPTIONS":
        response_data["message"] = ""
        response = generic_success_response(response_data)
        return response


# Module default
from mgn.services.default import mod as default
mgn.register_blueprint(default)

# Module auth
from mgn.services.user_authentication_services import mod as userAuthServiceModule
mgn.register_blueprint(userAuthServiceModule)

# Module user
from mgn.services.master_user_services import mod as userServiceModule
mgn.register_blueprint(userServiceModule)

# Module countries
from mgn.services.mgn_countries_services import mod as countriesServiceModule
mgn.register_blueprint(countriesServiceModule)


# Module user type
from mgn.services.mgn_user_type_services import mod as userTypeServiceModule
mgn.register_blueprint(userTypeServiceModule)

# Module auth type
from mgn.services.mgn_auth_type_services import mod as authTypeServiceModule
mgn.register_blueprint(authTypeServiceModule)

# Module master gender
from mgn.services.master_gender_services import mod as masterGenderServiceModule
mgn.register_blueprint(masterGenderServiceModule)

# Module master currency
from mgn.services.master_currency_services import mod as masterCurrencyServiceModule
mgn.register_blueprint(masterCurrencyServiceModule)


# Module master currency
from mgn.services.master_language_services import mod as masterLanguageServiceModule
mgn.register_blueprint(masterLanguageServiceModule)

# Module master timezone
from mgn.services.master_timezone_services import mod as masterTimezoneServiceModule
mgn.register_blueprint(masterTimezoneServiceModule)

# Module master user setting
from mgn.services.master_user_setting_services import mod as masterUserSettingServiceModule
mgn.register_blueprint(masterUserSettingServiceModule)

# Module master user profile
from mgn.services.user_profile_services import mod as userProfileServiceModule
mgn.register_blueprint(userProfileServiceModule)

# Module master user access details
from mgn.services.user_access_details_services import mod as userAccessDetailsModule
mgn.register_blueprint(userAccessDetailsModule)

# Module master user notifications
from mgn.services.user_notifications_services import mod as userNotificationsModule
mgn.register_blueprint(userNotificationsModule)

# Module master messages
from mgn.services.user_message_services import mod as userMessagesModule
mgn.register_blueprint(userMessagesModule)

# Module user follower module
from mgn.services.user_followers_services import mod as userFollowersModule
mgn.register_blueprint(userFollowersModule)

# Module user connection module
from mgn.services.user_connections_services import mod as userConnectionsModule
mgn.register_blueprint(userConnectionsModule)

# Module blogs module
from mgn.services.blogs_services import mod as blogsModule
mgn.register_blueprint(blogsModule)

# Module posts module
from mgn.services.posts_services import mod as postsModule
mgn.register_blueprint(postsModule)

# Module shares module
from mgn.services.shares_services import mod as sharesModule
mgn.register_blueprint(sharesModule)

# Module likes module
from mgn.services.likes_services import mod as likesModule
mgn.register_blueprint(likesModule)

# Module comments module
from mgn.services.comments_services import mod as commentsModule
mgn.register_blueprint(commentsModule)

# Module timeline module
from mgn.services.timeline_services import mod as timelineModule
mgn.register_blueprint(timelineModule)

# Module timeline activity type module
from mgn.services.timeline_activity_type_services import mod as timelineActivityTypeModule
mgn.register_blueprint(timelineActivityTypeModule)

# Module utils upload
from mgn.utils.upload import mod as utilsUploadModule
mgn.register_blueprint(utilsUploadModule)
