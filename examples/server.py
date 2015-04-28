import sys
import os
import tornado.web
import tornado.escape
import tornado.ioloop
import tornado.httputil
import json
import urllib
import time
from tornado import gen

from tornado.escape import json_encode
from tornado.options import define, options, parse_command_line
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.httpserver import HTTPServer
from tornado.http1connection import HTTP1ServerConnection, HTTP1ConnectionParameters

define("port", default=9001, help="run on the given port", type=int)

@tornado.web.stream_request_body
class Serverhook(tornado.web.RequestHandler):
    
    @tornado.web.asynchronous
    @gen.engine

    def initialize(self):
        pass

    def post(self):
        self.set_header("Content-Type","text/plain")
        try:
            text = self.get_argument('text')
            print(text)
            self.write(tornado.escape.json_encode({'status':'success'}))
        except tornado.web.MissingArgumentError:
            print('Argument is missing')
            self.write(tornado.escape.json_encode({'status':'fail'}))
        self.finish()

def main():
    application = tornado.web.Application([(r"/hook", Serverhook)])
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()

