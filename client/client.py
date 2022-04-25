from socket import socket


class Client:
    def __init__(self, address, port):
        self.socket = socket()
        self.socket.connect((address, port))

    def read(self):
        return self.socket.recv(1024).strip().decode()

    def write(self, command):
        if not command.endswith('\n'):
            command += '\n'
        self.socket.sendall(command.encode())

    def query(self, command):
        self.write(command)
        return self.read()

    def close(self):
        self.socket.close()
