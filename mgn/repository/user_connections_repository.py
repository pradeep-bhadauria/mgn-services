from mgn import db
from mgn.models.user_connections_model import UserConnectionsModel
from sqlalchemy.sql import and_, or_


class UserConnectionsRepository:
    connected_from_id = None
    connected_to_id = None

    def __init__(self, connected_from_id=None, connected_to_id=None):
        self.connected_from_id = connected_from_id
        self.connected_to_id = connected_to_id

    def add(self):
        try:
            data = UserConnectionsModel(
                    connected_from_id=self.connected_from_id,
                    connected_to_id=self.connected_to_id
            )
            db.session.add(data)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def get(self):
        user_connected_to_id_details = UserConnectionsModel.query.filter(
                or_(
                        and_(
                                UserConnectionsModel.connected_from_id == self.connected_from_id,
                                UserConnectionsModel.connected_to_id == self.connected_to_id
                        ),
                        and_(
                                UserConnectionsModel.connected_to_id == self.connected_from_id,
                                UserConnectionsModel.connected_from_id == self.connected_to_id
                        )
                )
        ).first()
        return user_connected_to_id_details

    def get_all(self):
        list_user_connected_to_id_details = UserConnectionsModel.query.filter_by(
                or_(
                        and_(
                                UserConnectionsModel.connected_from_id == self.connected_from_id,
                                UserConnectionsModel.is_accepted == 1,
                                UserConnectionsModel.is_blocked == 0,
                                UserConnectionsModel.is_ignored == 0

                        ),
                        and_(
                                UserConnectionsModel.connected_to_id == self.connected_from_id,
                                UserConnectionsModel.is_accepted == 1,
                                UserConnectionsModel.is_blocked == 0,
                                UserConnectionsModel.is_ignored == 0
                        )
                )
        )
        return list_user_connected_to_id_details

    def get_pending(self):
        list_user_connected_to_id_details = UserConnectionsModel.query.filter_by(
                and_(
                        UserConnectionsModel.connected_to_id == self.connected_from_id,
                        UserConnectionsModel.is_accepted == 0,
                        UserConnectionsModel.is_blocked == 0,
                        UserConnectionsModel.is_ignored == 0
                )
        )
        return list_user_connected_to_id_details

    def get_sent(self):
        list_user_connected_to_id_details = UserConnectionsModel.query.filter_by(
                and_(
                        UserConnectionsModel.connected_from_id == self.connected_from_id,
                        UserConnectionsModel.is_accepted == 0,
                        UserConnectionsModel.is_blocked == 0,
                        UserConnectionsModel.is_ignored == 0

                )
        )
        return list_user_connected_to_id_details

    def update_is_accepted(self, is_accepted=None):
        try:
            # opposite for recepient to accept connection
            UserConnectionsModel.query.filter_by(
                    connected_from_id=self.connected_to_id,
                    connected_to_id=self.connected_from_id
            ).update(dict(
                    is_accepted=is_accepted
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_is_blocked(self, is_blocked=None):
        try:
            UserConnectionsModel.query.filter_by(
                    connected_from_id=self.connected_from_id,
                    connected_to_id=self.connected_to_id
            ).update(dict(
                    is_blocked=is_blocked
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_is_ignored(self, is_ignored=None):
        try:
            UserConnectionsModel.query.filter_by(
                    connected_from_id=self.connected_from_id,
                    connected_to_id=self.connected_to_id
            ).update(dict(
                    is_ignored=is_ignored
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def update_message_thread(self, message_thread_id=None):
        try:
            UserConnectionsModel.query.filter(
                    or_(
                            and_(
                                    UserConnectionsModel.connected_from_id == self.connected_from_id,
                                    UserConnectionsModel.connected_to_id == self.connected_to_id
                            ),
                            and_(
                                    UserConnectionsModel.connected_to_id == self.connected_from_id,
                                    UserConnectionsModel.connected_from_id == self.connected_to_id
                            )
                    )
            ).update(dict(
                    user_message_thread_id=message_thread_id
            ))
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise

    def delete(self):
        try:
            UserConnectionsModel.query.filter_by(
                    connected_from_id=self.connected_from_id,
                    connected_to_id=self.connected_to_id
            ).delete()
            db.session.commit()
            return True
        except:
            db.session.rollback()
            raise
