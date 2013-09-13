from socket import socket
from threading import Thread


class server():
    def __init__(self, port=12345):
        self.s = s = socket()
        s.bind(("", port))
        self.connected = []
        self.stop = False
        self.thread = Thread(target=self.listen)
        self.thread.start()

    def __call__(self, val):
        try:
            return self.connected[val]
        except IndexError:
            return None

    def isdone(self):
        return self.stop

    def listen(self):
        print("Starting server...")
        self.s.listen(3)
        while not self.stop:
            conn, addr = self.s.accept()
            server = serveclient(conn, addr)
            self.connected += [server]
            if len(self.connected) >= 3:
                self.stop = True


class serveclient():
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
        self.stop = False
        self.name = None
        self.thread = Thread(target=self.handle)
        self.thread.start()

    def handle(self):
        while not self.stop:
            data = self.conn.recv(1024).decode()
            if not data:
                print(self.addr, "Disconnected")
                break
            print(self.addr, "sent:", data)
            data = data.split("/")
            if data[0] == "READY":
                self.name = data[1]
            self.conn.send("Got it!\r\n".encode())

if __name__ == "__main__":
    serv = server()
    while True:
        if serv.isdone():
            break
    for thing in serv.connected:
        print(thing.name)
