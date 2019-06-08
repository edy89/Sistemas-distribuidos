import socket
import thread

print 'taller 7 hilos'
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_temp_sum = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_temp_sub = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_temp_mul = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_temp_div = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_temp_pow = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_temp_sqr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_temp_log = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.connect(('localhost',8557))
exit = False

while not exit:

  print ("WELCOME TO OPTIONS MENU \n")
  print ("1. Sum \n")
  print ("2. Substraction \n")
  print ("3. Multiplication \n")
  print ("4. division \n")
  print ("5. Power \n")
  print ("6. enesim_square \n")
  print ("7. base_n_logarithm \n")
  print ("8. Exit \n")

  number1 = raw_input('Input option you want to realize: ')

  if (int(number1) >= 1   & int(number1) <= 8):
    
    if int(number1) == 1:
      socket_server.send(number1)
      address_server = socket_server.recv(1024)
      print "Connection with " + address_server + " is On!"
      number2 = raw_input('Input the first number: ')
      number3 = raw_input('Input the second number: ')
      numbers = number2 + "," + number3
      print "Parameters of send: ",numbers.split(",")
      socket_temp_sum.connect(('localhost',int(address_server)))
      socket_temp_sum.send(numbers)
      add = socket_temp_sum.recv(1024)
      print number2, " + " , number3, " = ", add
      print("CHAU!")
      exit = True
    elif int(number1) == 2:
      socket_server.send(number1)
      address_server = socket_server.recv(1024)
      print "Connection with " + address_server + " is On!"
      number2 = raw_input('Input the first number: ')
      number3 = raw_input('Input the second number: ')
      numbers = number2 + "," + number3
      print "Parameters of send: ",numbers.split(",")
      socket_temp_sub.connect(('localhost',int(address_server)))
      socket_temp_sub.send(numbers)
      sub = socket_temp_sub.recv(1024)
      print number2, " - " , number3, " = ", sub
      print("CHAU!")
      exit = True
    elif int(number1) == 3:
      socket_server.send(number1)
      address_server = socket_server.recv(1024)
      print "Connection with " + address_server + " is On!"
      number2 = raw_input('Input the first number: ')
      number3 = raw_input('Input the second number: ')
      numbers = number2 + "," + number3
      print "Parameters of send: ",numbers.split(",")
      socket_temp_mul.connect(('localhost',int(address_server)))
      socket_temp_mul.send(numbers)
      mul = socket_temp_mul.recv(1024)
      print number2, " * " , number3, " = ", mul
      print("CHAU!")
      exit = True
    elif int(number1) == 4:
      socket_server.send(number1)
      address_server = socket_server.recv(1024)
      print "Connection with " + address_server + " is On!"
      number2 = raw_input('Input the first number: ')
      number3 = raw_input('Input the second number: ')
      numbers = number2 + "," + number3
      print "Parameters of send: ",numbers.split(",")
      socket_temp_div.connect(('localhost',int(address_server)))
      socket_temp_div.send(numbers)
      div = socket_temp_div.recv(1024)
      print number2, " / " , number3, " = ", div
      print("CHAU!")
      exit = True
    elif int(number1) == 5:
      socket_server.send(number1)
      address_server = socket_server.recv(1024)
      print "Connection with " + address_server + " is On!"
      number2 = raw_input('Input the first number: ')
      number3 = raw_input('Input the second number: ')
      numbers = number2 + "," + number3
      print "Parameters of send: ",numbers.split(",")
      socket_temp_pow.connect(('localhost',int(address_server)))
      socket_temp_pow.send(numbers)
      powe = socket_temp_pow.recv(1024)
      print number2, " ^ " , number3, " = ", powe
      print("CHAU!")
      exit = True
    elif int(number1) == 6:
      socket_server.send(number1)
      address_server = socket_server.recv(1024)
      print "Connection with " + address_server + " is On!"
      number2 = raw_input('Input the first number: ')
      number3 = raw_input('Input the second number: ')
      numbers = number2 + "," + number3
      print "Parameters of send: ",numbers.split(",")
      socket_temp_sqr.connect(('localhost',int(address_server)))
      socket_temp_sqr.send(numbers)
      sqr = socket_temp_sqr.recv(1024)
      print number3, " ^ 1 / " , number2, " = ", sqr
      print("CHAU!")
      exit = True
    elif int(number1) == 7:
      socket_server.send(number1)
      address_server = socket_server.recv(1024)
      print "Connection with " + address_server + " is On!"
      number2 = raw_input('Input the first number: ')
      number3 = raw_input('Input the second number: ')
      numbers = number2 + "," + number3
      print "Parameters of send: ",numbers.split(",")
      socket_temp_log.connect(('localhost',int(address_server)))
      socket_temp_log.send(numbers)
      log = socket_temp_log.recv(1024)
      print " Log base ", number2," de ", number3, " = ", log
      print("CHAU!")
      exit = True
    elif int(number1) == 8:
      print("CHAU!")
      exit = True
  else: 
    print "No valid option CHAU!"
    exit = True

