SUCCESS = {"status": "success", "status_code": 200, "message": "Request successful."}
ERROR = {"status": "error", "status_code": 400, "message": "Please check all mandatory fields and try again."}
INVALID = {"status": "error", "status_code": 400, "message": "Invalid request."}
FAILURE = {"status": "failed", "status_code": 500, "message": "We had some issue. Please try again."}
UNAUTHORIZED = {"status": "unauthorized", "status_code": 403,
                "message": "You are not authorized to access this content."}
UNAUTHENTICATED = {"status": "unauthenticated", "status_code": 401,
                   "message": "You don't have sufficient permission to make this request."}

ADDED = "Added Successfully"
DELETED = "Deleted Successfully"
UPDATED = "Updated Successfully"

NO_DATA = "No Data Available"
INVALID_ID = "Invalid Id"
EMPTY_LIST = "[]"

TRUE = 1
FALSE = 0

ACTIVE = 1
INACTIVE = 0

# Various Auth Types
EMAIL = 1
FACEBOOK = 2
GMAIL = 3

# Various User Types
GENERAL = 1
PROFESSIONAL = 2
ADMIN = 3

# Various Gender Types
MALE = 1
FEMALE = 2
TRANS = 3

MAX_MESSAGE_PARTICIPANT_COUNT = 30

#Timeline constants
TIMELINE = {
    "blog":"BLOG",
    "post":"POST",
    "share":"SHARE",
    "comment":"COMMENT",
    "like":"LIKE"
}

TIMELINE_ACTIVITY_TYPE = {
    "blog":"blog",
    "post":"post",
    "share":"share",
    "blog_comment":"b_comment",
    "post_comment":"p_comment",
    "share_comment":"s_comment",
    "blog_like":"b_like",
    "post_like":"p_like",
    "share_like":"s_like"
}
