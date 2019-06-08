from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

def sub(x, y):
    return x - y

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

def main():

  server = SimpleXMLRPCServer(("localhost", 8002),requestHandler = RequestHandler)
  server.register_introspection_functions()
  server.register_function(sub,'sub')
  if server:
    print "Server Sub On!"
    server.serve_forever()

main()