# from flask_mysqldb import MySQL

# def init_mysql(app):
#     app.config['MYSQL_HOST'] = 'localhost'
#     app.config['MYSQL_USER'] = 'root'
#     app.config['MYSQL_PASSWORD'] = 'Root@123'
#     app.config['MYSQL_DB'] = 'ems'
#     return MySQL(app)

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DB')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
