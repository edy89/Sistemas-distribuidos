import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler


socket_sum = xmlrpclib.ServerProxy('http://localhost:8001')
socket_sub = xmlrpclib.ServerProxy('http://localhost:8002')
socket_mul = xmlrpclib.ServerProxy('http://localhost:8003')
socket_div = xmlrpclib.ServerProxy('http://localhost:8004')
socket_pow = xmlrpclib.ServerProxy('http://localhost:8005')
socket_sqr = xmlrpclib.ServerProxy('http://localhost:8006')
socket_log = xmlrpclib.ServerProxy('http://localhost:8007')

def sum_(x,y):        
    add = socket_sum.add(x,y)
    return add

def sub(x, y):
    sub = socket_sub.sub(x,y)
    return sub

def mul(x,y):
    mul = socket_mul.mul(x,y)
    return mul

def div(x,y):
    div = socket_div.div(x,y)
    return div

def powe(x,y):
    powe = socket_pow.pow(x,y)
    return powe

def sqr(x,y):
    sqr = socket_sqr.sqr(x,y)
    return sqr

def loga(x,y):
    loga = socket_log.loga(x,y)
    return loga



class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

    # def sum_(x,y):
    #     #socket1 = xmlrpclib.ServerProxy('http://localhost:8001')
    #     add = socket1.add(x,y)


def main():
    
    server = SimpleXMLRPCServer(("localhost", 8000),requestHandler = RequestHandler)
    server.register_introspection_functions()
    server.register_function(sum_,'add')
    server.register_function(sub,'sub')
    server.register_function(mul,'mul')
    server.register_function(div,'div')
    server.register_function(powe,'powe')
    server.register_function(sqr,'sqr')
    server.register_function(loga,'loga')
    #server.register_instance(MyFuncs())
    if server:
        print "Server Middle On!"
        server.serve_forever()
    
main()