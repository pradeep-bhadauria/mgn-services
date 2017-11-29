from flask import json
from mgn.repository.timeline_repository import TimelineRepository
from mgn.utils.helper import Helper


class TimelineDelegate:
    timeline = None

    def __init__(self, master_user_id=None):
        self.timeline = TimelineRepository(master_user_id)

    def add(self, post_id=None, blog_id=None, share_id=None, comment_id=None, like_id=None,
            timeline_activity_type_id=None):
        result = self.timeline.add(post_id, blog_id, share_id, comment_id, like_id, timeline_activity_type_id)
        return result

    def delete(self, delete_id=None, delete_type=None):
        result = self.timeline.delete(delete_id, delete_type)
        return result

    def get_timiline(self, offset=0):
        result = self.timeline.get_timeline(offset)
        if result is not None:
            return Helper.json_list(result)
        return result

    def get_feeds(self, offset=0):
        result = self.timeline.get_feeds(offset)
        if result is not None:
            return Helper.json_list(result)
        return result
