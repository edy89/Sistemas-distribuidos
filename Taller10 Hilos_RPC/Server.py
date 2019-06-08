from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import SocketServer
import SimpleXMLRPCServer
import sys
import threading
import xmlrpclib
import math

def sum_(numero1, numero2):
    return numero1 + numero2

def substraction(numero1, numero2):
    return numero1 - numero2

def multiplication(numero1, numero2):
    return numero1 * numero2

def division(numero1, numero2):
	return numero1 / numero2

def power(numero1, numero2):
    return pow(numero1,numero2)

def enesim_square(numero1, numero2):
	return math.pow(numero2, (1/numero1))

def base_n_logarithm(numero1, numero2):
    return math.log(numero1,numero2)

class SimpleThreadedXMLRPCServer(SocketServer.ThreadingMixIn, SimpleXMLRPCServer.SimpleXMLRPCServer):
        pass

class ServerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.localServer = SimpleThreadedXMLRPCServer(("localhost",8557))
        self.localServer.register_function(sum_)
        self.localServer.register_function(substraction)
        self.localServer.register_function(multiplication)
        self.localServer.register_function(division)
        self.localServer.register_function(power)
        self.localServer.register_function(enesim_square)
        self.localServer.register_function(base_n_logarithm) 

    def run(self):
        self.localServer.serve_forever()         
         # The server is now running
        print "Listo servidor."      
    
def main():

   server = ServerThread()   
   
   if server:
    print "server ON"
    server.start()
    #server1.serve_forever()

main()