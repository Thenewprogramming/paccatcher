import socket


def connect(ip, port):
    global HOST, PORT, s
    HOST = ip
    PORT = port
    s = socket.socket()
    s.connect((HOST, PORT))


def sendMsg(msg):
    s.send((msg + "\r\n").encode())


def ready(name):
    msg = "READY " + name
    sendMsg(msg)


def recv():
    return s.recv(1024).decode()
