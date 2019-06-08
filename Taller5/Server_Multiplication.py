from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

def mul(x, y):
    return x * y

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

def main():

  server = SimpleXMLRPCServer(("localhost", 8003),requestHandler = RequestHandler)
  server.register_introspection_functions()
  server.register_function(mul,'mul')
  if server:
    print "Server Mul On!"
    server.serve_forever()

main()