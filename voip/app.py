import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)


db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)

from . import views, models
    





