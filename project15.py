import socket
import threading
import pickle


SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5555
ADDR = (SERVER_HOST, SERVER_PORT)
BUFFER_SIZE = 1024


players = {}


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen(2)  

print(f"Server started on {SERVER_HOST}:{SERVER_PORT}...")

def handle_client(client, addr, player_id):
    print(f"Player {player_id} connected from {addr}")
    player_data = {"x": 100, "y": 100, "direction": "RIGHT"}

   
    client.send(pickle.dumps(player_data))

    while True:
        try:
         
            msg = client.recv(BUFFER_SIZE)
            if not msg:
                break

      
            player_data = pickle.loads(msg)
            players[player_id] = player_data

          
            for client_id in players:
                if client_id != player_id:
                    client.send(pickle.dumps(players[client_id]))

        except:
            break


    client.close()
    print(f"Player {player_id} disconnected.")


def accept_players():
    player_id = 1
    while player_id <= 2:
        client, addr = server.accept()
        players[player_id] = {"x": 100, "y": 100, "direction": "RIGHT"}

        thread = threading.Thread(target=handle_client, args=(client, addr, player_id))
        thread.start()

        player_id += 1


accept_players()
