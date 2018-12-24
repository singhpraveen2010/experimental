import requests
import json


def call_db(str_gremlin_dsl):
    #url = "http://localhost:8182"
    payload = {'gremlin': str_gremlin_dsl}
    response = requests.post(url, data=json.dumps(payload))
    json_response = response.json()
    return json_response


def test_insert_pck():
    print "\n 1. Add a package vertex"
    str_gremlin_dsl = 'tx = graph.newTransaction(); p = tx.addVertex(T.label, "Package", "pid", "test123", "name", "testPackage", "ecosystem", "testEcosystem"); tx.commit()'
    json_response = call_db(str_gremlin_dsl)
    assert(json_response["result"]["data"][0]==None)
    assert(json_response["status"]["code"]==200)


def test_get_pck():
    print "2. Fetch a package vertex"
    str_gremlin_dsl = 'g.V().has("pid","test123")'
    json_response = call_db(str_gremlin_dsl)
    j = json_response["result"]["data"][0]["properties"]
    assert(j["ecosystem"][0]["value"]=="testEcosystem")
    assert(j["name"][0]["value"]=="testPackage")


def test_del_get_pck():
    print "3. Delete the package vertex"
    str_gremlin_dsl = 'g.V().has("pid","test123").drop()'
    json_response = call_db(str_gremlin_dsl)
    assert(json_response["status"]["code"]==200)
    assert(json_response["result"]["data"]==[])
