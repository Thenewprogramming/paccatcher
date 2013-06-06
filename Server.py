import socketserver

print (__name__)

class Server(socketserver.BaseRequestHandler):
    
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        #print "{} wrote:".format(self.client_address[0])
        #print self.data
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

server = None

def startserver(port):
    global server
    HOST, PORT = "localhost", port
    server = socketserver.TCPServer((HOST, PORT), Server)
    server.serve_forever()

def stopserver():
    global server
    server.shutdown()