import xmlrpclib


print 'taller 4'
exit = False
socket_server_mid = xmlrpclib.ServerProxy('http://localhost:8000')
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
      number1 = int(number1)
      number2 = raw_input('Input the first number: ')
      number3 = raw_input('Input the second number: ')
      http_temp = socket_server_mid.receive(number1)
      number2 = int(number2)
      number3 = int(number3)  
      socket_server_temp = xmlrpclib.ServerProxy(http_temp)
      add = socket_server_temp.add(number2,number3)
      print number2, " + " , number3, " = ", add
      print("CHAU!")
      exit = True
    elif int(number1) == 2:
      number1 = int(number1)
      number2 = raw_input('Input the first number: ')
      number3 = raw_input('Input the second number: ')
      http_temp = socket_server_mid.receive(number1)
      number2 = int(number2)
      number3 = int(number3)
      socket_server_temp = xmlrpclib.ServerProxy(http_temp)
      sub = socket_server_temp.sub(number2,number3)
      print number2, " - " , number3, " = ", sub
      print("CHAU!")
      exit = True
    elif int(number1) == 3:
      number1 = int(number1)
      number2 = raw_input('Input the first number: ')
      number3 = raw_input('Input the second number: ')
      http_temp = socket_server_mid.receive(number1)
      number2 = int(number2)
      number3 = int(number3)
      socket_server_temp = xmlrpclib.ServerProxy(http_temp)
      mul = socket_server_temp.mul(number2,number3)
      print number2, " * " , number3, " = ", mul
      print("CHAU!")
      exit = True
    elif int(number1) == 4:
      number1 = int(number1)
      number2 = raw_input('Input the first number (numerador): ')
      number3 = raw_input('Input the second number (denominador): ')
      http_temp = socket_server_mid.receive(number1)
      number2 = float(number2)
      number3 = float(number3)
      socket_server_temp = xmlrpclib.ServerProxy(http_temp)
      div = socket_server_temp.div(number2,number3)
      print number2, " / " , number3, " = ", div
      print("CHAU!")
      exit = True
    elif int(number1) == 5:
      number1 = int(number1)
      number2 = raw_input('Input the first number (base): ')
      number3 = raw_input('Input the second number (exponent): ')
      http_temp = socket_server_mid.receive(number1)
      number2 = int(number2)
      number3 = int(number3)
      socket_server_temp = xmlrpclib.ServerProxy(http_temp)
      powe = socket_server_temp.pow(number2,number3)
      print number2, " ^ " , number3, " = ", powe
      print("CHAU!")
      exit = True
    elif int(number1) == 6:
      number1 = int(number1)
      number2 = raw_input('Input the first number (index): ')
      number3 = raw_input('Input the second number (base): ')
      http_temp = socket_server_mid.receive(number1)
      number2 = float(number2)
      number3 = float(number3)
      socket_server_temp = xmlrpclib.ServerProxy(http_temp)
      sqr = socket_server_temp.sqr(number2,number3)
      print number3,"^","("," 1/" , number2,")", " = ", sqr
      print("CHAU!")
      exit = True
    elif int(number1) == 7:
      number1 = int(number1)
      number2 = raw_input('Input the first number: ')
      number3 = raw_input('Input the second number: ')
      http_temp = socket_server_mid.receive(number1)
      number2 = float(number2)
      number3 = float(number3)
      socket_server_temp = xmlrpclib.ServerProxy(http_temp)
      loga = socket_server_temp.log(number2,number3)
      print " Log base ", number2," de ", number3, " = ", loga
      print("CHAU!")
      exit = True
    elif int(number1) == 8:
      print("CHAU!")
      exit = True
  else: 
    print "No valid option CHAU!"
    exit = True

