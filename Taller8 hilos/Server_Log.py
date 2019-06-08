import socket
import thread
import math

host = 'localhost'

def base_n_logarithm(x, y):
    return math.log(x,y)


def myHandler(conn,addr):

    numbers = conn.recv(1024)
    num1,num2 = numbers.split(",")
    log = str(base_n_logarithm(float(num1),float(num2)))
    conn.sendall(log)
    print("Log operation done and send!")

def main():

   server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      server_socket.bind((host, 8007))
   except socket.error as msg:
      print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
      sys.exit()

   server_socket.listen(10)

   if server_socket:
            print "Server Log On"

   while 1:
    #wait to accept a connection - blocking call
    conn, addr = server_socket.accept()    
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    thread.start_new_thread (myHandler, (conn, addr))

main()