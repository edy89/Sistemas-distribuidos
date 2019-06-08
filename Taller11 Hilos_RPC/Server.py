from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import SocketServer
import SimpleXMLRPCServer
import sys
import threading
import xmlrpclib
import math

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class ClientThread(threading.Thread):

    def __init__(self):
      threading.Thread.__init__(self)
      self.client = xmlrpclib.ServerProxy('http://localhost:8558')

    def run(self):
      time.sleep(3)


class myFuncs:

    def sum_(self,x,y):
        client_sum = xmlrpclib.ServerProxy('http://localhost:8558')
        return client_sum.sum_(x,y)

    def substraction(self,x, y):
        client_sub = xmlrpclib.ServerProxy('http://localhost:8559')
        return client_sub.sub(x,y)

    def multiplication(self,x, y):
        client_mul = xmlrpclib.ServerProxy('http://localhost:8560')
        return client_mul.mul(x,y)

    def division(self,x, y):
    	client_div = xmlrpclib.ServerProxy('http://localhost:8561')
        return client_div.div(x,y)

    def power(self,x, y):
        client_pow = xmlrpclib.ServerProxy('http://localhost:8562')
        return client_pow.powe(x,y)

    def enesim_square(self,x, y):
    	client_sqr = xmlrpclib.ServerProxy('http://localhost:8563')
        return client_sqr.enesim_square(x,y)

    def base_n_logarithm(self,x, y):
        client_log = xmlrpclib.ServerProxy('http://localhost:8564')
        return client_log.base_n_logarithm(x,y)

class SimpleThreadedXMLRPCServer(SocketServer.ThreadingMixIn, SimpleXMLRPCServer.SimpleXMLRPCServer):
        pass

class ServerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.localServer = SimpleThreadedXMLRPCServer(("localhost",8557))
        self.localServer.register_instance(myFuncs())
        
    def run(self):
        self.localServer.serve_forever()

        
             
    
def main():

   server = ServerThread()   
   
   if server:
    print "server ON"
    server.start()
    #server1.serve_forever()

main()