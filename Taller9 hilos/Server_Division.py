import socket
import thread

host = 'localhost'

def division(x, y):
    return x / y


def myHandler(conn,addr):

    numbers = conn.recv(1024)
    num1,num2 = numbers.split(",")
    div = str(division(float(num1),float(num2)))
    conn.sendall(div)
    print("Div operation done and send!")

def main():

   server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      server_socket.bind((host, 8004))
   except socket.error as msg:
      print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
      sys.exit()

   server_socket.listen(10)

   if server_socket:
            print "Server Div On"

   while 1:
    #wait to accept a connection - blocking call
    conn, addr = server_socket.accept()    
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    thread.start_new_thread (myHandler, (conn, addr))

main()