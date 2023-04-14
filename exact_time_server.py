import datetime
import socket


class ExactTimeServer():
    def __init__(self):
        self.host = 'localhost'
        self.port = 123
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.time_offset = int(open('configuration').readline())

    def run(self):
        self.s.bind((self.host, self.port))
        self.s.listen(1)
        while True:
            conn, addr = self.s.accept()
            data = conn.recv(1024).decode()
            if not data:
                self.s.close()
            if data == 'get time':
                conn.sendall(self.get_time().encode())

    def get_time(self):
        return (datetime.datetime.now() + datetime.timedelta(seconds=self.time_offset)).strftime('%H:%M:%S')


if __name__ == '__main__':
    server = ExactTimeServer()
    server.run()
