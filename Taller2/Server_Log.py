import SocketServer
import socket
import math

host = 'localhost'
port_server_log = 8566

def base_n_logarithm(x, y):
    return math.log(x,y)

class myHandler(SocketServer.BaseRequestHandler):

   def handle(self):
    self.numbers = self.request.recv(1024)
    temp = self.numbers
    number1,number2,number3 = temp.split(",")
    log = str(base_n_logarithm(float(number2),float(number3)))
    print 'The received numbers are: ' , number2, 'and', number3, 'and its logarithm is equal to: ', log
    self.request.send(log)

def main():

  server_sum = SocketServer.TCPServer((host, port_server_log), myHandler, bind_and_activate = False)
  server_sum.allow_reuse_address = True
  server_sum.server_bind()
  server_sum.server_activate()
  if server_sum:
    print "Server Logarithm On"
  server_sum.serve_forever()

main()