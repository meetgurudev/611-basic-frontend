from importlib.metadata import requires
from flask import request, jsonify
from app.service.welcome import Welcome
from app import app

@app.route('/')
def index():
    return Welcome.welcome_user(request.json)

@app.route('/hi')
def index2():
    print(request.params)
    return Welcome.welcome_user(request.json)