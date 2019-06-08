from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import SimpleXMLRPCServer
import SocketServer
import threading
import xmlrpclib


def sum_(x, y):
    return int(x) + int(y)

class SimpleThreadedXMLRPCServer(SocketServer.ThreadingMixIn, SimpleXMLRPCServer.SimpleXMLRPCServer):
        pass

class ServerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.localServer = SimpleThreadedXMLRPCServer(("localhost",8558))
        self.localServer.register_function(sum_)         

    def run(self):
        self.localServer.serve_forever()         
            
def main():

   server = ServerThread()   
   
   if server:
    print "server Sum ON"
    server.start()
    #server1.serve_forever()

main()