from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

def sum_(x, y):
    return x + y

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

def main():

  server = SimpleXMLRPCServer(("localhost", 8001),requestHandler = RequestHandler)
  server.register_introspection_functions()
  server.register_function(sum_,'add')
  if server:
    print "Server Sum On!"
    server.serve_forever()

main()