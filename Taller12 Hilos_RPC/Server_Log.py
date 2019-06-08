from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import SimpleXMLRPCServer
import SocketServer
import threading
import xmlrpclib
import math


def base_n_logarithm(x, y):
    return math.log(float(x),float(y))

class SimpleThreadedXMLRPCServer(SocketServer.ThreadingMixIn, SimpleXMLRPCServer.SimpleXMLRPCServer):
        pass

class ServerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.localServer = SimpleThreadedXMLRPCServer(("localhost",8564))
        self.localServer.register_function(base_n_logarithm)         

    def run(self):
        self.localServer.serve_forever()         
        #print "Listo servidor."      
    
def main():

   server = ServerThread()   
   
   if server:
    print "server Log ON"
    server.start()
    #server1.serve_forever()

main()