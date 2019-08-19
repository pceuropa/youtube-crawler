from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}

res = es.index(index="test-index", doc_type='tweet', id=2, body=doc)

print('first res', res['result'])

res = es.get(index="test-index", doc_type='tweet', id=2)
print('second res', res['_source'])

es.indices.refresh(index="test-index")

res = es.search(index="test-index", body={"query": {"match_all": {}}})
print(res)

for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
