from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


db = SQLAlchemy()
db.init_app(app)

from . import views, models



