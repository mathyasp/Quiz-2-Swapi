import json
import requests
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def homepage():
    """Homepage link"""
    return render_template('base.html')


@app.route('/characterSelect')
def characterSelect():
    """Character Select"""
    return render_template('form.html')


@app.route('/results', methods=['GET'])
def results():
    """ Connect to SWAPI and return results """
    api_url = 'https://swapi.py4e.com/api/'
    character_id = request.args.get('character_id')
    response = requests.get(api_url + 'people/' + character_id)
    character = json.loads(response.content)

    character_attributes = [
        {'Name': character['name']}, 
        {'Height:': character['height']}, 
        {'Mass': character['mass']}, 
        {'Hair Color': character['hair_color']}, 
        {'Eye Color': character['eye_color']},
    ]

    context = {
        'character': character,
        'character_attributes': character_attributes,
    }
    return render_template("results.html", **context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)