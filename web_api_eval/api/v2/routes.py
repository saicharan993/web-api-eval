from flask import Blueprint
from flask import Flask, request, jsonify,Response
import json
import urllib

api_2 = Blueprint('api_2',__name__,url_prefix='/api')

# Get defination of the word
@api_2.route("/dictionary", methods=["GET"])
def get_defination():
    word = request.args.get('word')
    if not word:
        return jsonify({'message': 'Please provide a word by adding to end of url like this ?word=hello'})
    if word:
        url = 'https://api.dictionaryapi.dev/api/v2/entries/en'
        full_url = url + '/' + word
        data = urllib.request.urlopen(full_url)
        return jsonify(json.loads(data.read()))
    
    
    







