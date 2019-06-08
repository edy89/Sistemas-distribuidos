from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import SimpleXMLRPCServer
import SocketServer
import threading
import xmlrpclib


def enesim_square(y, x):
    return pow(float(x),(1/float(y)))

class SimpleThreadedXMLRPCServer(SocketServer.ThreadingMixIn, SimpleXMLRPCServer.SimpleXMLRPCServer):
        pass

class ServerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.localServer = SimpleThreadedXMLRPCServer(("localhost",8563))
        self.localServer.register_function(enesim_square)         

    def run(self):
        self.localServer.serve_forever()         
        #print "Listo servidor."      
    
def main():

   server = ServerThread()   
   
   if server:
    print "server Sqr ON"
    server.start()
    #server1.serve_forever()

main()