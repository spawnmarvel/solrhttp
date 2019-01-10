from flask import Flask, render_template, request
from . import get
from home import views
from app.dao import data_access_object

@get.route("/get", methods=["GET", "POST"])
def index():
    data = ""
    local_url = views.get_url_select()
    req = "GET"
    if request.method == "POST":
        req = "POST"
        if request.form["action"] == "GetDefault":
            try:
                data = data_access_object.DataAccess().get_docs_default(local_url)
                # data = run_get.get_docs_default("http://localhost:8993/solr")
            except Exception as e:
                data = ["error", str(e)]
        if request.form["action"] == "GetMax":
            try:
                data = data_access_object.DataAccess().get_docs_max(local_url)
            except Exception as e:
                data = ["error", str(e)]
       
    #GET
    return render_template("get.html", data=data, req=req, local_url=local_url)