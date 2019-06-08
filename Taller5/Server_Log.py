from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import math

def base_n_logarithm(x, y):
    return math.log(x,y)


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

def main():

  server = SimpleXMLRPCServer(("localhost", 8007),requestHandler = RequestHandler)
  server.register_introspection_functions()
  server.register_function(base_n_logarithm,'loga')
  #server.register_function(div,'div')
  if server:
    print "Server Log On!"
    server.serve_forever()

main()