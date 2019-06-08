#cd Desktop/sistemas distribuidos/Taller9 hilos
import socket
import thread

port_client = 8557
port_server_sum = '8001'
port_server_sub = '8002'
port_server_mul = '8003'
port_server_div = '8004'
port_server_pow = '8005'
port_server_sqr = '8006'
port_server_log = '8007'


def myHandler(conn, addr):    
    
    op = conn.recv(1024)
    exit = False

    while not exit:
        if int(op) >= 1 & int(op) <= 8:
    
         if int(op) == 1:
            print "Server Sum host has been sent!"
            conn.sendall(port_server_sum)
            exit = True
         elif int(op) == 2:
            print "Server Sub host has been sent!"
            conn.sendall(port_server_sub)
            exit = True
         elif int(op) == 3:
            print "Server Mul host has been sent!"
            conn.sendall(port_server_mul)
            exit = True
         elif int(op) == 4:
            print "Server Div host has been sent!"
            conn.sendall(port_server_div)
            exit = True
         elif int(op) == 5:
            print "Server Pow host has been sent!"
            conn.sendall(port_server_pow)
            exit = True
         elif int(op) == 6:
            print "Server Sqr host has been sent!"
            conn.sendall(port_server_sqr)
            exit = True
         elif int(op) == 7:
            print "Server Log host has been sent!"
            conn.sendall(port_server_log)
            exit = True
        else: 
         print "No valid option CHAU!"
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