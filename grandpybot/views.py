#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
from flask import Flask, render_template, request
from flask.json import jsonify

from grandpybot.parser import Parser
from grandpybot.api_requests import Google_maps_search as gms
from grandpybot.api_requests import Wiki_search as ws
from config_user import google_api_key


TEMPLATE_DIR = os.path.abspath("grandpybot/templates")
STATIC_DIR = os.path.abspath("grandpybot/static")

app = Flask(__name__, static_folder=STATIC_DIR, template_folder=TEMPLATE_DIR)

@app.route('/index/')
@app.route('/')
def index():
    return render_template('index.html', gak=google_api_key)


@app.route('/search/', methods=['GET'])
def search():
    if request.method == 'GET':
        user_input = request.args.get('question')
        if user_input not in ("Donnez moi le lieu qui vous interresse", ""):
            clean_input = Parser(user_input).result
            infos = gms(google_api_key).request_google(clean_input)
            pos_story = ws(clean_input).answer
            return jsonify(
                user_input=user_input,
                pos_story=pos_story,
                infos=infos
                )
        else:
            pass