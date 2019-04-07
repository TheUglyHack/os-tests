#!/usr/bin/python
from flask import Flask,make_response, jsonify
from flask_oidc import OpenIDConnect

app = Flask(__name__)
oidc = OpenIDConnect(app)

@app.route('/')
def index():
    if oidc.user_loggedin:
        return "app1: Welcome {}\n".format(oidc.user_getfield('email'))
    else:
        return "app1: not logged in\n"


@app.route('/login')
@oidc.require_login
def login():
    return "app1: Welcome %s\n" % oidc.user_getfield('email')


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

