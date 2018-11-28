from flask import Flask, render_template, request
from . import get
import run_get
from home import views

@get.route("/get", methods=["GET", "POST"])
def index():
    data = ""
    local_url = views.get_url_select()
    req = "GET"
    if request.method == "POST":
        req = "POST"
        if request.form["action"] == "GetDefault":
            try:
                data = run_get.get_docs_default(local_url)
            except Exception as e:
                data = ["error", str(e)]
        if request.form["action"] == "GetMax":
            try:
                data = run_get.get_docs_max()
            except Exception as e:
                data = ["error", str(e)]
       
    #GET
    return render_template("get.html", data=data, req=req, local_url=local_url)