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


def send_message(client : socket.socket, msg : str):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_lenght = str(msg_len).encode(FORMAT)
    send_lenght += b' ' * (HEADER - len(send_lenght))
    client.send(send_lenght)
    client.send(message)


send_message(client, "HOLA AMIGO!")
input()
send_message(client, "Hamza Mughal here")
input()
send_message(client, "bing chilling")
input()
send_message(client, "nigga")
input()
send_message(client, DISCONNECT_MESSAGE)
