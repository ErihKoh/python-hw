import socket
import threading
from env import HOST, PORT


def send_all(data, users):
    for user in users:
        user.send(data)


def listen_user(user, users):
    while True:
        data = user.recv(1024)
        print(f"User sent {data}")

        send_all(data, users)


def start_server():
    users = []
    with socket.socket() as sock:
        sock.bind((HOST, PORT))
        sock.listen(5)
        print("Server started!")
        while True:
            user_data, address = sock.accept()
            print(f"User with {address[0]}, connected")
            users.append(user_data)
            listening_user = threading.Thread(target=listen_user, args=(user_data, users))
            listening_user.start()


if __name__ == '__main__':
    start_server()
