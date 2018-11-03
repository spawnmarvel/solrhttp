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

def get_docs():
    r = requests.get("http://localhost:8983/solr/newcore/select?q=*:*")
    print("Solr status " + str(r.status_code))
    js = r.json()
    print("Docs")
    for l in js["response"]["docs"]:
        print(l)

def get_fields():
    r = requests.get("http://localhost:8983/solr/newcore/schema/fields")
    print("Solr status " + str(r.status_code))
    js = r.json()
    print(js)
    print("Fields")
    for k, v in js.items():
        print(k)
        print(v)
    for l in js["fields"]:
        for k, v in l.items():
            if k == "name":
                print(v)     
   

def get_info():
    print("http://lucene.apache.org/solr/guide/7_5/the-standard-query-parser.html")

def generate_test_data():
    with open("testData.txt", "w") as f:
        for x in range(0,2000):
            obj = "" + str(x) + ";" + "Item" + str(x) + ";" + str("Description of " + str(x) + "\n")
            f.write(obj)

def main():
    print("Get job")
    # get_all()
    # get_info()
    get_fields()
    # get_docs()
    # generate_test_data()


if __name__ == "__main__":
    main()