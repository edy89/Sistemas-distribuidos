#import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler


class myServers:

    op = 0
    def receive(self,x):
        op = x

        if (op >= 1   &  op <= 8):

            if op == 1:
              return 'http://localhost:8001'
              print "Host server Sum has been sent!"
              print("CHAU!")
              exit = True
            elif op == 2:
              return 'http://localhost:8002'
              print "Host server Sub has been sent!"
              print("CHAU!")
              exit = True
            elif op == 3:
              return 'http://localhost:8003'
              print "Host server Mul has been sent!"
              print("CHAU!")
              exit = True
            elif op == 4:
              return 'http://localhost:8004'
              print "Host server Div has been sent!"
              print("CHAU!")
              exit = True
            elif op == 5:
              return 'http://localhost:8005'
              print "Host server Pow has been sent!"
              print("CHAU!")
              exit = True
            elif op == 6:
              return 'http://localhost:8006'
              print "Host server Sqr has been sent!"
              print("CHAU!")
              exit = True
            elif op == 7:
              return 'http://localhost:8007'
              print "Host server Log has been sent!"
              print("CHAU!")
              exit = True
            elif op == 8:
              print("CHAU!")
              exit = True
        else: 
            print "No valid option CHAU!"
            exit = True




class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

   

def main():
    
    server = SimpleXMLRPCServer(("localhost", 8000),requestHandler = RequestHandler)
    server.register_instance(myServers())
    if server:
        print "Server Middle On!"
        server.serve_forever()
    
main()