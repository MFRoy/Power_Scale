from flask import Flask
import random

app = Flask(__name__)

occupation = ['Bounty Hunter', 'Sith Lord', 'Jedi', 'Crime Lord', 'Politician']

@app.route('/get/occupation')
def get_occupation():
    return random.choice(occupation)

if __name__ == '__main__':
    app.run(host='0.0.0.0')