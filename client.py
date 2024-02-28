import socket
import json

# initializing client site
SERVER = '192.168.0.108'  
PORT = 8080        
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "DISCONNECT_TRUE"   

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# function for receiving data (JSON)
def re_msg(client : socket.socket):
    # lenght of message we gonna receive (for handling size dynamically)
    msg_lenght = client.recv(HEADER).decode(FORMAT)

    # if message is None
    if msg_lenght:
        pass
    else:
        return None
    
    # receiving message using msg_lenght and converting back to JSON
    msg_lenght = int(msg_lenght)
    msg = client.recv(msg_lenght).decode(FORMAT)
    msg = json.loads(msg)

    # printing 'msg' from JSON we received
    print(f"[MESSAGE] (content = {msg['msg']})")


# function for sending data (JSON)
def send_message(client : socket.socket, msg : dict):
    # Conveting JSON into string and then into bit code
    message = json.dumps(msg).encode(FORMAT)

    # sending lenght of the data we are going to send
    msg_len = len(message)
    send_lenght = str(msg_len).encode(FORMAT)
    send_lenght += b' ' * (HEADER - len(send_lenght))
    client.send(send_lenght)

    # sending actual data (JSON)
    client.send(message)
    

if __name__ == "__main__":
    msgs = [
        "hola amigo",
            "Hamza Mughal here",
            "bing chilling",
            "nigga",
            DISCONNECT_MESSAGE
            ]
    
    for i in msgs:
        send_message(client, {"msg" : i})
        re_msg(client)
        input()
