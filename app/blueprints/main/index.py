from flask import render_template, g, current_app
from app.blueprints.main import main

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')
