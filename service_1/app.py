
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    species = requests.get('http://service-2:5000/get/species').text
    occupation = requests.get('http://service-3:5000/get/occupation').text

    powers = {'species': species, 'occupation': occupation}
    power_level = requests.post('http://service-4:5000/post/power', json=powers).json() 

    return f"A {species} {occupation} has a power level of {power_level}.\n"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')