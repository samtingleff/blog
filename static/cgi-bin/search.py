#!/usr/bin/env python
import web
import json
from yassg.search import SearchClient
from yassg.likes import LikesClient
from yassg.sessions import SessionClient
from tservices import ttypes
        
urls = (
    '/cgi-bin/search', 'search',
    '/cgi-bin/similar', 'similar',
    '/cgi-bin/likes', 'likes',
    '/cgi-bin/reopen', 'reopen'
)
app = web.application(urls, globals())
session_client = SessionClient("localhost", 9998)
session_client.connect()
search_client = SearchClient("localhost", 9999)
search_client.connect()
likes_client = LikesClient("localhost", 9997)
likes_client.connect()

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

class likes:
    def GET(self):
        args = web.input()
        response = {}
        try:
            page_id = int(args.page)
            device = ttypes.TDevice(web.ctx.ip, web.ctx.env['HTTP_USER_AGENT'], None)
            device.id = session_client.create(device)
            count = likes_client.count(device, page_id)
            response["status"] = "ok"
            response["count"] = count
        except AttributeError, e1:
            response["status"] = "error"
            response["error"] = "no page id specific"
        except ttypes.TSessionException, e2:
            response["status"] = "error"
            response["error"] = "invalid session"
        web.header("Content-Type", "application-json")
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
