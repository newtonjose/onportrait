
class Config(object):
	"""
	Configuration base, for all environments.
	"""
	DEBUG = False
	TESTING = False
        basedir = os.path.abspath(os.path.dirname(__file__))

        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
        SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

        
class ProductionConfig(Config):
	DATABASE_URI = 'sqlite:///application.db'

class DevelopmentConfig(Config):
	DEBUG = True

class TestingConfig(Config):
	TESTING = True
