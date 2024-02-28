import socket
import json
import threading

# Define host and port
SERVER = socket.gethostbyname(socket.gethostname()) 
PORT = 8080        
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "DISCONNECT_TRUE"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION]... (address = {addr})")

    connection = True
    while connection:
        msg_lenght = conn.recv(HEADER).decode(FORMAT)
        if msg_lenght:
            pass
        else:
            continue
        msg_lenght = int(msg_lenght)
        msg = conn.recv(msg_lenght).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connection = False
        print(f"[MESSAGE] (content = {msg}, address = {addr})")
    
    conn.close()




def start(server : socket.socket):
    print(f"[LISTENING].. (state = server is listening for connections, server = {SERVER})")
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args = (conn, addr))
        thread.start()

        print(f"[THREAD-STARTING]... (state = thread starting, clinets = {(threading.active_count()) - 1})")
        
        




print("[STARTING].... (state = server is starting)")
start(server)
