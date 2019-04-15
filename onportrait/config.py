class Config(object):
    """
	Configuration base, for all environments.
	"""
<<<<<<< HEAD
    DEBUG = False
    TESTING = False


=======
	DEBUG = False
	TESTING = False
<<<<<<< HEAD
<<<<<<< HEAD
	basedir = os.path.abspath(os.path.dirname(__file__))

	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
	SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

=======
>>>>>>> 0cb46b61bb479dc6d1ab8e0b250d1a1904164301
=======
>>>>>>> 0cb46b61bb479dc6d1ab8e0b250d1a1904164301
        
>>>>>>> 5f184732a892ad5df64615c4216930d8f3abdc11
class ProductionConfig(Config):
    DATABASE_URI = 'sqlite:///application.db'



class DevelopmentConfig(Config):
    DEBUG = True