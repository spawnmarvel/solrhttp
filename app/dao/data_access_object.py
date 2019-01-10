import requests

class DataAccess:

    def __init__(self):
        pass

    def search_string(self, user_input, atr_input):
        """Get 10000 rows where atr like input"""
        url = "http://localhost:8983/solr/newcore/select?q=" + atr_input + ":*"+ str(user_input) + "*&rows=10000"
        r = requests.get(url)
        # print("Solr status " + str(r.status_code))
        js = r.json()
        li = js["response"]["docs"]
        return li


    def get_docs_default(self, url_to_use):
        # r = requests.get("http://localhost:8983/solr/newcore/select?q=*:*")
        url_full = url_to_use + "/newcore/select?q=*:*"
        r = requests.get(url_full)
        print("Solr status " + str(r.status_code))
        js = r.json()
        # print("Docs")
        li = js["response"]["docs"]
        # for l in li:
        #    print(l)
        return li

    def get_docs_max(self, url_to_use, default=10000):
        # r = requests.get("http://localhost:8983/solr/newcore/select?q=*:*&rows=" + str(default))
        url_full = url_to_use + "/newcore/select?q=*:*&rows=" + str(default)
        r = requests.get(url_full)
        print("Solr status " + str(r.status_code))
        js = r.json()
        # print("Docs")
        li = js["response"]["docs"]
        # for l in li:
        #    print(l)
        return li