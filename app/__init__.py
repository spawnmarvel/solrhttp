from flask import Flask, render_template, request
import run_get
app = Flask(__name__)

from .home import home as home_blueprint
app.register_blueprint(home_blueprint)

