import json
from onportrait import db


class Portrait(db.Model):
    __tablename__ = 'portrait'
    id = db.Column(db.Integer(), primary_key=True)
    social_media = db.Column(db.String(65))  # is social_media unique
    file_name = db.Column(db.String(255))
    name = db.Column(db.String(255))
    # TODO: save image as binary
    _faces_coods = db.Column(db.String)

    def __repr__(self):
        self.faces_coods(self.faces_coods)
        return '<Portrait {} {} {}>'.format(self.file_name,
                                            self.social_media,
                                            self.name)

    @staticmethod
    def add(*args, **kwargs):
        new_portrait = Portrait(*args, **kwargs)
        db.session.add(new_portrait)
        db.session.commit()

        return new_portrait

    @staticmethod
    def update(id, name, social_media):
        image = Portrait.query.get(id)

        image.name = name
        image.social_media = social_media
        db.session.commit()

        return image

    @property
    def faces_coods(self):
        return json.loads(self._faces_coods)

    @faces_coods.setter
    def faces_coods(self, faces):
        self._faces_coods = json.dumps(faces)
