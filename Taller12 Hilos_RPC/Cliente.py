# cd Desktop\Sistemas distribuidos\Taller12 Hilos_RPC
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
      time.sleep(1)
      print 'taller 10 Hilos/RPC'
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
            dir_server_sum = self.client.server_sum()
            client_sum = xmlrpclib.ServerProxy('http://localhost:'+ dir_server_sum)
            print number2, " + " , number3, " = ", client_sum.sum_(number2,number3)
          elif int(number1) == 2:
            number2 = raw_input('Input the first number: ')
            number3 = raw_input('Input the second number: ')
            dir_server_sub = self.client.server_substraction()
            client_sub = xmlrpclib.ServerProxy('http://localhost:'+ dir_server_sub)
            print number2, " - " , number3, " = ", client_sub.sub(number2,number3)
          elif int(number1) == 3:
            number2 = raw_input('Input the first number: ')
            number3 = raw_input('Input the second number: ')
            dir_server_mul = self.client.server_multiplication()
            client_mul = xmlrpclib.ServerProxy('http://localhost:'+ dir_server_mul)
            print number2, " * " , number3, " = ", client_mul.mul(number2,number3)
          elif int(number1) == 4:
            number2 = raw_input('Input the first number: ')
            number3 = raw_input('Input the second number: ')
            dir_server_div = self.client.server_division()
            client_div = xmlrpclib.ServerProxy('http://localhost:'+ dir_server_div)
            print number2, " / " , number3, " = ", client_div.div(number2,number3)
          elif int(number1) == 5:
            number2 = raw_input('Input the first number (base): ')
            number3 = raw_input('Input the second number (exponent): ')
            dir_server_pow = self.client.server_power()
            client_pow = xmlrpclib.ServerProxy('http://localhost:'+ dir_server_pow)
            print number2, " ^ " , number3, " = ", client_pow.powe(number2,number3)
          elif int(number1) == 6:
            number2 = raw_input('Input the first number (index): ')
            number3 = raw_input('Input the second number (base): ')
            dir_server_sqr = self.client.server_enesim_square()
            client_sqr = xmlrpclib.ServerProxy('http://localhost:'+ dir_server_sqr)
            print number3, " ^ " ,"1 / ", number2, " = ", client_sqr.enesim_square(number2,number3)
          elif int(number1) == 7:
            number2 = raw_input('Input the first number (index): ')
            number3 = raw_input('Input the second number (base): ')
            dir_server_log = self.client.server_base_n_logarithm()
            client_log = xmlrpclib.ServerProxy('http://localhost:'+ dir_server_log)
            print number2, " log " , number3, " = ", client_log.base_n_logarithm(number2,number3)
          elif int(number1) == 8:
            print("CHAU!")
            exit = True
        else: 
          number1 = 8

client = ClientThread()
client.start()