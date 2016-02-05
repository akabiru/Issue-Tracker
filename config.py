import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    '''This base class contains configuration
    that is common in all environments
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dolor ipsum Lorem'

    @staticmethod
    def init_app(app):
        pass


class DevelopementConfig(Config):
    '''This class configures the development
    environment properties
    '''
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, 'data-dev.sqlite')


class ProductionConfig(Config):
    '''This class cofigures the production
    environment properties
    '''
    PORT = int(os.environ.get("PORT", 5000))
    HOST = '0.0.0.0'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopementConfig,
    'production': ProductionConfig,
    'default': DevelopementConfig
}
