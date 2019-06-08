import SocketServer
import socket
import math

host = 'localhost'
port_client = 8557
port_server_sum = '8560'
port_server_sub = '8561'
port_server_mul = '8562'
port_server_div = '8563'
port_server_pow = '8564'
port_server_sqr = '8565'
port_server_log = '8566'

class myHandler(SocketServer.BaseRequestHandler):

   def handle(self):

    self.number1 = self.request.recv(1024)
    exit = False

    while not exit:
        if int(self.number1) >= 1 & int(self.number1) <= 8:
    
         if int(self.number1) == 1:
            self.request.send(port_server_sum)
            print "Port number of Server sum has been sent!"
            exit = True
         elif int(self.number1) == 2:
            self.request.send(port_server_sub)
            print "Port number of Server sub has been sent!"
            exit = True
         elif int(self.number1) == 3:
            self.request.send(port_server_mul)
            print "Port number of Server Mul has been sent!"
            exit = True
         elif int(self.number1) == 4:
            self.request.send(port_server_div)
            print "Port number of Server div has been sent!"
            exit = True
         elif int(self.number1) == 5:
            self.request.send(port_server_pow)
            print "Port number of Server pow has been sent!"
            exit = True
         elif int(self.number1) == 6:
            self.request.send(port_server_sqr)
            print "Port number of Server sqr has been sent!"
            exit = True
         elif int(self.number1) == 7:
            self.request.send(port_server_log)
            print "Port number of Server log has been sent!"
            exit = True
        else:
            print "Server with that refence does not exist!"
            exit = True
            
def main():
   server = SocketServer.TCPServer((host, port_client), myHandler, bind_and_activate = False)
   server.allow_reuse_address = True
   server.server_bind()
   server.server_activate()
   if server:
            print "Server On"

   server.serve_forever()
main()