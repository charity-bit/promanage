import os
class Config:
    SECRET_KEY = "4545"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:jimi@localhost/promanage'

class ProdConfig(Config):

    pass

class DevConfig(Config):

    DEBUG = True

config_options = {
    'production': ProdConfig,
    'development': DevConfig
}
