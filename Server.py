import socketserver
import pygame
class Server():
    
    server = None

    def startserver(self, port, ghosts):
        
        HOST, PORT = "", port
        self.server = socketserver.TCPServer(("", 1234), ServerHandler)
        print("Starting server on port " + str(PORT))
        self.server.serve_forever()
        self.ghosts = ghosts
        
    
    def stopserver(self):
        
        self.server.shutdown()
    
    def processkeypress(self, key):
        pos = [0,0]
        if (key == str(pygame.K_DOWN)):
            pos[1] += 1
            pos[1] += self.ghosts[0].getpos()[1]
            
        if (key == str(pygame.K_UP)):
            pos[1] -= 1
            pos[1] += self.ghosts[0].getpos()[1]
            
        if (key == str(pygame.K_RIGHT)):
            pos[0] += 1
            pos[0] += self.ghosts[0].getpos()[0]
            
        if (key == str(pygame.K_LEFT)):
            pos[0] -= 1
            pos[0] += self.ghosts[0].getpos()[0]
            
        return pos
            
    
class ServerHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        self.data = self.request.recv(4096)
        print("Client sent" + self.data.decode() + ". Now figuring out what to do with it..." )
        
        pos = Server.processkeypress(Server, self.data.decode())
#         if (self.data.decode() == str(pygame.K_DOWN)):
#             pos = Server.processkeypress(Server, self.data.decode())
#             
#         if (self.data.decode() == str(pygame.K_UP)):
#             pos = Server.processkeypress(Server, self.data.decode())
#             
#         if (self.data.decode() == str(pygame.K_RIGHT)):
#             pos = Server.processkeypress(Server, self.data.decode())
#             
#         if (self.data.decode() == str(pygame.K_LEFT)):
#             pos = Server.processkeypress(Server, self.data.decode())
            
        sendData = str(pos[0]) + ":" + str(pos[1])
        self.request.sendto(sendData.encode(), self.client_address)
        
if __name__ == "__main__":
#     a little debugging
    Server.startserver(1111)
