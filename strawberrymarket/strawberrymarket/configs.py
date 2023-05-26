import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost:3307/strawberrymarket?charset=utf8'
    JWT_SECRET_KEY = 'super-jwt-secret-key'
    UPLOAD_FOLDER = os.path.abspath('app/static/')