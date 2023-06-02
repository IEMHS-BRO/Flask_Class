import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/strawberrymarket?charset=utf8'
    JWT_SECRET_KEY = 'super-jwt-secret-key'
    UPLOAD_FOLDER = os.path.abspath('app/static/')

    def __init__(self):
        db_env = os.environ.get('SQLALCHEMY_DATABASE_URI')
        if db_env:
            self.SQLALCHEMY_DATABASE_URI = db_env