from mgn import db


class User(db.Model):
    __tablename__ = 'test'
    __table_args__ = {"schema": "test"}
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(45), unique=True)
    desc = db.Column(db.String(100))
    updated = db.Column(db.DateTime, nullable=True)

    def __init__(self, id=None, name=None, desc=None, updated=None):
        self.id = id
        self.desc = desc
        self.name = name
        self.updated = updated

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'desc': self.desc,
            'updated': str(self.updated)
        }
