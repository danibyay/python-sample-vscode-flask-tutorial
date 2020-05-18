# Entry point for the application.
from . import app    # For application discovery by the 'flask' command. 
from . import views  # For import side-effects of setting up routes. 
from . import models
from . import db

# Time-saver: output a URL to the VS Code terminal so you can easily Ctrl+click to open a browser
# print('http://127.0.0.1:5000/hello/VSCode')

from .models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}