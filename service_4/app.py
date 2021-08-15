from flask import Flask, request, jsonify

app = Flask(__name__)

power = {
    'species': {
        'Wookie':5,
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
        'Bounty Hunter':30,
        'Sith Lord':50,
        'Jedi':50,
        'Crime Lord': 40,
        'Politician': 15,
        'Medic':25
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