from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import SimpleXMLRPCServer
import SocketServer
import threading
import xmlrpclib


def powe(x, y):
    return pow(x,y)

class SimpleThreadedXMLRPCServer(SocketServer.ThreadingMixIn, SimpleXMLRPCServer.SimpleXMLRPCServer):
        pass

class ServerThread(threading.Thread):

    def __init__(self):

        threading.Thread.__init__(self)
        self.localServer = SimpleThreadedXMLRPCServer(("localhost",8562))
        self.localServer.register_function(powe)         

    def run(self):
        self.localServer.serve_forever()         
        #print "Listo servidor."      
    
def main():

   server = ServerThread()   
   
   if server:
    print "server pow ON"
    server.start()
    #server1.serve_forever()

main()