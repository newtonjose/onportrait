
class Config(object):
	"""
	Configuration base, for all environments.
	"""
	DEBUG = False
	TESTING = False
<<<<<<< HEAD
	basedir = os.path.abspath(os.path.dirname(__file__))

	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
	SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

=======
>>>>>>> 0cb46b61bb479dc6d1ab8e0b250d1a1904164301
        
class ProductionConfig(Config):
	DATABASE_URI = 'sqlite:///application.db'


class DevelopmentConfig(Config):
	DEBUG = True
