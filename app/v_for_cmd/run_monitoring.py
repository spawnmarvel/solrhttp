import requests
import json
import datetime
import random

def get_dict():
    r = requests.get("http://localhost:8983/solr/newcore/replication?command=details")
    print("Solr status " + str(r.status_code))
    js = r.json()
    print("Dict")
    for k, v in js.items():
        print(k)
        print(v)

def status_core():
    r = requests.get("http://localhost:8983/solr/newcore/replication?command=details")
    print("Status: " + str(r.status_code))
    js = r.json()
    print("Index sixe: " + format(js["details"]["indexSize"]))
    print("Path: " + format(js["details"]["indexPath"]))
    print("Master: " + format(js["details"]["isMaster"]))
    try:
        bck = js["details"]["backup"]
        print("Backup information: Name " + str(bck[9]))
    except KeyError as ke:
        print("No backup avaliable for current index")

def generate_bck(name):
    if len(name) < 3:
        name = "bck_"+ str(datetime.datetime.now().date()) + "_1"
    r = requests.get("http://localhost:8983/solr/newcore/replication?command=backup&name=" + str(name))
    print("Status: " + str(r.status_code))



def main():
    print("Monitoring job")
    get_dict()
    status_core()
    # generate_bck("nu")

if __name__ == "__main__":
    main()