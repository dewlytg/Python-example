#!/usr/bin/env python

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("GET REQUEST")
        u = self.get_argument("user")
        e = self.get_argument("email")
        p = self.get_argument("pwd")
        if u == "tg" and e == "tg@163.com" and p == "123":
            print("OK")
        else:
            print("NOT OK")

    def post(self):
        self.write("POST REQUEST")
        u = self.get_argument("user")
        e = self.get_argument("email")
        p = self.get_argument("pwd")
        print(u,e,p)

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()