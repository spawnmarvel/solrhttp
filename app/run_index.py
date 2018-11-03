import requests
import json


def index_dt_xml():
    headers = { "Content-Type": "text/xml",}
    data = '\n<add>\n  <doc>\n <field name="id">118</field>\n  <field name="tag">Test9</field>\n <field name="desc">Nith test tag</field>\n </doc>\n</add>'
    resp = requests.post("http://localhost:8983/solr/newcore/update?commit=true", headers=headers, data=data)
    print(resp)
    # solr config <requestHandler name="/update" class="solr.UpdateRequestHandler" />
    # solr config must have auto commit or use url, else restart to get it to work

def index_dt_test_data():
    headers = { "Content-Type": "text/xml",}
    # with open("testData.txt", "r"):
    data = '\n<add>\n  <doc>\n'
    data+= '<field name="id">1</field>\n'
    data+= '<field name="tag">Test9</field>\n'
    data+= '<field name="desc">Nith test tag</field>\n'
    data+= '</doc>\n</add>'
    resp = requests.post("http://localhost:8983/solr/newcore/update?commit=true", headers=headers, data=data)
    print(resp)


def index_remove_all():
     headers = { "Content-Type": "text/xml",}
     data = "<delete><query>*:*</query></delete>"
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
    # index_remove_all()
    index_dt_test_data()






if __name__ == "__main__":
    main()


