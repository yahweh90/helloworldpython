from wsgire.simple_server import make_server
from pyramid.config import Configurator 
from pyramid.response import Response
import os

def hello_world(request):
    name = os.environ.get('NAME')
    if name ==None or len(name) == 0:
        name = "world"
        message = "Hello," + name + "!\n"
        return Response(message)

    if_name_ == '__main__'
    port =int(os.environ.get("PORT"))
    with Configurator() as config:
        config.add_route('hello','/')
        config.add_view(hello_world,route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()


# python3 server.py
# 127.0.0.1 - - [11/Apr/2017 11:36:49] "GET / HTTP/1.1" 200 -
# http :8000
'''
HTTP/1.0 200 OK
Date: Tue, 11 Apr 2017 15:36:49 GMT
Server: SimpleHTTP/0.6 Python/3.5.2

Hello world
