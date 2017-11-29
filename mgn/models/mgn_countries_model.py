from mgn import db
from sqlalchemy.dialects.postgresql import JSONB


class MgnCountriesModel(db.Model):
    __tablename__ = 'mgn_countries'
    __table_args__ = {"schema": "mgn"}
    country_id = db.Column(db.SmallInteger, primary_key=True)
    short_name = db.Column(db.String(3), unique=True)
    full_name = db.Column(db.String(50))
    isd_code = db.Column(db.String(10))
    states = db.Column(JSONB)
    cities = db.Column(JSONB)
    is_active = db.Column(db.SmallInteger, nullable=True)

    def __init__(self, country_id=None, short_name=None, full_name=None, isd_code=None, states=None, cities=None,
                 is_active=None):
        self.country_id = country_id
        self.short_name = short_name
        self.full_name = full_name
        self.isd_code = isd_code
        self.states = states
        self.cities = cities
        self.is_active = is_active

    @property
    def id(self):
        return self.country_id

    @property
    def serialize(self):
        return {
            'country_id': self.country_id,
            'short_name': self.short_name,
            'full_name': self.full_name,
            'isd_code': self.isd_code,
            'states': self.states,
            'cities': self.cities,
            'is_active': self.is_active
        }
