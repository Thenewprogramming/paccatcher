import socketserver

class Server(socketserver.BaseRequestHandler):
    
    def handle(self):
        self.data = self.request.recv(4096)
        print(self.data.decode())
        self.request.sendto(self.data.upper(), self.client_address)

def startserver(port):
    global server
    HOST, PORT = "", port
    server = socketserver.TCPServer((HOST, PORT), Server)
    print("Starting server on port " + str(PORT))
    server.serve_forever()

def stopserver():
    global server
    server.shutdown()

if __name__ == "__main__":
    # a little debugging
    startserver(1111)