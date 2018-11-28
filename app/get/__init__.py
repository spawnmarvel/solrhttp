""" ___ """

from flask import Blueprint

get = Blueprint("get", __name__)

from . import views