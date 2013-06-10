import socket


def ConnectToServer():
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))


def CloseConnection():
    sock.close()


def SetAdress(host, port):
    global HOST, PORT
    HOST = host
    PORT = port


def SendMessage(message):
    ConnectToServer()
    sock.sendto(message.encode(), (HOST, PORT))
    response = sock.recv(1024).decode()
    CloseConnection()
    return response

if __name__ == "__main__":
    # a little debugging
    SetAdress("localhost", 1111)
    print(SendMessage("herpaderp"))
