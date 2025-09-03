import socket
from threading import Thread
import os

class Client:
    def __init__(self, HOST, PORT):

        self.socket = socket.socket()
        self.socket.connect((HOST, PORT))

        self.talk_to_server()

    def talk_to_server(self):
        Thread(target=self.receive_message, args=(self.socket,)).start()
        self.send_message(self.socket)


    def send_message(self, client_socket):
        while True:
            server_message = input("")
            client_socket.send(server_message.encode())

    def receive_message(self, client_socket):
        while True:
            client_message = client_socket.recv(1024).decode()
            if (client_message.strip() == "bye" or not client_message.strip()):
                os._exit(0)
            print("\033[1;31;40m" + "Server: " + client_message + "\033[0m")

    
Client('127.0.0.1', 2025)