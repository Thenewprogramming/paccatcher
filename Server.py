import socketserver
import pygame
class Server():
    
    server = None

    def startserver(self, port):
        
        HOST, PORT = "", port
        self.server = socketserver.TCPServer(("", 1234), ServerHandler)
        print("Starting server on port " + str(PORT))
        self.server.serve_forever()
        
    
    def stopserver(self):
        
        self.server.shutdown()
    
    def processkeypress(self, key):
        pass
    
class ServerHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        self.data = self.request.recv(4096)
        print("Client sent" + self.data.decode() + ". Now figuring out what to do with it..." )
        
        if (self.data.decode() == str(pygame.K_DOWN) | self.data.decode() == str(pygame.K_UP) | self.data.decode() == str(pygame.K_LEFT) | self.data.decode() == str(pygame.K_RIGHT) ):
            Server.processkeypress(self.data.decode())
        
        
        self.request.sendto(self.data.upper(), self.client_address)
        
if __name__ == "__main__":
#     a little debugging
    Server.startserver(1111)
