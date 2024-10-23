import socket
from _thread import *

clients = []

def client_thread(conn, addr):
        message = conn.recv(1024).decode()
        if message:
                print(f"[{addr}] {message}")
                broadcast(message, conn)
    
def broadcast(message, connection):
    for client in clients:
        if client != connection:
            client.send(message.encode())

server = socket.socket()
hostname = socket.gethostname()
port = 12345
server.bind((hostname, port))
server.listen(5)

print("Server running...")

while True:
    conn, addr = server.accept()
    clients.append(conn)
    print(f"New connection: {addr}")
    start_new_thread(client_thread, (conn, addr,))