# cd Desktop\Sistemas distribuidos\Final\PC1
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import SocketServer
import SimpleXMLRPCServer
import sys
import threading
import xmlrpclib
import time
import os.path

print 'Proyecto Final'

class page:
  def __init__(self,name,id):
    self.id   = id
    self.name = name
    self.page = open(name,'w')
    self.page.close()
    self.state = True

  def state_(self):
    return self.state

  def write_(self,content):
    self.page = open(self.name,'w')
    self.page.write(content)
    self.page.close()

class ClientThread(threading.Thread):

    def __init__(self):

      threading.Thread.__init__(self)
      self.client  = xmlrpclib.ServerProxy('http://localhost:8557',allow_none = True)
      self.id      = 1
      self.page1   = page('page1.txt',1)
      self.page2   = page('page2.txt',2)
      self.page1.write_('Page1 : PC1 \n')
      self.page2.write_('Page2 : PC1 \n')
      self.register   = open ('register.txt','w')
      self.register.write('register: ')
      self.register.close()
      self.client.catch_page('C:/Users/Edyson/Desktop/Sistemas distribuidos/Final/PC1/page1.txt',self.id,self.page1.id)
      self.client.catch_page('C:/Users/Edyson/Desktop/Sistemas distribuidos/Final/PC1/page2.txt',self.id,self.page2.id)

     
    def run(self):
      time.sleep(1)
      exit = False      
      
      
      while not exit:

        print ("\n WELCOME TO OPTIONS MENU \n")
        print ("Press D to display the available pages from all PC's \n")
        print ("Press W to write on any page \n")
        print ("Press R to display the register file \n")
        print ("Press E to Exit \n")

        opd = raw_input('Input option you want to realize: ')

        if opd == 'd' or opd == 'r' or opd == 'w' or opd == 'e':

          if opd == 'd':
           
           all_pages = self.client.get_all_pages()
           
           for item in all_pages:
            file = open(item[0],'r')
            linesFile = file.readlines()
            for line in linesFile:
               print line
            file.close()           
          
          elif opd == 'w':

           exit2 = True
           print ("\n Select any PC to read one of his pages \n")
           print ("\n -------------------- PC'S ------------------ \n")
           print ("\n 1. PC1\n")
           print ("\n 2. PC2\n")
           print ("\n 3. PC3\n")

           pc = raw_input('Input your choice: ')
           while exit2:
             if pc == '1' or pc == '2' or pc == '3':
              
               print ("\n -------------------- PAGES ------------------ \n")
               pages_pc =  self.client.pool_pages_pc(pc)
               cont = 1

               for page in pages_pc:
                 file = open(page,'r')
                 linesFile = file.readline()
                 print cont,'.',linesFile
                 cont += 1
               file.close()

               opage = raw_input("Select some page: ")
               
               if  int(opage) <= len(pages_pc):
                 if not self.client.is_used(int(pc),int(opage)):
                   self.client.add_page_p(int(pc),int(opage))
                   file = open(pages_pc[int(opage) - 1],'r+')
                   content = file.readlines()
                   #file.write('page' + opage + ':PC1')
                   #file.close()                   
                   input_ = raw_input('write content for page: \n')
                   #file = open(pages_pc[int(opage) - 1],'w')
                   file.write(content[0] + input_)
                   file.close()
                   self.client.del_page_p(int(pc),int(opage))
                   self.client.register_in(int(pc),int(opage),'http://localhost:8557')
                 else:
                   print 'The page you need is not available rigth now, wait for it...'
                   temp = self.client.put_in_queue('http://localhost:8557',int(pc),int(opage))
                   self.client.add_page_p(int(pc),int(opage))
                   file = open(pages_pc[int(opage) - 1],'r+')
                   content = file.readlines()
                   #file.write('page' + opage + ':PC1')
                   #file.close()                   
                   input_ = raw_input('write content for page: \n')
                   #file = open(pages_pc[int(opage) - 1],'w')
                   file.write(content[0] + input_)
                   file.close()
                   self.client.del_page_p(int(pc),int(opage))
                   self.client.register_in(int(pc),int(opage),'http://localhost:8557')
 
               else:
                   print("Press a valid option please!!!")

               exit2 = False

             else:
               print "Press a valid option please"
               exit2 = False
        
          elif opd == 'r':

            file = open('register.txt','r')
            linesFile_t = file.readlines()
            for line in linesFile_t:
               print line

          elif opd == 'e':
           print("CHAU!")
           exit = True
        
        else: 
          print "Press a valid option please"

client = ClientThread()
client.start()