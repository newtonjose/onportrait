from onportrait import db


class Portrait(db.Model):
    __tablename__ = 'portrait'
    id = db.Column(db.Integer(), primary_key=True)
    social_media = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))

    def __repr__(self):
        return '<Portrait {} {} {}>'.format(self.id, self.social_media,
                                            self.name)

    @staticmethod
    def add(*args, **kwargs):
        new_portrait = Portrait(*args, **kwargs)

        print(new_portrait)
        db.session.add(new_portrait)
        db.session.commit()

        return new_portrait
