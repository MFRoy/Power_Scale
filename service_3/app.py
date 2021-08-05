from flask import Flask
import random

app = Flask(__name__)

species = ['Jawa', 'Bith', 'Human', 'Hutt', 'Gungan', 'Droid', 'Muun']

@app.route('/get/species')
def get_species():
    return random.choice(species)

if __name__ == '__main__':
    app.run(host='0.0.0.0')