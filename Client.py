import socket


def connect(ip, port=12345):
    global HOST, PORT, s
    HOST = ip
    PORT = port
    s = socket.socket()
    s.connect((HOST, PORT))


def sendMsg(msg):
    s.send((msg + "\r\n").encode())


def ready(name):
    msg = "READY/" + name
    sendMsg(msg)


def recv():
    return s.recv(1024).decode()

if __name__ == "__main__":
    connect("localhost")
    sendMsg("bladibladibla")
    while True:
        print(recv())
