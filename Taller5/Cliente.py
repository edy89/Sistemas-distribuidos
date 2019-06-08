import xmlrpclib


print 'taller 4'
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
      number2 = raw_input('Input the first number: ')
      number3 = raw_input('Input the second number: ')
      number2 = int(number2)
      number3 = int(number3)
      socket_sum = xmlrpclib.ServerProxy('http://localhost:8000')
      add = socket_sum.add(number2,number3)
      print number2, " + " , number3, " = ", add
      print("CHAU!")
      exit = True
    elif int(number1) == 2:
      number2 = raw_input('Input the first number: ')
      number3 = raw_input('Input the second number: ')
      number2 = int(number2)
      number3 = int(number3)
      socket_sub = xmlrpclib.ServerProxy('http://localhost:8000')
      sub = socket_sub.sub(number2,number3)
      print number2, " - " , number3, " = ", sub
      print("CHAU!")
      exit = True
    elif int(number1) == 3:
      number2 = raw_input('Input the first number: ')
      number3 = raw_input('Input the second number: ')
      number2 = int(number2)
      number3 = int(number3)
      socket_mul = xmlrpclib.ServerProxy('http://localhost:8000')
      mul = socket_mul.mul(number2,number3)
      print number2, " * " , number3, " = ", mul
      print("CHAU!")
      exit = True
    elif int(number1) == 4:
      number2 = raw_input('Input the first number (numerador): ')
      number3 = raw_input('Input the second number (denominador): ')
      number2 = float(number2)
      number3 = float(number3)
      socket_div = xmlrpclib.ServerProxy('http://localhost:8000')
      div = socket_div.div(number2,number3)
      print number2, " / " , number3, " = ", div
      print("CHAU!")
      exit = True
    elif int(number1) == 5:
      number2 = raw_input('Input the first number (base): ')
      number3 = raw_input('Input the second number (exponent): ')
      number2 = int(number2)
      number3 = int(number3)
      socket_pow = xmlrpclib.ServerProxy('http://localhost:8000')
      powe = socket_pow.powe(number2,number3)
      print number2, " ^ " , number3, " = ", powe
      print("CHAU!")
      exit = True
    elif int(number1) == 6:
      number2 = raw_input('Input the first number (index): ')
      number3 = raw_input('Input the second number (base): ')
      number2 = float(number2)
      number3 = float(number3)
      socket_sqr = xmlrpclib.ServerProxy('http://localhost:8000')
      sqr = socket_sqr.sqr(number2,number3)
      print number3,"^","("," 1/" , number2,")", " = ", sqr
      print("CHAU!")
      exit = True
    elif int(number1) == 7:
      number2 = raw_input('Input the first number: ')
      number3 = raw_input('Input the second number: ')
      number2 = float(number2)
      number3 = float(number3)
      socket_log = xmlrpclib.ServerProxy('http://localhost:8000')
      loga = socket_log.loga(number2,number3)
      print " Log base ", number2," de ", number3, " = ", loga
      print("CHAU!")
      exit = True
    elif int(number1) == 8:
      print("CHAU!")
      exit = True
  else: 
    print "No valid option CHAU!"
    exit = True

