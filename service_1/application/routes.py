from . import app, db
from .models import Powerscale
import requests
from flask import redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

@app.route('/', methods=['GET','POST'])
def home():
    # species = requests.get('http://service-2:5000/get/occupation').text
    # occupation = requests.get('http://service-3:5000/get/species').text
    # data = [species, occupation]
    data = [requests.get('http://service-2:5000/get/occupation').json(), requests.get('http://service-3:5000/get/species').json()]
    power_level = requests.post('http://service-4:5000/post/power', json=data).json()
    

    return render_template('home.html', occupation=data[0], species=data[1], power_level=power_level)

    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)