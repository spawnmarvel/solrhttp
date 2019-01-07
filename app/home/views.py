from flask import Flask, render_template, request
import json

from . import home

@home.route("/", methods=["GET", "POST"])
def index():
    data = ""
    local_urls = prepare_urls()
    print(local_urls)
    local_url_selected = get_url_select()
    print(local_url_selected)
    req = "GET"
    if request.method == "POST":
        req = "POST"
        if request.form["action"] == "Set":
            local_url_selected = request.form["SelectUrl"]
            set_url_selected(local_url_selected)
    #GET
    return render_template("index.html", data=data, req=req, local_urls=local_urls, local_url_selected=local_url_selected)

@home.route("/about")
def about():
    return render_template("about.html")

def set_url_selected(new_url):
    try:
        with open("index.json") as j:
            js = json.load(j)
            tmp_url = js["urls"]
            tmp_current = js["current"]
            dic = {"urls": tmp_url, "current": tmp_current}
            print("\n")
            print(new_url)
            print(dic)
            for u, p in zip(tmp_url, tmp_current):
                if u == new_url:
                    print("yes")
                    dic["current"][p] = 1
            print(dic)
            #https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
    except Exception as ex:
        print(ex)
    return ""


def get_url_select():
    msg = ""
    url = ""
    cur = ""
    try:
        with open("index.json") as j:
            js = json.load(j)
            tmp_url = js["urls"]
            tmp_current = js["current"]
            for u, p in zip(tmp_url, tmp_current):
                if p == 1:
                    cur = u
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



