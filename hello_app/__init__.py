from flask import Flask  # Import the Flask class
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)    # Create an instance of the class for our use
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)