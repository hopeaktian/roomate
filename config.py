class Config(object):
    SECRET_KEY = '7a71ea10c4af9f16f020488e115b32fd'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:yourpassword@120.79.139.82:3306/flask_learn01"
