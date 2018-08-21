import os


class Config(object):
    """
    Common configurations
    """

    DEBUG = False
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEVELOPMENT = True
    DEBUG = True

    SQLALCHEMY_ECHO = False

    DB_NAME = 'dev.db'

    DB_PATH = os.path.join(Config.BASE_DIR, DB_NAME)

    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)


class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')



class HerokuConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    """
    Testing configurations
    """
    TESTING = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'heroku': HerokuConfig,
    'testing': TestingConfig
}
