from flask import Flask, jsonify
import random

app = Flask(__name__)

occupation = ['Storm Trooper', 'Assasin', 'Pilot', 'Farmer']

@app.route('/get/occupation')
def get_occupation():
    return jsonify(random.choice(occupation).strip())

if __name__ == '__main__':
    app.run(host='0.0.0.0')