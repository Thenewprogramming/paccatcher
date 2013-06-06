import pygame
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def ConnectToServer(serverIp):
    global HOST, PORT, sock
    HOST = serverIp
    PORT = 9999
    sock.connect(("145.120.120.25", 2345))
    sock.sendall("hallo".encode(encoding='utf_8', errors='strict'))
    print ("yay")
    print (type(sock.recv(1024).decode("utf-8")))
    
def CloseConnection():
    
    sock.close()

if __name__ == "__main__":
    ConnectToServer("10.16.128.67")
    CloseConnection()