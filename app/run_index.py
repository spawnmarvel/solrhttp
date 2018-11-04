import requests
import json


def index_dt_xml():
    headers = { "Content-Type": "text/xml",}
    data = '\n<add>\n  <doc>\n <field name="id">2000</field>\n  <field name="tag">Item-2000</field>\n <field name="desc">Description of 2000</field>\n  <field name="plant">System 2000</field>\n </doc>\n</add>'
    print(data)
    resp = requests.post("http://localhost:8983/solr/newcore/update?commit=true", headers=headers, data=data)
    print(resp)
    # solr config <requestHandler name="/update" class="solr.UpdateRequestHandler" />
    # solr config must have auto commit or use url, else restart to get it to work

def index_dt_test_data():
    headers = { "Content-Type": "text/xml",}
    data = '\n<add>\n'
    with open("testData.txt", "r") as f:
        if f.readable():
            tags = f.read().splitlines()
            if len(tags) != 0:
                for i, x in enumerate(tags):
                    tag = tags[i].split(";")
                    tag_id = tag[0]
                    tag_name = tag[1]
                    tag_desc = tag[2]
                    tag_plant = tag[3]
                    data+= '<doc>\n'
                    data+= ' <field name="id">' + str(tag_id) + '</field>\n'
                    data+= ' <field name="tag">' + str(tag_name) + '</field>\n'
                    data+= ' <field name="desc">' + str(tag_desc) + '</field>\n'
                    data+= ' <field name="plant">' + str(tag_plant) + '</field>\n'
                    data+= '</doc>\n'
            data+= '</add>'
            print(data)
                    
    resp = requests.post("http://localhost:8983/solr/newcore/update?commit=true", headers=headers, data=data)
    print(resp)
    # debug error from solr
    # print(resp.text)

def index_remove_all():
     headers = { "Content-Type": "text/xml",}
     data = "<delete><query>*:*</query></delete>"
     print("Remove all")
     resp = requests.post("http://localhost:8983/solr/newcore/update?commit=true", headers=headers, data=data)
     print(resp)

def index_remove_id(nr):
     headers = { "Content-Type": "text/xml",}
     data = "<delete><query>id:" + str(nr) + "</query></delete>"
     resp = requests.post("http://localhost:8983/solr/newcore/update?commit=true", headers=headers, data=data)
     print(resp)

def main():
    print("Index job")
    # index_dt_xml()
    index_remove_all()
    # index_dt_test_data()







if __name__ == "__main__":
    main()


