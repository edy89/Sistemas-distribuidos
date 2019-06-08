import SocketServer
import socket
import math

host = 'localhost'
port_server_pow = 8564

def power(x, y):
    return pow(x,y)

class myHandler(SocketServer.BaseRequestHandler):

   def handle(self):
    self.numbers = self.request.recv(1024)
    temp = self.numbers
    number2,number3 = temp.split(",")
    powe = str(power(int(number2),int(number3)))
    print 'The received numbers are: ' , number2, 'and', number3, 'and its power is equal to: ', powe
    self.request.send(powe)

def main():

  server_sum = SocketServer.TCPServer((host, port_server_pow), myHandler, bind_and_activate = False)
  server_sum.allow_reuse_address = True
  server_sum.server_bind()
  server_sum.server_activate()
  if server_sum:
    print "Server Power On"
  server_sum.serve_forever()

main()