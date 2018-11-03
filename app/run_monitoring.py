import requests
import json
import datetime

def test():
    r = requests.get("http://localhost:8983/solr/newcore/replication?command=details")
    print("Solr status " + str(r.status_code))
    js = r.json()
    for k, v in js.items():
        print(k)
        print(v)

def status():
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
        print("No backup avaliable")

def generate_bck(name):
    if len(name) < 3:
        name = "bck"+ str(datetime.datetime.now())
    r = requests.get("http://localhost:8983/solr/newcore/replication?command=backup&name=" + str(name))
    print("Status: " + str(r.status_code))



def main():
    print("Monitoring job")
    status()
    # generate_bck("test")

if __name__ == "__main__":
    main()