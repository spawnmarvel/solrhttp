import json
def get_url_select():
    msg = ""
    url = ""
    cur = ""
    try:
        with open("index.json") as j:
            js = json.load(j)
            tmp_url = js["urls"]
            tmp_current = js["current"]
            print(tmp_current)
            for u, p in zip(tmp_url, tmp_current):
                if p == 1:
                    cur = u
                    msg = cur
    except Exception as ex:
        msg = ex
    return msg

print(get_url_select())


def prepare_urls():
    js = ""
    try:
        with open("index.json") as j:
            js = json.load(j)
            js = js["urls"]
            print(js)
    except Exception as ex:
        js = ex
    return js

prepare_urls()
