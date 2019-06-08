import socket
import sys
import thread
import math

host = 'localhost'
port_client = 8557

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
    return pow(numero2, (1/numero1))

def base_n_logarithm(numero1, numero2):
    return math.log(numero1,numero2)

#class myHandler(SocketServer.BaseRequestHandler):

def myHandler(conn, addr):

    numbers = conn.recv(1024)
    #temp = numbers
    number1,number2,number3 = numbers.split(",")
    exit = False

    while not exit:
        if int(number1) >= 1 & int(number1) <= 8:
    
         if int(number1) == 1:
            print "numbers ", number2, " y ", number3, " are received!"
            add = str(sum_(int(number2),int(number3)))
            print("Sum operation done and send!")
            conn.sendall(add)
            exit = True
         elif int(number1) == 2:
            print "numbers ", number2, " y ", number3, " are received!"
            sub = str(substraction(int(number2),int(number3)))
            print("Sub operation done and send!")
            conn.sendall(sub)
            exit = True
         elif int(number1) == 3:
            print "numbers ", number2, " y ", number3, " are received!"
            mul = str(multiplication(int(number2),int(number3)))
            print("Mul operation done and send!")
            conn.sendall(mul)
            exit = True
         elif int(number1) == 4:
            print "numbers ", number2, " y ", number3, " are received!"
            div = str(division(float(number2),float(number3)))
            print("Div operation done and send!")
            conn.sendall(div)
            exit = True
         elif int(number1) == 5:
            print "numbers ", number2, " y ", number3, " are received!"
            powe = str(power(int(number2),int(number3)))
            print("Pow operation done and send!")
            conn.sendall(powe)
            exit = True
         elif int(number1) == 6:
            print "numbers ", number2, " y ", number3, " are received!"
            sqr = str(enesim_square(float(number2),float(number3)))
            print("Sqr operation done and send!")
            conn.sendall(sqr)
            exit = True
         elif int(number1) == 7:
            print "numbers ", number2, " y ", number3, " are received!"
            log = str(base_n_logarithm(float(number2),float(number3)))
            print("Log operation done and send!")
            conn.sendall(log)
            exit = True

            
def main():
   # server = SocketServer.TCPServer((host, port_client), myHandler, bind_and_activate = False)
   # server.allow_reuse_address = True
   # server.server_bind()
   # server.server_activate()
   server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   server_socket.bind((host, port_client))
   server_socket.listen(10)

   if server_socket:
            print "Server On"

   while 1:
    #wait to accept a connection - blocking call
    conn, addr = server_socket.accept()    
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    thread.start_new_thread (myHandler, (conn, addr))
   
   

   #server.serve_forever()
main()