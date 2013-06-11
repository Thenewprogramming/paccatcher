import socketserver


class Server(socketserver.BaseRequestHandler):
    
    server = None

    def __init__(self):
#         self.server = None
        pass
    
    def handle(self):
        self.data = self.request.recv(4096)
        print("Client sended" + self.data.decode() + ". Now figuring out what to do with it...")
        if (self.data.decode == "playerpositionsplease"):
            pass
        self.request.sendto(self.data.upper(), self.client_address)


    def startserver(self, port):
        
        HOST, PORT = "", port
        self.server = socketserver.TCPServer(("", 1234), Server)
        print("Starting server on port " + str(PORT))
        self.server.serve_forever()
        
    
    def stopserver(self):
        
        self.server.shutdown()
    
if __name__ == "__main__":
#     a little debugging
    Server.startserver(1111)
