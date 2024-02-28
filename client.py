import socket
import json

SERVER = '192.168.0.108'  
PORT = 8080        
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "DISCONNECT_TRUE"   

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def re_msg(client : socket.socket):
    msg_lenght = client.recv(HEADER).decode(FORMAT)

    if msg_lenght:
        pass
    else:
        return None
    
    msg_lenght = int(msg_lenght)
    msg = client.recv(msg_lenght).decode(FORMAT)
    msg = json.loads(msg)

    print(f"[MESSAGE] (content = {msg['msg']})")

def send_message(client : socket.socket, msg : dict):
    message = json.dumps(msg).encode(FORMAT)
    msg_len = len(message)
    send_lenght = str(msg_len).encode(FORMAT)
    send_lenght += b' ' * (HEADER - len(send_lenght))
    client.send(send_lenght)
    client.send(message)
    re_msg(client)


send_message(client, {"msg" : "hola amigo"})
input()
# send_message(client, "Hamza Mughal here")
# input()
# send_message(client, "bing chilling")
# input()
# send_message(client, "nigga")
# input()
send_message(client, {"msg" : DISCONNECT_MESSAGE})
