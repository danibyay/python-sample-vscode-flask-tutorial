from flask import Flask  # Import the Flask class
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)    # Create an instance of the class for our use
app.config.from_object(Config)
engine_azure = create_engine(app.config['SQLALCHEMY_DATABASE_URI'],echo=True)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'