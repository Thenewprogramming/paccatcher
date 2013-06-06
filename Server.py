import socketserver

print (__name__)

class Server(socketserver.BaseRequestHandler):
    
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(4096)
        print(self.data)
        #print "{} wrote:".format(self.client_address[0])
        #print self.data
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())
        
        print (self.data.decode("utf-8"))

server = None

def startserver():
    
    global server
    HOST, PORT = "", 2345
    server = socketserver.TCPServer((HOST, PORT), Server)
    server.serve_forever()

def stopserver():
    global server
    server.shutdown()