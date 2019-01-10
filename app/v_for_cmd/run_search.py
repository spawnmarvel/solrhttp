import requests
# http://lucene.apache.org/solr/guide/7_5/the-standard-query-parser.html


def get_string_solr(user_input):
    """Get 7 rows where desc has Gas"""
    url = "http://localhost:8983/solr/newcore/select?q=desc:*"+ str(user_input) + "*&rows=7"
    print(url)
    # r = requests.get("http://localhost:8983/solr/newcore/select?q=desc:*Gas*&rows=7")
    r = requests.get(url)
    print("Solr status " + str(r.status_code))
    js = r.json()
    for l in js["response"]["docs"]:
        # print(l)
        pass
    li = js["response"]["docs"]
    return li


def get_id():
    """Get id"""
    r = requests.get("http://localhost:8983/solr/newcore/select?q=id:1")
    print("Solr status " + str(r.status_code))
    js = r.json()
    print(js)

def get_id_range():
    """Get range"""
    r = requests.get("http://localhost:8983/solr/newcore/select?q=id:[9980 TO 9982]")
    print("Solr status " + str(r.status_code))
    js = r.json()
    for l in js["response"]["docs"]:
        print(l)

def get_string():
    """Get 7 rows where desc has Gas"""
    r = requests.get("http://localhost:8983/solr/newcore/select?q=desc:*Gas*&rows=7")
    print("Solr status " + str(r.status_code))
    js = r.json()
    for l in js["response"]["docs"]:
        print(l)

def get_string_sort():
    """Get default rows, sort by id desc """
    r = requests.get("http://localhost:8983/solr/newcore/select?q=*:*&sort=id desc")
    print("Solr status " + str(r.status_code))
    js = r.json()
    for l in js["response"]["docs"]:
        print(l)

def get_string_sort_desc():
    """Get 3 rows where desc start with Oil, sort by id asc"""
    r = requests.get("http://localhost:8983/solr/newcore/select?q=desc:Oil*&sort=id asc&rows=3")
    print("Solr status " + str(r.status_code))
    js = r.json()
    for l in js["response"]["docs"]:
        print(l)

def get_name_sort_desc_():
    """Get 3 rows, just name and id, sort by id asc"""
    r = requests.get("http://localhost:8983/solr/newcore/select?fl=tag id&q=*:*&rows=3&sort=id desc")
    print("Solr status " + str(r.status_code))
    js = r.json()
    for l in js["response"]["docs"]:
        print(l)



def main():
    # get_id()
    # get_id_range()
    # get_string_sort()
    # get_string_sort_desc()
    get_name_sort_desc_()
   
if __name__ == "__main__":
    main()