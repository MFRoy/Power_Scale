from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config.update(
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@34.89.1.172/power_scale",
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
    SECRET_KEY=str(os.urandom(16))
)

db = SQLAlchemy(app)

from . import routes