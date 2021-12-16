# -*- coding: utf-8 -*-
import os.path
from flask import Flask, render_template

import config_user as cu

TEMPLATE_DIR = os.path.abspath("grandpybot/templates")
STATIC_DIR = os.path.abspath("grandpybot/static")

app = Flask(__name__, static_folder=STATIC_DIR, template_folder=TEMPLATE_DIR)

@app.route('/')
def base():
    return render_template("layout.html", a = cu.a)