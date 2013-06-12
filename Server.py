import socketserver


class Server():
    
    server = None

    def startserver(self, port):
        
        HOST, PORT = "", port
        self.server = socketserver.TCPServer(("", 1234), ServerHandler)
        print("Starting server on port " + str(PORT))
        self.server.serve_forever()
        
    
    def stopserver(self):
        
        self.server.shutdown()
        
class ServerHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        self.data = self.request.recv(4096)
        print("Client sent" + self.data.decode() + ". Now figuring out what to do with it...")
        if (self.data.decode == "playerpositionsplease"):
            pass
        self.request.sendto(self.data.upper(), self.client_address)
        
if __name__ == "__main__":
#     a little debugging
    Server.startserver(1111)
