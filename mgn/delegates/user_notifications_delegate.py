import datetime
from flask import json
from mgn.repository.user_notifications_repository import UserNotificationsRepository
from mgn.utils.constants import FALSE, TRUE


class UserNotificationsDelegate:
    user_notifications = None

    def __init__(self, master_user_id=None):
        if master_user_id is not None:
            self.user_notifications = UserNotificationsRepository(master_user_id)
        else:
            self.user_notifications = UserNotificationsRepository()

    def add(self, n_type=None, n_message=None, n_url=None, n_timestamp=None):
        new_notification = dict(
                n_type=n_type,
                n_message=n_message,
                n_url=n_url,
                n_timestamp=n_timestamp,
                n_read_status=FALSE,
                n_read_timestamp=''
        )
        notification_list = list()
        notification_list.append(new_notification)
        exists = FALSE
        get_notifications = self.user_notifications.get()
        if get_notifications is not None:
            notification_list = get_notifications.__dict__['notifications']['notification_list']
            notification_list.append(new_notification)
            exists = TRUE
        notifications = {'notification_list': notification_list}
        result = self.user_notifications.add(notifications, exists)
        return result

    def get(self):
        result = self.user_notifications.get()
        if result is not None:
            return json.dumps(result.serialize)
        return result

    def update(self):
        get_notifications = self.user_notifications.get()
        if get_notifications is not None:
            new_notification_list = list()
            notification_list = get_notifications.__dict__['notifications']['notification_list']
            for notification in notification_list:
                if notification['n_read_status'] == FALSE:
                    notification['n_read_status'] = TRUE
                    notification['n_read_timestamp'] = str(datetime.datetime.utcnow())
                new_notification_list.append(notification)
                notifications = {'notification_list': new_notification_list}
        result = self.user_notifications.update(notifications)
        return result
