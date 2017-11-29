import datetime
from mgn import db


class MasterCurrencyModel(db.Model):
    __tablename__ = 'master_currency'
    __table_args__ = {"schema": "mgn"}
    master_currency_id = db.Column(db.Integer, primary_key=True)
    currency_code = db.Column(db.String(10), unique=True, nullable=False)
    currency_name = db.Column(db.String(50), nullable=False)
    currency_symbol = db.Column(db.String(30), nullable=False)
    currency_description = db.Column(db.String(100), nullable=False)
    is_active = db.Column(db.SmallInteger, nullable=False)
    created = db.Column(db.DateTime, nullable=True)

    @property
    def id(self):
        return self.master_currency_id

    def __init__(self, currency_code=None, currency_name=None, currency_symbol=None, currency_description=None,
                 is_active=None):
        self.currency_code = currency_code
        self.currency_name = currency_name
        self.currency_symbol = currency_symbol
        self.currency_description = currency_description
        self.is_active = is_active
        self.created = datetime.datetime.utcnow()

    @property
    def serialize(self):
        return {
            'currency_id': self.master_currency_id,
            'currency_code': self.currency_code,
            'currency_name': self.currency_name,
            'currency_symbol': self.currency_symbol,
            'currency_description': self.currency_description,
            'is_active': self.is_active,
            'created': str(self.created)
        }
