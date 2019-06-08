import SocketServer
import socket
import math

host = 'localhost'
port_server_mul = 8562

def multiplication(x, y):
    return x * y

class myHandler(SocketServer.BaseRequestHandler):

   def handle(self):
    self.numbers = self.request.recv(1024)
    temp = self.numbers
    number1,number2,number3 = temp.split(",")
    mul = str(multiplication(int(number2),int(number3)))
    print 'The received numbers are: ' , number2, 'and', number3, 'and its multiplication is equal to: ', mul
    self.request.send(mul)

def main():

  server_sum = SocketServer.TCPServer((host, port_server_mul), myHandler, bind_and_activate = False)
  server_sum.allow_reuse_address = True
  server_sum.server_bind()
  server_sum.server_activate()
  if server_sum:
    print "Server Multiplication On"
  server_sum.serve_forever()

main()