#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2012
#
# @author zhengji91@gmail.com
# @version 1.0
#
"""
    gtalkrobot
"""

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import logging
from tornado.options import define, options
import robot

define("addr", default="0.0.0.0", help="run on given addr", type=str)
define("port", default=8090, help="run on given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/gtalk", TalkHandler),
            (r"/add",AddContact),
            (r"/remove",RemoveContact)
        ]
        settings = dict()
        tornado.web.Application.__init__(self, handlers, **settings)

class Contacts:
    contacts = []

    def __init__(self,filename):
        self.filename = filename
        Contacts.contacts = []
        fp = open(self.filename,"r")
        for line in fp:
            Contacts.contacts.append(line[0:-1])
        fp.close()

    def add(self, email):
        fp = open(self.filename,"a+")
        if email.strip() in Contacts.contacts: 
            print "email has been existed"
        else:
            fp.write(email.strip()+"\n")
        fp.close()
        self.update()

    def remove(self, email):
        fp = open(self.filename,"r")
        tmp_content = []
        for line in fp:
            if line[0:-1] != email.strip():
                tmp_content.append(line)
            else:
                continue
        fp.close()
        fp = open(self.filename,"w")
        for line in tmp_content:
            fp.write(line)
        fp.close()
        self.update()

    def update(self):
        fp = open(self.filename,"r")
        Contacts.contacts = []
        for line in fp:
            Contacts.contacts.append(line[0:-1])
        fp.close()
    
class TalkHandler(tornado.web.RequestHandler):
    def post(self):
        msg = self.get_argument("msg")
        robot.chat(msg)

class AddContact(tornado.web.RequestHandler):
    def get(self):
        cls = Contacts("contactlist")
        if self.get_argument("email",None):
            cls.add(self.get_argument("email"))
            print "receive"
        self.render("html/index.html",lists = cls.contacts)


class RemoveContact(tornado.web.RequestHandler):
    def get(self):
        cls = Contacts("contactlist")
        if self.get_argument("email",None):
            cls.remove(self.get_argument("email"))
            print "receive"
        self.render("html/index.html",lists = cls.contacts)



def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port, options.addr)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
