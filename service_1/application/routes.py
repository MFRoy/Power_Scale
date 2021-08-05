from . import app, db
from .models import Powerscale
from flask import redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

@app.route("/")
def home():
    
    return render_template("home.html")