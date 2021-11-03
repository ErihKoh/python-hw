import socket
import threading
from env import HOST, PORT


def listen_server(sock):
    while True:
        data = sock.recv(1024)
        print(data.decode('utf-8'))


def send_to_server():
    with socket.socket() as sock:
        sock.connect((HOST, PORT))
        listen_thread = threading.Thread(target=listen_server, args=(sock,))
        listen_thread.start()
        while True:
            sock.send(input().encode('utf-8'))


if __name__ == '__main__':
    send_to_server()
