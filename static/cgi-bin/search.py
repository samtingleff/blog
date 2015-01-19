#!/usr/bin/env python
import web
import json
from yassg.search import SearchClient
        
urls = (
    '/cgi-bin/search', 'search',
    '/cgi-bin/similar', 'similar'
    '/cgi-bin/reopen', 'reopen'
)
app = web.application(urls, globals())
search_client = SearchClient("localhost", 9999)
search_client.connect()

class search:        
    def GET(self):
        args = web.input()
        response = {}
        try:
            q = args.q
            results = search_client.query(q)
            response["status"] = "ok"
            response["results"] = convert(results.hits)
        except AttributeError, e:
            response["status"] = "error"
            response["error"] = "no query specified"
        web.header('Content-Type', 'application/json')
        return json.dumps(response)

class similar:
    def GET(self):
        args = web.input()
        response = {}
        try:
            search = args.search
            results = search_client.similar(search)
            response["status"] = "ok"
            response["results"] = convert(results.hits)
        except AttributeError, e:
            response["status"] = "error"
            response["error"] = "no query specified"
        web.header('Content-Type', 'application/json')
        return json.dumps(response)

class reopen:
    def GET(self):
        response = {}
        try:
            results = search_client.reopen()
            response["status"] = "ok"
        except AttributeError, e:
            response["status"] = "error"
        web.header('Content-Type', 'application/json')
        return json.dumps(response)

def convert(hits):
    result = []
    for search_doc in hits:
        o = {
            "docId":search_doc.docId,
            "description":search_doc.fields["description"],
            "date":search_doc.fields["pubDate"],
            "id":search_doc.fields["id"],
            "href":("/%s" % search_doc.fields["href"]) }
        result.append(o)
    return result

if __name__ == "__main__":
    app.run()
