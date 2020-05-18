import os
#from sqlalchemy import create_engine
import pyodbc
import urllib

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
  
    params = urllib.parse.quote_plus(r'Driver={ODBC Driver 17 for SQL Server};Server=tcp:microblog.database.windows.net,1433;Database=microblog;Uid=hellodarkness;Pwd=fidgetCube1;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')    
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
    # for local use
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #    'sqlite:///' + os.path.join(basedir, 'app.db')

    # feature to signal the application every time a change is about to be made in the database.
    SQLALCHEMY_TRACK_MODIFICATIONS = False