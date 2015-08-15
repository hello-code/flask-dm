import os

DEBUG = True
SECRET_KEY = 'DEV KEY'
SITE_PATH = os.path.dirname(os.path.abspath(__file__))  # flask-dm
# SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
# SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(SITE_PATH, "mydb.db")
SQLALCHEMY_DATABASE_URI = "postgresql://z:123@localhost/mydb"
SQLALCHEMY_ECHO = True
