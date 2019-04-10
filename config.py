ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = './files/uploads'

class BaseCongig(object):
    DEBUG = True
    TESTING = False


class ProductionConfig(BaseCongig):
    """
    Production specific config
    """
    DEBUG = False


class DevelopmentConfig(BaseCongig):
    """
    Development environment specific configuration
    """
    TESTING = True
