from flask import Flask, render_template, request
import run_get
app = Flask(__name__)

from .home import home as home_blueprint
app.register_blueprint(home_blueprint)

from .get import get as get_blueprint
app.register_blueprint(get_blueprint)

from .search import search as search_blueprint
app.register_blueprint(search_blueprint)

