#!/usr/bin/env python3
"""
Main file
"""
from pprint import pprint as pp
Server = __import__('2-hypermedia_pagination').Server
# Server = __import__('1-simple_pagination').Server

server = Server()

pp(server.get_hyper(1, 2))
print("---")
pp(server.get_hyper(2, 2))
print("---")
pp(server.get_hyper(100, 3))
print("---")
pp(server.get_hyper(3000, 100))
