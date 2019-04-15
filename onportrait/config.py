class Config(object):
    """
	Configuration base, for all environments.
	"""
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    DATABASE_URI = 'sqlite:///application.db'


class DevelopmentConfig(Config):
    DEBUG = True