import socket


class Client:
    def __init__(self):
        self.host = 'localhost'
        self.port = 123
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def open_connection(self):
        self.s.connect((self.host, self.port))

    def get_time(self):
        self.s.sendall('get time'.encode('utf-8'))
        while True:
            data = self.s.recv(1024)
            if not data:
                break
            print(data.decode())

    def close_connection(self):
        self.s.close()


if __name__ == '__main__':
    client = Client()
    client.open_connection()
    client.get_time()
    client.close_connection()
