#cd Desktop/sistemas distribuidos/Taller7 hilos
import socket
import sys
import thread
import math

port_client = 8557


def myHandler(conn, addr):
    
    socket_temp_sum = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_temp_sub = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_temp_mul = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_temp_div = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_temp_pow = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_temp_sqr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_temp_log = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    numbers = conn.recv(1024)
    number1,number2,number3 = numbers.split(",")
    exit = False

    while not exit:
        if int(number1) >= 1 & int(number1) <= 8:
    
         if int(number1) == 1:
            print "numbers ", number2, " y ", number3, " are received!"
            #socket_temp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_temp_sum.connect(('localhost',8001))
            socket_temp_sum.send(number2 + "," + number3)
            add = socket_temp_sum.recv(1024)
            conn.sendall(add)
            exit = True
         elif int(number1) == 2:
            print "numbers ", number2, " y ", number3, " are received!"
            socket_temp_sub.connect(('localhost',8002))
            socket_temp_sub.send(number2 + "," + number3)
            sub = socket_temp_sub.recv(1024)
            conn.sendall(sub)
            exit = True
         elif int(number1) == 3:
            print "numbers ", number2, " y ", number3, " are received!"
            # socket_temp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_temp_mul.connect(('localhost',8003))
            socket_temp_mul.send(number2 + "," + number3)
            mul = socket_temp_mul.recv(1024)
            conn.sendall(mul)
            exit = True
         elif int(number1) == 4:
            print "numbers ", number2, " y ", number3, " are received!"
            socket_temp_div.connect(('localhost',8004))
            socket_temp_div.send(number2 + "," + number3)
            div = socket_temp_div.recv(1024)
            conn.sendall(div)
            exit = True
         elif int(number1) == 5:
            print "numbers ", number2, " y ", number3, " are received!"
            socket_temp_pow.connect(('localhost',8005))
            socket_temp_pow.send(number2 + "," + number3)
            powe = socket_temp_pow.recv(1024)
            conn.sendall(powe)
            exit = True
         elif int(number1) == 6:
            print "numbers ", number2, " y ", number3, " are received!"
            socket_temp_sqr.connect(('localhost',8006))
            socket_temp_sqr.send(number2 + "," + number3)
            sqr = socket_temp_sqr.recv(1024)
            conn.sendall(sqr)
            exit = True
         elif int(number1) == 7:
            print "numbers ", number2, " y ", number3, " are received!"
            socket_temp_log.connect(('localhost',8007))
            socket_temp_log.send(number2 + "," + number3)
            log = socket_temp_log.recv(1024)
            conn.sendall(log)
            exit = True

            
def main():
   
   server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   server_socket.bind(('localhost', port_client))
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