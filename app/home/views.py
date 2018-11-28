from flask import Flask, render_template, request
import json

from . import home

@home.route("/", methods=["GET", "POST"])
def index():
    data = ""
    local_urls = prepare_urls()
    local_url_selected = get_url_select()
    req = "GET"
    if request.method == "POST":
        req = "POST"
        if request.form["action"] == "Set":
            local_url_selected = request.form["SelectUrl"]
            set_url_selected()
    #GET
    return render_template("index.html", data=data, req=req, local_urls=local_urls, local_url_selected=local_url_selected)


def set_url_selected():
    pass
def get_url_select():
    msg = ""
    url = ""
    cur = ""
    try:
        with open("index.json") as j:
            js = json.load(j)
            tmp_url = js["urls"]
            tmp_current = js["current"]
            for x in tmp_current:
                if x == 1:
                    cur = tmp_url[x]
                    msg = cur
    except Exception as ex:
        msg = ex
    return msg

def prepare_urls():
    js = ""
    try:
        with open("index.json") as j:
            js = json.load(j)
            js = js["urls"]
    except Exception as ex:
        js = ex
    return js