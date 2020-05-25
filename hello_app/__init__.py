from flask import Flask  # Import the Flask class
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_migrate import Migrate
from flask_login import LoginManager
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


app = Flask(__name__)    # Create an instance of the class for our use
app.config.from_object(Config)
engine_azure = create_engine(app.config['SQLALCHEMY_DATABASE_URI'],echo=True)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
# Azure Blob Storage
az_connect_str = "DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName=domingostorage9898;AccountKey=RfznV6ibGv9eX9Y6ImQAXzmRID5UCgiAY9I15YH2PPII9ZQABDwGh7ElHnTFIZzcXU2Q4O6DjPJQOLwU6ARncg=="
#os.getenv('AZURE_STORAGE_CONNECTION_STRING')
blob_service_client = BlobServiceClient.from_connection_string(az_connect_str)
container_name = "domingocontainer9898"
container_client = blob_service_client.get_container_client(container_name)

# this would be in views.py
#blob_client = blob_service_client.get_blob_client(container=container_name, blob=unique_name_for_each_image)
#with open(upload_file_path, "rb") as data:
#            blob_client.upload_blob(data)
