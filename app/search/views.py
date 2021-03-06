from flask import Flask, render_template, request
import json
from home import views
from . import search
from app.dao import data_access_object


@search.route("/search_str", methods=["GET", "POST"])
def search_str():
    rv = ""
    param = ""
    data = ""
    req = "GET"
    local_url_selected = views.get_url_select()
    if request.method == "POST":
        print("post")
        req = "POST"
        if request.form["action"] == "Search":
            user_input = request.form["user_input"]
            rv = user_input
            param = request.form["options"]

            if len(rv) < 2:
                data = ["Msg", "Blank input"]
            else:
                try:
                    data = data_access_object.DataAccess().search_string(rv, param)
                except Exception as e:
                    data = ["error", str(e)]
    #GET
    return render_template("search.html", rv=rv,req=req,param=param, local_url_selected=local_url_selected, data=data)