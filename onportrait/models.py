from onportrait import db


class Portrait(db.Model):
    __tablename__ = 'portrait'
    id = db.Column(db.Integer(), primary_key=True)
    social_media = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))

    def __init__(self, id):
        self.id = id
