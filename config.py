import os
from dotenv import dotenv_values


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'harusdiubah'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # Email Config
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
        ['true', 'on', '1']
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ABSEN_MAIL_SUBJECT_PREFIX ='[ABSENAPP]'
    ABSEN_MAIL_SENDER = 'AbsenApp Admin'
    ABSEN_ADMIN = os.environ.get('ABSEN_ADMIN')

    # BCRYPT_LOG_ROUNDS = 15

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'postgresql://petro:udin4j4@172.18.0.4/absendev'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://petro:udin4j4@172.18.0.4/absen'


config = {
    **dotenv_values(".flaskenv"),
    **os.environ,
    'development': DevelopmentConfig,
    'testing' : TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
