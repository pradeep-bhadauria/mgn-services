from mgn import db


class MasterGenderModel(db.Model):
    __tablename__ = 'master_gender'
    __table_args__ = {"schema": "mgn"}
    master_gender_id = db.Column(db.SmallInteger, primary_key=True)
    gender = db.Column(db.String(10), unique=True)

    @property
    def id(self):
        return self.master_gender_id

    def __init__(self, gender=None):
        self.gender = gender

    @property
    def serialize(self):
        return {
            'master_gender_id': self.master_gender_id,
            'gender': self.gender
        }
