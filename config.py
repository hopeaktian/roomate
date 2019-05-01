class Config(object):
    SECRET_KEY = ''

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:yourpassword@IP:3306/database_name"
