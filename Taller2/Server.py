import SocketServer
import socket
import math

host = 'localhost'
port_client = 8557
port_server_sum = 8560
port_server_sub = 8561
port_server_mul = 8562
port_server_div = 8563
port_server_pow = 8564
port_server_sqr = 8565
port_server_log = 8566

class myHandler(SocketServer.BaseRequestHandler):

   def handle(self):

    self.numbers = self.request.recv(1024)
    temp = self.numbers
    number1,number2,number3 = temp.split(",")
    exit = False

    while not exit:
        if int(number1) >= 1 & int(number1) <= 8:
    
         if int(number1) == 1:
            socket_sum = socket.socket()
            socket_sum.connect((host,port_server_sum))
            socket_sum.send(temp)
            print "numbers ", number2, " y ", number3, " are send!"
            self.add = socket_sum.recv(1024)
            print("Sum operation done and send!")
            self.request.send(self.add)
            exit = True
         elif int(number1) == 2:
            socket_sum = socket.socket()
            socket_sum.connect((host,port_server_sub))
            socket_sum.send(temp)
            print "numbers ", number2, " y ", number3, " are send!"
            self.sub = socket_sum.recv(1024)
            print("Substraction operation done and send!")
            self.request.send(self.sub)
            exit = True
         elif int(number1) == 3:
            socket_sum = socket.socket()
            socket_sum.connect((host,port_server_mul))
            socket_sum.send(temp)
            print "numbers ", number2, " y ", number3, " are send!"
            self.mul = socket_sum.recv(1024)
            print("Multiplication operation done and send!")
            self.request.send(self.mul)
            exit = True
         elif int(number1) == 4:
            socket_sum = socket.socket()
            socket_sum.connect((host,port_server_div))
            socket_sum.send(temp)
            print "numbers ", number2, " y ", number3, " are send!"
            self.div = socket_sum.recv(1024)
            print("Division operation done and send!")
            self.request.send(self.div)
            exit = True
         elif int(number1) == 5:
            socket_sum = socket.socket()
            socket_sum.connect((host,port_server_pow))
            socket_sum.send(temp)
            print "numbers ", number2, " y ", number3, " are send!"
            self.powe = socket_sum.recv(1024)
            print("Power operation done and send!")
            self.request.send(self.powe)
            exit = True
         elif int(number1) == 6:
            socket_sum = socket.socket()
            socket_sum.connect((host,port_server_sqr))
            socket_sum.send(temp)
            print "numbers ", number2, " y ", number3, " are send!"
            self.sqr = socket_sum.recv(1024)
            print("Square operation done and send!")
            self.request.send(self.sqr)
            exit = True
         elif int(number1) == 7:
            socket_sum = socket.socket()
            socket_sum.connect((host,port_server_log))
            socket_sum.send(temp)
            print "numbers ", number2, " y ", number3, " are send!"
            self.log = socket_sum.recv(1024)
            print("Logarithm operation done and send!")
            self.request.send(self.log)
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