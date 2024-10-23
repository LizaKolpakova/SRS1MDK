import socket
import threading

def receive_messages(client):
    message = client.recv(1024).decode()
    if message:
       print(message)
    client.close()


client = socket.socket()
hostname = socket.gethostname()
port = 12345
client.connect((hostname, port))

threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

while True:
    message = input()
    client.send(message.encode())