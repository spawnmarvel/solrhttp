import requests
import json


def get_all():
    r = requests.get("http://localhost:8983/solr/newcore/select?q=*:*")
    print("Solr status " + str(r.status_code))
    js = r.json()
    print("All")
    for k, v in js.items():
        print(k)
        print(v)

def get_docs_default():
    r = requests.get("http://localhost:8983/solr/newcore/select?q=*:*")
    print("Solr status " + str(r.status_code))
    js = r.json()
    print("Docs")
    li = js["response"]["docs"]
    for l in li:
        print(l)
    return li

def get_docs_max(default=10000):
    r = requests.get("http://localhost:8983/solr/newcore/select?q=*:*&rows=" + str(default))
    print("Solr status " + str(r.status_code))
    js = r.json()
    print("Docs")
    li = js["response"]["docs"]
    for l in li:
        print(l)
    return li

def get_info():
    print("http://lucene.apache.org/solr/guide/7_5/the-standard-query-parser.html")


def main():
    print("Get job")
    # get_all()
    # get_info()
    get_docs_max()


if __name__ == "__main__":
    main()