import pygame
import Client
import SocketServer

print (__name__)

class Server(SocketServer.BaseRequestHandler):
    
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        #print "{} wrote:".format(self.client_address[0])
        #print self.data
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())
        
    def __init__(self, socket):
        HOST, PORT = "localhost", socket
        self.server = SocketServer.TCPServer((HOST, PORT), Server)
        self.server.serve_forever()
        self.server.shutdown()
    
    def StopGame(self):
        self.shutdown()
    
        
        