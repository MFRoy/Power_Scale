from flask import Flask, jsonify
import random

app = Flask(__name__)

species = ['Wookie', 'Zabrak', 'Lasat', 'Ewok']

@app.route('/get/species')
def get_species():
    return jsonify(random.choice(species))

if __name__ == '__main__':
    app.run(host='0.0.0.0')