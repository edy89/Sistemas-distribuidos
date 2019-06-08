# cd Desktop\Sistemas distribuidos\Final
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import SocketServer
import SimpleXMLRPCServer
import sys
import threading
import xmlrpclib
from collections import deque


def main():
  pcs_queue = deque([])
  all_pages   = []
  all_pcs     = []
  pages_queue = []

  def catch_page(y,z,w):
    temp_bool = False
    temp = []
    for page in all_pages:
      if page[0] == y:
        temp_bool = True
    if temp_bool == False:
      temp = [y,z,w]
      all_pages.append(temp)   
    
  def add_page_p(x,y):
    temp2 = [x,y]
    print pages_queue
    pages_queue.append(temp2)
    print pages_queue

  def del_page_p(x,y):
    cont = 0
    for page in pages_queue:
      if page[0] == x and page[1] == y:
        pages_queue.pop(cont)

      cont += 1

  def is_used(x,y):
    temp_bool2 = False
    for page in pages_queue:
      if page[0] == x and page[1] == y:
        temp_bool2 = True
    return temp_bool2

  def get_all_pages():
    return all_pages

  def pool_pages_pc(pc):
    temp_pages = []
    for page  in all_pages:
      if page[1] == int(pc):
        temp_pages.append(page[0])
    return temp_pages

  def put_in_queue(x,y,z):
    pcs_queue.append(x)
    temp = True
    while temp:
      temp = is_used(y,z)
      if not temp:
        pcs_queue.popleft()        
    return temp

  def register_in(x,y,z):
    for page in all_pages:
      if page[1] == x and page[2] == y:
        str_temp = page[0][:56] + 'register.txt'
        file = open(str_temp,'r+')
        conte = file.readlines()
        file.write(' ')
        file.close()
        file = open(str_temp,'w')
        file.write(conte[0] + z + '|')
        file.close()


  class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

         
  class SimpleThreadedXMLRPCServer(SocketServer.ThreadingMixIn, SimpleXMLRPCServer.SimpleXMLRPCServer):
      pass

  class ClientThread(threading.Thread):
      def __init__(self, num, addr):
          threading.Thread.__init__(self)
          self.num = num
          self.localServer = SimpleThreadedXMLRPCServer(("localhost",addr),allow_none = True)
          self.localServer.register_function(catch_page)
          self.localServer.register_function(get_all_pages)
          self.localServer.register_function(pool_pages_pc)
          self.localServer.register_function(add_page_p)
          self.localServer.register_function(del_page_p)
          self.localServer.register_function(is_used)
          self.localServer.register_function(put_in_queue)
          self.localServer.register_function(register_in)

          
      def run(self):
          self.localServer.serve_forever()
          sys.stdout.write("Server with Hilo %d\n" % self.num)
        
               
      

  client_thread1 = ClientThread(1,8557)
  client_thread2 = ClientThread(2,8558)
  client_thread3 = ClientThread(3,8559)
  
     
  if client_thread1 and client_thread2 and client_thread3 :
      print "Ready"
      client_thread1.start()
      client_thread2.start()
      client_thread3.start()

main()