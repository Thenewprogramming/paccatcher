"""
Needs rewriting
"""

import socketserver
import pygame
import Game

def startserver(port):
    global server
    HOST, PORT = "", port
    server = socketserver.TCPServer(("", 1234), ServerHandler)
    print("Starting server on port " + str(PORT))
    server.serve_forever()

def stopserver():
    global server
    server.shutdown()
    
class ServerHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        self.data = self.request.recv(4096).decode().split(":")
        self.request.sendto(sendData.encode(), self.client_address)
