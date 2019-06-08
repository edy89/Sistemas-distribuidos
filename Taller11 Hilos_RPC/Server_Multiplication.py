from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import SimpleXMLRPCServer
import SocketServer
import threading
import xmlrpclib


def mul(x, y):
    return x * y

class SimpleThreadedXMLRPCServer(SocketServer.ThreadingMixIn, SimpleXMLRPCServer.SimpleXMLRPCServer):
        pass

class ServerThread(threading.Thread):

    def __init__(self):

        threading.Thread.__init__(self)
        self.localServer = SimpleThreadedXMLRPCServer(("localhost",8560))
        self.localServer.register_function(mul)         

    def run(self):
        self.localServer.serve_forever()         
            
def main():

   server = ServerThread()   
   
   if server:
    print "server Mul ON"
    server.start()
    #server1.serve_forever()

main()