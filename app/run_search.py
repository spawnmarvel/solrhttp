import requests
# http://lucene.apache.org/solr/guide/7_5/the-standard-query-parser.html

def get_id():
    r = requests.get("http://localhost:8983/solr/newcore/select?q=id:1")
    print("Solr status " + str(r.status_code))
    js = r.json()
    print(js)

def get_id_range():
    r = requests.get("http://localhost:8983/solr/newcore/select?q=id:[9980 TO 9982]")
    print("Solr status " + str(r.status_code))
    js = r.json()
    for l in js["response"]["docs"]:
        print(l)

def get_string():
    r = requests.get("http://localhost:8983/solr/newcore/select?q=desc:*Gas*&rows=2000")
    print("Solr status " + str(r.status_code))
    js = r.json()
    for l in js["response"]["docs"]:
        print(l)


def main():
    # get_id()
    # get_id_range()
    get_string()
if __name__ == "__main__":
    main()