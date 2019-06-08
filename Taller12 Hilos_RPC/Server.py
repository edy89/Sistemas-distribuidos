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

class myFuncs:

    def server_sum(self):
        return '8558'

    def server_substraction(self):
        return '8559'

    def server_multiplication(self):
        return '8560'

    def server_division(self):
    	return '8561'

    def server_power(self):
        return '8562'

    def server_enesim_square(self):
    	return '8563'

    def server_base_n_logarithm(self):
        return '8564'

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