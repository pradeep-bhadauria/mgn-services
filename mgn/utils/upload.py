import datetime, time, cloudinary.uploader, cloudinary.api
from werkzeug import secure_filename
from flask import Blueprint, request
from mgn.utils.constants import SUCCESS, ERROR
from mgn.utils.config import *
from mgn.utils.general_response import *

mod = Blueprint('upload', __name__, url_prefix='/utils/upload')


def allowed_images(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS_IMAGES


def allowed_attachment(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_MESSAGE_ATTACHMENTS


@mod.route('/attachment/', methods=['POST'])
def upload_attachment(name):
    file = request.files['file']
    if file and allowed_attachment(file.filename):
        epoch_time = int(time.time())
        filename = secure_filename(str(epoch_time) + "-" + file.filename)
        try:
            obj = cloudinary.uploader.upload(
                    file,
                    public_id='mgn-messages/' + filename,
                    tags=['message'],
                    resource_type='raw'
            )
            SUCCESS["message"] = "Attachment uploaded successfully."
            SUCCESS["url"] = obj["secure_url"]
            SUCCESS["filename"] = filename
            response = generic_success_response(SUCCESS)
        except:
            response = FAILURE_RESPONSE
    else:
        ERROR["message"] = "Invalid file. Only " + ', '.join(ALLOWED_MESSAGE_ATTACHMENTS) + " files are supported."
        response = generic_error_response(ERROR)
    return response


@mod.route('/profile-pic/<int:user_id>', methods=['POST'])
def upload_profile_pic(user_id=None):
    file = request.files['file']
    if file and allowed_images(file.filename):
        filename_160 = secure_filename(user_id + "-img-160x160")
        filename_50 = secure_filename(user_id + "-img-50x50")
        filename_24 = secure_filename(user_id + "-img-24x24")
        try:
            obj_24 = cloudinary.uploader.upload(
                    file,
                    public_id='mgn-profile/' + filename_24,
                    eager=[
                        {'width': 24, 'height': 24,
                         'crop': 'crop', 'gravity': 'face', 'format': 'png'}
                    ],
                    tags=['profile_24']
            )
            obj_50 = cloudinary.uploader.upload(
                    file,
                    public_id='mgn-profile/' + filename_50,
                    eager=[
                        {'width': 50, 'height': 50,
                         'crop': 'crop', 'gravity': 'face', 'format': 'png'}
                    ],
                    tags=['profile_50']
            )

            obj_160 = cloudinary.uploader.upload(
                    file,
                    public_id='mgn-profile/' + filename_160,
                    eager=[
                        {'width': 160, 'height': 160,
                         'crop': 'crop', 'gravity': 'face', 'format': 'png'}
                    ],
                    tags=['profile_160']
            )
            profile_pic = {"profile_pic": [
                {"pic_160": {"public_id": obj_160["public_id"], "secure_url": obj_160["secure_url"]}},
                {"pic_50": {"public_id": obj_50["public_id"], "secure_url": obj_50["secure_url"]}},
                {"pic_24": {"public_id": obj_24["public_id"], "secure_url": obj_24["secure_url"]}}
            ]}

            """
            User.query.filter_by(id=user.id).update(dict(
                    profile_pic=obj["secure_url"],
                    updated=datetime.datetime.utcnow()
            ))
            db.session.commit()
            """
            SUCCESS["message"] = "Profile picture updated successfully."
            SUCCESS["profile_pic"] = profile_pic
            response = generic_success_response(SUCCESS)
        except:
            response = FAILURE_RESPONSE
    else:
        ERROR["message"] = "Invalid file. Only " + ', '.join(ALLOWED_EXTENSIONS_IMAGES) + " files are supported."
        response = generic_error_response(ERROR)
    return response


@mod.route('/user-images/<int:user_id>', methods=['POST'])
@mod.route('/hc-images/<int:hc_id>', methods=['POST'])
@mod.route('/group-images/<int:group_id>', methods=['POST'])
def upload_images(user_id=None, hc_id=None, group_id=None):
    file = request.files['file']
    if file and allowed_images(file.filename):
        epoch_time = int(time.time())
        if user_id is not None:
            filename = secure_filename(str(epoch_time) + "-" + user_id + "-img-500x300")
            tag = "user-images"
        elif hc_id is not None:
            filename = secure_filename(str(epoch_time) + "-" + hc_id + "-img-500x300")
            tag = "hc-images"
        elif group_id is not None:
            filename = secure_filename(str(epoch_time) + "-" + group_id + "-img-500x300")
            tag = "group-images"
        try:
            obj = cloudinary.uploader.upload(
                    file,
                    public_id=tag + '/' + filename,
                    eager=[
                        {'width': 500, 'height': 300,
                         'crop': 'crop', 'gravity': 'north', 'format': 'png', 'format': 'png'}
                    ],
                    tags=[tag]
            )
            SUCCESS["message"] = "Image uploaded successfully."
            SUCCESS["url"] = obj["secure_url"]
            response = generic_success_response(SUCCESS)
        except:
            response = FAILURE_RESPONSE
    else:
        ERROR["message"] = "Invalid file. Only " + ', '.join(ALLOWED_EXTENSIONS_IMAGES) + " files are supported."
        response = generic_error_response(ERROR)
    return response


@mod.route('/user-banner/<int:user_id>', methods=['POST'])
@mod.route('/blog-banner/<int:blog_id>', methods=['POST'])
@mod.route('/hc-banner/<int:hc_id>', methods=['POST'])
@mod.route('/group-banner/<int:group_id>', methods=['POST'])
def upload_banner(user_id=None, blog_id=None, hc_id=None, group_id=None):
    file = request.files['file']
    if file and allowed_images(file.filename):
        if user_id is not None:
            filename = secure_filename(user_id + "-img-800x300")
            tag = "user-banner"
        elif blog_id is not None:
            filename = secure_filename(blog_id + "-img-800x300")
            tag = "blog-banner"
        elif hc_id is not None:
            filename = secure_filename(hc_id + "-img-800x300")
            tag = "hc-banner"
        elif group_id is not None:
            filename = secure_filename(group_id + "-img-800x300")
            tag = "group-banner"
        try:
            obj = cloudinary.uploader.upload(
                    file,
                    public_id=tag + '/' + filename,
                    eager=[
                        {'width': 800, 'height': 300,
                         'crop': 'crop', 'gravity': 'north', 'format': 'png', 'format': 'png'}
                    ],
                    tags=[tag]
            )
            SUCCESS["message"] = "Image uploaded successfully."
            SUCCESS["url"] = obj["secure_url"]
            response = generic_success_response(SUCCESS)
        except:
            response = FAILURE_RESPONSE
    else:
        ERROR["message"] = "Invalid file. Only " + ', '.join(ALLOWED_EXTENSIONS_IMAGES) + " files are supported."
        response = generic_error_response(ERROR)
    return response
