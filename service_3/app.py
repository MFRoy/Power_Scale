from flask import Flask, jsonify
import random

app = Flask(__name__)

species = ['Wookie', 'Bith', 'Human', 'Hutt', 'Gungan', 'Droid', 'Muun', 'Dug', 'kaminoan', 'Ugnaught']

@app.route('/get/species')
def get_species():
    return jsonify(random.choice(species))

if __name__ == '__main__':
    app.run(host='0.0.0.0')