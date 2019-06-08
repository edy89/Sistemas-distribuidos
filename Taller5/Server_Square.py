from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler


def enesim_square(x, y):
  return pow(y, (1.0/x))


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

def main():

  server = SimpleXMLRPCServer(("localhost", 8006),requestHandler = RequestHandler)
  server.register_introspection_functions()
  server.register_function(enesim_square,'sqr')
  #server.register_function(div,'div')
  if server:
    print "Server Sqr On!"
    server.serve_forever()

main()