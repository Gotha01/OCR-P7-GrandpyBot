# -*- coding: utf-8 -*-
import os.path
from flask import Flask, render_template

TEMPLATE_DIR = os.path.abspath("grandpybot/templates")
STATIC_DIR = os.path.abspath("grandpybot/static")

app = Flask(__name__, static_folder=STATIC_DIR, template_folder=TEMPLATE_DIR)

@app.route('/')
def base():
    return render_template("home.html", title='GrandPyBot', banniere="../static/img/banniere_papy_acceuil.png")