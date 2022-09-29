#import flask and routes
from distutils.log import debug
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#the routes module is imported at the bottom to avoid circular imports
from app import routes, models
