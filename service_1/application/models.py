from . import db

class Powerscale(db.Model):
    id = db.Column(db.Integer, primaey_key=True)
    species = db.Column(db.String(20))
    occupation = db.Column(db.String(20))
    power = db.Column(db.Integer)