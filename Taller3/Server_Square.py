import SocketServer
import socket
import math

host = 'localhost'
port_server_sqr = 8565

def enesim_square(x, y):
  return pow(y, (1.0/x))

class myHandler(SocketServer.BaseRequestHandler):

   def handle(self):
    self.numbers = self.request.recv(1024)
    temp = self.numbers
    number2,number3 = temp.split(",")
    sqr = str(enesim_square(int(number2),int(number3)))
    print 'The received numbers are: ' , number2, 'and', number3, 'and its Square is equal to: ', sqr
    self.request.send(sqr)

def main():

  server_sum = SocketServer.TCPServer((host, port_server_sqr), myHandler, bind_and_activate = False)
  server_sum.allow_reuse_address = True
  server_sum.server_bind()
  server_sum.server_activate()
  if server_sum:
    print "Server Square On"
  server_sum.serve_forever()

main()