import socket
import threading


def init(port=1235):
    global s
    print("Starting server on port:", port)
    s = socket.socket()
    s.bind(("", port))
    s.listen(0)


def start(self):
    while True:
        conn, addr = s.accept()
        print(addr, "connected")
        threading.Thread(target=self.serveclient, args=(conn, addr)).start()


def serveclient(self, conn, addr):
    while True:
        data = conn.recv(1024).decode()
        if not data:
            print(addr, "Disconnected")
            break
        print(addr, "sent:", data)
        conn.send("Got it!\r\n".encode())
    conn.close()
