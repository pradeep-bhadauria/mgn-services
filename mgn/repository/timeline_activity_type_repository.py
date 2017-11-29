from mgn import db
from mgn.models.timeline_activity_type_model import TimelineActivityTypeModel


class TimelineActivityTypeRepository:
    timeline_activity_type_id = None

    def __init__(self, timeline_activity_type_id=None):
        self.timeline_activity_type_id = timeline_activity_type_id

    @staticmethod
    def add(name=None, description=None):
        try:
            data = TimelineActivityTypeModel(
                    name=name,
                    description=description
            )
            db.session.add(data)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def get(self):
        timeline_activity_type_details = TimelineActivityTypeModel.query.filter_by(
                timeline_activity_type_id=self.timeline_activity_type_id).first()
        return timeline_activity_type_details

    def get_by_name(self, name=None):
        timeline_activity_type_details = TimelineActivityTypeModel.query.filter_by(
                name=name).first()
        return timeline_activity_type_details

    @staticmethod
    def get_all():
        list_timeline_activity_type_details = TimelineActivityTypeModel.query
        return list_timeline_activity_type_details

    def update(self, name=None, description=None):
        try:
            TimelineActivityTypeModel.query.filter_by(timeline_activity_type_id=self.timeline_activity_type_id).update(
                    dict(
                            name=name,
                            description=description
                    ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def delete(self):
        try:
            TimelineActivityTypeModel.query.filter_by(timeline_activity_type_id=self.timeline_activity_type_id).delete()
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise
