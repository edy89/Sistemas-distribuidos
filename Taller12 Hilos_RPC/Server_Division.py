from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import SimpleXMLRPCServer
import SocketServer
import threading
import xmlrpclib


def div(x,y):
    return float(x) / float(y)

class SimpleThreadedXMLRPCServer(SocketServer.ThreadingMixIn, SimpleXMLRPCServer.SimpleXMLRPCServer):
        pass

class ServerThread(threading.Thread):

    def __init__(self):

        threading.Thread.__init__(self)
        self.localServer = SimpleThreadedXMLRPCServer(("localhost",8561))
        self.localServer.register_function(div)         

    def run(self):
        self.localServer.serve_forever()         
        #print "Listo servidor."      
    
def main():

   server = ServerThread()   
   
   if server:
    print "server Div ON"
    server.start()
    #server1.serve_forever()

main()