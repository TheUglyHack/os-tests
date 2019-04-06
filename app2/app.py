#!/usr/bin/python
from flask import Flask,make_response, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "app2\n"

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)

