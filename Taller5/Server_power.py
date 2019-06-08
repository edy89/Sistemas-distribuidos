from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

def main():

  server = SimpleXMLRPCServer(("localhost", 8005),requestHandler = RequestHandler)
  server.register_introspection_functions()
  server.register_function(pow)
  #server.register_function(div,'div')
  if server:
    print "Server Pow On!"
    server.serve_forever()

main()