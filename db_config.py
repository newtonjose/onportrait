import os
from onportrait import app, db


def createdb():
    """
    initi database and migration information
    """
    # Local database only to test
    SQLALCHEMY_DATABASE_URI = 'sqlite:////usr/src/app/application.db' #app.config['SQLALCHEMY_DATABASE_URI']

    if SQLALCHEMY_DATABASE_URI.startswith('sqlite:///'):
        path = os.path.dirname(os.path.realpath
                               (SQLALCHEMY_DATABASE_URI.replace(
                                   'sqlite:///', '')))

        
        if not os.path.exists(path):
            os.makedirs(path)

    db.create_all(app=app)


if __name__ == "__main__":
    createdb()
