from flask import Flask, request, jsonify

app = Flask(__name__)

power = {
    'species': {
        'Jawa':5,
        'Bith':50,
        'Human':30,
        'Hutt':45,
        'Gungan':25,
        'Droid':20,
        'Muun':50,
        'Dug':20,
        'kaminoan':40,
        'Ugnaught':20
    },
    'occupation': {
        'Assasin':30,
        'Commander':50,
        'Pilot':50,
        'Farmer': 40,
        'Civilian': 15,
        'Banker':25
    }
}

@app.route('/post/power', methods=['POST'])
def post_power():
    occupation = request.json[0]
    species = request.json[1]
    power_level = power['species'][species] + power['occupation'][occupation]
    return jsonify(power_level)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)