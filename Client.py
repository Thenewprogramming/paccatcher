import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def ConnectToServer(serverIp, port):
    global HOST, PORT, sock
    HOST = serverIp
    PORT = port
    sock.connect((HOST, PORT))
    
def CloseConnection():
    sock.close()

def SendMessage(message):
    global HOST, PORT
    sock.sendto(message.encode(), (HOST,PORT))
    print(sock.recv(1024).decode())

if __name__ == "__main__":
    # a little debugging
    ConnectToServer("localhost", 1234)
    SendMessage("herpaderp")
    CloseConnection()