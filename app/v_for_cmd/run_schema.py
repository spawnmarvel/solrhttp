import requests
import json

def get_fields():
    r = requests.get("http://localhost:8983/solr/newcore/schema/fields")
    print("Solr status " + str(r.status_code))
    js = r.json()
    for l in js["fields"]:
        for k, v in l.items():
            if k == "name":
                print(v)  
def get_dict():
    r = requests.get("http://localhost:8983/solr/newcore/schema/fields")
    print("Solr status " + str(r.status_code))
    js = r.json()
    print("Dict")
    for k, v in js.items():
        print(k)
        print(v)

def alter_schema():
    pass

def main():
    print("Schema job")
    get_dict()
    get_fields()
  


if __name__ == "__main__":
    main()