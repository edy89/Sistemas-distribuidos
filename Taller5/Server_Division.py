from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler


def division(x, y):
    return x / y


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

def main():

  server = SimpleXMLRPCServer(("localhost", 8004),requestHandler = RequestHandler)
  server.register_introspection_functions()
  server.register_function(division,'div')
  if server:
    print "Server Div On!"
    server.serve_forever()

main()