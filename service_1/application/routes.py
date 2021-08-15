from . import app, db
from .models import Powerscale
import requests
from flask import redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

@app.route('/', methods=['GET','POST'])
def home():
    species = requests.get('http://service-2:5000/get/occupation').json()
    occupation = requests.get('http://service-3:5000/get/species').json()
    data = [species, occupation]
    raise ValueError(power_level = requests.post('http://service-4:5000/post/power', json=data).json())

    history = Powerscale.query.order_by(Powerscale.id.desc()).limit(10).all()
    result = Powerscale(power_level=power_level, species=species, occupation=occupation)
    db.session.add(result)
    db.session.commit()

    return render_template('home.html', occupation=data[0], species=data[1], power_level=power_level, history=history)

    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)