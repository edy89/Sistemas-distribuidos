import math

from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

class MyFuncs:

    def sum_(self,x,y):
        return x + y

    def div(self, x, y):
        return x / y

    def sub(self,x,y):
        return x - y

    def mul(self,x,y):
        return x * y

    def sqr(self,x,y):
        return pow(y, 1.0/x)

    def loga(self,x,y):
        return math.log(x,y)

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

def main():

    server = SimpleXMLRPCServer(("localhost", 8000),requestHandler = RequestHandler)
    server.register_introspection_functions()
    server.register_function(pow)
    server.register_instance(MyFuncs())
    server.serve_forever()
    
main()