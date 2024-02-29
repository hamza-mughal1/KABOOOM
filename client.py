import socket
import json
import pygame


pygame.init()

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

    return msg


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
    root = pygame.display.set_mode((700,500))
    loop_check = True
    x = 350
    y = 250

    while loop_check:
        root.fill((50,50,50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop_check = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    x = 350
                    y = 250

        if x >= 600 or y >= 450:
            pass
        else:
            send_message(client, {"msg" : 1, "coor" : [x,y]})
            x, y = re_msg(client)["coor"]

        pygame.draw.rect(root,(100,100,100),pygame.Rect(x,y,50,50))
        
        
        pygame.display.update()

    pygame.quit()

    # msgs = [
    #     "hola amigo",
    #         "Hamza Mughal here",
    #         "bing chilling",
    #         "nigga",
    #         DISCONNECT_MESSAGE
    #         ]
    
    # for i in msgs:
    #     send_message(client, {"msg" : i})
    #     re_msg(client)
    #     input()
