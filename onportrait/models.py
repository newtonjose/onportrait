from onportrait import db


class Portrait(db.Model):
    __tablename__ = 'portrait'
    id = db.Column(db.Integer(), primary_key=True)
    social_media = db.Column(db.String(65))  # is social_media unique
    file_name = db.Column(db.String(255))
    name = db.Column(db.String(255))

    def __repr__(self):
        return '<Portrait {} {} {}>'.format(self.file_name,
                                            self.social_media, self.name)

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
