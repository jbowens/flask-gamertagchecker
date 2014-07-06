from flask import render_template, g, current_app, request
from app.blueprints.main import main
from app.api.xboxliveapi import XboxLiveApi

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and request.form.get('gamertag'):
        # Try and validate the gamertag
        gamertag = request.form.get('gamertag')
        api = XboxLiveApi()
        taken = api.is_gamertag_taken(gamertag)
        return render_template('index.html', gamertag=gamertag, taken=taken)
    return render_template('index.html')
