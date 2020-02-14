from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Heroku + Python Flask API'


@app.route('/summarize', methods=['POST'])
def summarize():
    data= request.get_json()
    number_of_sentences = data['number_of_sentences']
    paragraph = data['paragraph']
    
    return  paragraph


