import SocketServer
import socket
import math

host = 'localhost'
port_server_div = 8563

def division(x, y):
    return x / y

class myHandler(SocketServer.BaseRequestHandler):

   def handle(self):
    self.numbers = self.request.recv(1024)
    temp = self.numbers
    number2,number3 = temp.split(",")
    div = str(division(float(number2),float(number3)))
    print 'The received numbers are: ' , number2, 'and', number3, 'and its division is equal to: ', div
    self.request.send(div)

def main():

  server_sum = SocketServer.TCPServer((host, port_server_div), myHandler, bind_and_activate = False)
  server_sum.allow_reuse_address = True
  server_sum.server_bind()
  server_sum.server_activate()
  if server_sum:
    print "Server Division On"
  server_sum.serve_forever()

main()