from flask import Flask  # Import the Flask class
from .config import Config

app = Flask(__name__)    # Create an instance of the class for our use
app.config.from_object(Config)