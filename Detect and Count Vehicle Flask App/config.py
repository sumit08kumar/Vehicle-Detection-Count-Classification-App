class Config(object):

    SECRET_KEY = 'Sumit@123'

    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None

class DevelopmentConfig(Config):
    DEBUG = True
