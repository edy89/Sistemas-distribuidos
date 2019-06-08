import socket

print 'taller 7 hilos'
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(('localhost',8557))
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
      numbers = number1 + "," + number2 + "," + number3
      print "Parameters of send: ",numbers.split(",")
      socket.send(numbers)
      add = socket.recv(1024)
      print number2, " + " , number3, " = ", add
      #socket.close ()
      print("CHAU!")
      exit = True
    elif int(number1) == 2:
      number2 = raw_input('Input the first number: ')
      number3 = raw_input('Input the second number: ')
      numbers = number1 + "," + number2 + "," + number3
      print "Parameters of send: ",numbers.split(",")
      socket.send(numbers)
      sub = socket.recv(1024)
      print number2, " - " , number3, " = ", sub
      print("CHAU!")
      exit = True
    elif int(number1) == 3:
      number2 = raw_input('Input the first number: ')
      number3 = raw_input('Input the second number: ')
      numbers = number1 + "," + number2 + "," + number3
      print "Parameters of send: ",numbers.split(",")
      socket.send(numbers)
      mul = socket.recv(1024)
      print number2, " * " , number3, " = ", mul
      print("CHAU!")
      exit = True
    elif int(number1) == 4:
      number2 = raw_input('Input the first number: ')
      number3 = raw_input('Input the second number: ')
      numbers = number1 + "," + number2 + "," + number3
      print "Parameters of send: ",numbers.split(",")
      socket.send(numbers)
      div = socket.recv(1024)
      print number2, " / " , number3, " = ", div
      print("CHAU!")
      exit = True
    elif int(number1) == 5:
      number2 = raw_input('Input the first number (base): ')
      number3 = raw_input('Input the second number (exponent): ')
      numbers = number1 + "," + number2 + "," + number3
      print "Parameters of send: ",numbers.split(",")
      socket.send(numbers)
      powe = socket.recv(1024)
      print number2, " ^ " , number3, " = ", powe
      print("CHAU!")
      exit = True
    elif int(number1) == 6:
      number2 = raw_input('Input the first number (square): ')
      number3 = raw_input('Input the second number (base): ')
      numbers = number1 + "," + number2 + "," + number3
      print "Parameters of send: ",numbers.split(",")
      socket.send(numbers)
      sqr = socket.recv(1024)
      print number3, " ^ 1 / " , number2, " = ", sqr
      print("CHAU!")
      exit = True
    elif int(number1) == 7:
      number2 = raw_input('Input the first number (base): ')
      number3 = raw_input('Input the second number : ')
      numbers = number1 + "," + number2 + "," + number3
      print "Parameters of send: ",numbers.split(",")
      socket.send(numbers)
      log = socket.recv(1024)
      print " Log base ", number2," de ", number3, " = ", log
      print("CHAU!")
      exit = True
    elif int(number1) == 8:
      print("CHAU!")
      exit = True
  else: 
    print "No valid option CHAU!"
    exit = True

