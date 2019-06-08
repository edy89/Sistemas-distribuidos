#cd downloads/Test/taller1/
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import SocketServer
import SimpleXMLRPCServer
import sys
import threading
import xmlrpclib
import time

class ClientThread(threading.Thread):
    def __init__(self):
      threading.Thread.__init__(self)
      self.client = xmlrpclib.ServerProxy('http://localhost:8557')

    def run(self):
      time.sleep(3)
      print 'taller 1 Hilos/RPC'
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
          #socket1.send(number1)

          if int(number1) == 1:
            number2 = raw_input('Input the first number: ')
            number3 = raw_input('Input the second number: ')
            print number2, " + " , number3, " = ", self.client.sum_(int(number2),int(number3))
          elif int(number1) == 2:
            number2 = raw_input('Input the first number: ')
            number3 = raw_input('Input the second number: ')
            print number2, " - " , number3, " = ", self.client.substraction(int(number2),int(number3))
          elif int(number1) == 3:
            number2 = raw_input('Input the first number: ')
            number3 = raw_input('Input the second number: ')
            print number2, " * " , number3, " = ", self.client.multiplication(int(number2),int(number3))
          elif int(number1) == 4:
            number2 = raw_input('Input the first number: ')
            number3 = raw_input('Input the second number: ')
            print number2, " / " , number3, " = ", self.client.division(float(number2),float(number3))
          elif int(number1) == 5:
            number2 = raw_input('Input the first number (base): ')
            number3 = raw_input('Input the second number (exponent): ')
            print number2, " ^ " , number3, " = ", self.client.power(int(number2),int(number3))
          elif int(number1) == 6:
            number2 = raw_input('Input the first number (index): ')
            number3 = raw_input('Input the second number (base): ')
            print number3, " ^ " ,"1 / ", number2, " = ", self.client.enesim_square(float(number2),float(number3))
          elif int(number1) == 7:
            number2 = raw_input('Input the first number (index): ')
            number3 = raw_input('Input the second number (base): ')
            print number2, " log " , number3, " = ", self.client.base_n_logarithm(int(number2),int(number3))
          elif int(number1) == 8:
            print("CHAU!")
            exit = True
        else: 
          number1 = 8

client = ClientThread()
client.start()