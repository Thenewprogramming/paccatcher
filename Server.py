import socketserver

server = None

class Server(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(4096)
        print("Client sended" + self.data.decode() + ". Now figuring out what to do with it...")
        if (self.data.decode == "playerpositionsplease"):
            pass
        self.request.sendto(self.data.upper(), self.client_address)


def startserver(port):
    
    HOST, PORT = "", port
    server = socketserver.TCPServer((HOST, PORT), Server)
    print("Starting server on port " + str(PORT))
    server.serve_forever()
    

def stopserver():
    
    server.shutdown()

if __name__ == "__main__":
    # a little debugging
    startserver(1111)
