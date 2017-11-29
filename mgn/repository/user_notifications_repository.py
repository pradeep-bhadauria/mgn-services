from mgn import db
from mgn.models.user_notifications_model import UserNotificationsModel
from mgn.utils.constants import FALSE


class UserNotificationsRepository:
    master_user_id = None

    def __init__(self, master_user_id=None):
        self.master_user_id = master_user_id

    def add(self, notifications=None, exists=None):
        try:
            if exists == FALSE:
                data = UserNotificationsModel(
                        master_user_id=self.master_user_id,
                        notifications=notifications
                )
                db.session.add(data)
                db.session.commit()
                return True
            else:
                self.update(notifications)
                db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def get(self):
        user_notifications = UserNotificationsModel.query.filter_by(master_user_id=self.master_user_id).first()
        return user_notifications

    def update(self, notifications=None):
        try:
            UserNotificationsModel.query.filter_by(master_user_id=self.master_user_id).update(dict(
                    notifications=notifications
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise
