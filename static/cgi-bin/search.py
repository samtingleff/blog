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
            cookie_val = web.cookies().get("id")
            if cookie_val:
                device.id = get_device_id_from_cookie(cookie_val)
            if device.id is None:
                device.id = session_client.create(device)
            count = likes_client.count(device, page_id)
            response["status"] = "ok"
            response["count"] = count
            cookie_val = format_device_id_cookie(device.id)
            web.setcookie('id', cookie_val, 31536000, path="/")
        except TypeError, e0:
            response["status"] = "error"
            response["error"] = "type error"
        except AttributeError, e1:
            response["status"] = "error"
            response["error"] = "no page id specific"
        except ttypes.TSessionException, e2:
            response["status"] = "error"
            response["error"] = "invalid session"
        web.header("Content-Type", "application-json")
        return json.dumps(response)

    def POST(self):
        args = web.input()
        response = {}
        try:
            page_id = int(args.page)
            device = ttypes.TDevice(web.ctx.ip, web.ctx.env['HTTP_USER_AGENT'], None)
            cookie_val = web.cookies().get("id")
            if cookie_val:
                device.id = get_device_id_from_cookie(cookie_val)
            if device.id is None:
                response["status"] = "session"
            else:
                likes_client.like(device, page_id)
                response["status"] = "ok"
        except TypeError, e0:
            response["status"] = "error"
            response["error"] = "type error"
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

def get_device_id_from_cookie(cookie_val):
    try:
        vals = cookie_val.split("/")
        result = ttypes.TDeviceId(int(vals[0]), int(vals[1], 16), vals[2])
        return result
    except Error, e: return None

def format_device_id_cookie(device_id):
    return "%s/%s/%s" % (device_id.version, format(device_id.id, "x"), device_id.signature)

if __name__ == "__main__":
    app.run()
