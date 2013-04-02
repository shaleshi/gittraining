import SimpleHTTPServer
import SocketServer

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)
print dir(httpd)
print "serving at port", PORT
httpd.serve_forever()
httpd.server_close()

