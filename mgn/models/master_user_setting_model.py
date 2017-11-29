from mgn import db
from mgn.models.master_currency_model import MasterCurrencyModel
from mgn.models.master_language_model import MasterLanguageModel
from mgn.models.master_timezone_model import MasterTimezoneModel
from mgn.models.master_user_model import MasterUserModel


class MasterUserSettingModel(db.Model):
    __tablename__ = 'master_user_setting'
    __table_args__ = {"schema": "mgn"}
    master_user_setting_id = db.Column(db.BigInteger, primary_key=True)
    master_user_id = db.Column(db.BigInteger, db.ForeignKey(MasterUserModel.master_user_id))
    master_language_id = db.Column(db.Integer, db.ForeignKey(MasterLanguageModel.master_language_id))
    timezone_id = db.Column(db.Integer, db.ForeignKey(MasterTimezoneModel.timezone_id))
    master_currency_id = db.Column(db.Integer, db.ForeignKey(MasterCurrencyModel.master_currency_id))

    master_user = db.relationship('MasterUserModel', backref=db.backref('user', lazy='dynamic'))
    master_timezone = db.relationship('MasterTimezoneModel', backref=db.backref('timezone', lazy='dynamic'))
    master_language = db.relationship('MasterLanguageModel', backref=db.backref('language', lazy='dynamic'))
    master_currency = db.relationship('MasterCurrencyModel', backref=db.backref('currency', lazy='dynamic'))

    @property
    def id(self):
        return self.master_user_setting_id

    def __init__(self, master_user_id=None, master_language_id=None, timezone_id=None, master_currency_id=None):
        self.master_user_id = master_user_id
        self.master_language_id = master_language_id
        self.timezone_id = timezone_id
        self.master_currency_id = master_currency_id

    @property
    def serialize(self):
        return {
            'id': self.master_user_setting_id,
            'user': self.master_user.serialize,
            'language': self.master_language.serialize,
            'timezone': self.master_timezone.serialize,
            'currency': self.master_currency.serialize
        }
