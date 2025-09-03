import socket
from threading import Thread
import os

class Server:
    def __init__(self, HOST, PORT):

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((HOST, PORT))

        self.socket.listen()
        print('Waiting for connection from client...')

        client_socket, address = self.socket.accept()
        print("Connection from: " + str(address) + " established")

        self.talk_to_client(client_socket)

    def talk_to_client(self, client_socket):
        Thread(target=self.receive_message, args=(client_socket,)).start()
        self.send_message(client_socket)

    def send_message(self, client_socket):
        while True:
            server_message = input("")
            client_socket.send(server_message.encode())

    def receive_message(self, client_socket):
        while True:
            client_message = client_socket.recv(1024).decode()
            if (client_message.strip() == "bye" or not client_message.strip()):
                os._exit(0)
            print("\033[1;31;40m" + "Client: " + client_message + "\033[0m")

Server ('127.0.0.1', 7632)