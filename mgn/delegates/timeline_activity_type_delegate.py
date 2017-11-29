from flask import json
from mgn.repository.timeline_activity_type_repository import TimelineActivityTypeRepository
from mgn.utils.helper import Helper


class TimelineActivityTypeDelegate:
    timeline_activity_type = None

    def __init__(self, timeline_activity_type_id=None):
        self.timeline_activity_type = TimelineActivityTypeRepository(timeline_activity_type_id)

    def add(self, name=None, description=None):
        result = self.timeline_activity_type.add(name, description)
        return result

    def update(self, name=None, description=None):
        result = self.timeline_activity_type.update(name, description)
        return result

    def delete(self):
        result = self.timeline_activity_type.delete()
        return result

    def get(self):
        result = self.timeline_activity_type.get()
        if result is not None:
            return json.dumps(result.serialize)
        return result

    def get_by_name(self,name=None):
        result = self.timeline_activity_type.get_by_name(name)
        return result

    def get_all(self):
        result = self.timeline_activity_type.get_all()
        if result is not None:
            return Helper.json_list(result)
        return result
