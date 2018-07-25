# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)
app.secret_key="Gabriel"
from app import views
