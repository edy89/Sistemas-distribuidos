import socket

print 'taller 3'
host = 'localhost'
port = 8557
socket_server = socket.socket()
socket_server.connect((host,port))
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
      number2 = raw_input('Input the first number: ')
      number3 = raw_input('Input the second number: ')
      numbers = number2 + "," + number3
      print "Parameters of send: ",numbers.split(",")
      port_server_sum = socket_server.recv(1024)
      socket_server_sum = socket.socket()
      socket_server_sum.connect((host,int(port_server_sum)))
      socket_server_sum.send(numbers)
      add = socket_server_sum.recv(1024)
      print number2, " + " , number3, " = ", add
      print("CHAU!")
      exit = True
    elif int(number1) == 2:
      socket_server.send(number1)
      number2 = raw_input('Input the first number: ')
      number3 = raw_input('Input the second number: ')
      numbers = number2 + "," + number3
      print "Parameters of send: ",numbers.split(",")
      port_server_sub = socket_server.recv(1024)
      socket_server_sub = socket.socket()
      socket_server_sub.connect((host,int(port_server_sub)))
      socket_server_sub.send(numbers)
      sub = socket_server_sub.recv(1024)
      print sub
      print number2, " - " , number3, " = ", sub
      print("CHAU!")
      exit = True
    elif int(number1) == 3:
      socket_server.send(number1)
      number2 = raw_input('Input the first number: ')
      number3 = raw_input('Input the second number: ')
      numbers = number2 + "," + number3
      print "Parameters of send: ",numbers.split(",")
      port_server_mul = socket_server.recv(1024)
      socket_server_mul = socket.socket()
      socket_server_mul.connect((host,int(port_server_mul)))
      socket_server_mul.send(numbers)
      mul = socket_server_mul.recv(1024)
      print number2, " * " , number3, " = ", mul
      print("CHAU!")
      exit = True
    elif int(number1) == 4:
      socket_server.send(number1)
      number2 = raw_input('Input the first number: ')
      number3 = raw_input('Input the second number: ')
      numbers = number2 + "," + number3
      print "Parameters of send: ",numbers.split(",")
      port_server_div = socket_server.recv(1024)
      socket_server_div = socket.socket()
      socket_server_div.connect((host,int(port_server_div)))
      socket_server_div.send(numbers)
      div = socket_server_div.recv(1024)
      print number2, " / " , number3, " = ", div
      print("CHAU!")
      exit = True
    elif int(number1) == 5:
      socket_server.send(number1)
      number2 = raw_input('Input the first number (base): ')
      number3 = raw_input('Input the second number (exponent): ')
      numbers = number2 + "," + number3
      print "Parameters of send: ",numbers.split(",")
      port_server_pow = socket_server.recv(1024)
      socket_server_pow = socket.socket()
      socket_server_pow.connect((host,int(port_server_pow)))
      socket_server_pow.send(numbers)
      powe = socket_server_pow.recv(1024)
      print number2, " ^ " , number3, " = ", powe
      print("CHAU!")
      exit = True
    elif int(number1) == 6:
      socket_server.send(number1)
      number2 = raw_input('Input the first number (index): ')
      number3 = raw_input('Input the second number (base): ')
      numbers = number2 + "," + number3
      print "Parameters of send: ",numbers.split(",")
      port_server_sqr = socket_server.recv(1024)
      socket_server_sqr = socket.socket()
      socket_server_sqr.connect((host,int(port_server_sqr)))
      socket_server_sqr.send(numbers)
      sqr = socket_server_sqr.recv(1024)
      print number2, " ^ 1 / " , number3, " = ", sqr
      print("CHAU!")
      exit = True
    elif int(number1) == 7:
      socket_server.send(number1)
      number2 = raw_input('Input the first number: ')
      number3 = raw_input('Input the second number: ')
      numbers = number2 + "," + number3
      print "Parameters of send: ",numbers.split(",")
      port_server_log = socket_server.recv(1024)
      socket_server_log = socket.socket()
      socket_server_log.connect((host,int(port_server_log)))
      socket_server_log.send(numbers)
      log = socket_server_log.recv(1024)
      print " Log base ", number2," de ", number3, " = ", log
      print("CHAU!")
      exit = True
    elif int(number1) == 8:
      print("CHAU!")
      exit = True
  else: 
    print "No valid option CHAU!"
    exit = True

