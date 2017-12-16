#!/usr/bin/env python
from wsgiref.simple_server import make_server
from View import account

handler_dict = {
    "/index":account.handler_index,
    "/date":account.handler_date
}

def RunServer(environ,start_response):
    pathinfo = environ["PATH_INFO"]
    start_response("200 OK",[("Content-Type","text/html")])
    if pathinfo in handler_dict:
        func = handler_dict[pathinfo]
        ret = func()
        return ret
    else:
        return [b"<h1>hello,web!</h1>",]

if __name__ == '__main__':
    httpd = make_server("",8000,RunServer)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()