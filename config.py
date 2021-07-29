import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ['SECRET_KEY'] or 'harus diubah'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # Email Config
    MAIL_SERVER = os.environ['MAIL_SERVER']
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
        ['true', 'on', '1']
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USERNAME = os.environ['MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
    ABSEN_ADMIN = os.environ['FLASKY_ADMIN']

    # BCRYPT_LOG_ROUNDS = 15

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing' : TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}