import sys
from banner import banner

banner()
print()


def principale():
    while True:
        print()
        print("""
        Que souhaitez vous faire ?
        1) Reverse shell
        2) Keylogger
        3) Scan Network
        4) DDOS
        5) Mining Monero
        6) Exit
        """)
        print()
        intro = input("Votre choix : ")
        try:
            int_intro = int(intro)
            if int_intro == 6:
                break
            choix(int_intro)
            continue
        except:
            print("ERREUR: Votre choix doit etre un chiffre ")
            continue
        else:
            break


def choix(int_intro):
    if int_intro == 1:
        from Outils.backdoor_serveur import server
        server()
    elif int_intro == 2:
        from Outils.keylogger import keylogger
        keylogger()
    elif int_intro == 3:
        from Outils.scan_network import scan_network
        scan_network()
    elif int_intro == 4:
        from Outils.ddos import ddos
        ddos()
    elif int_intro == 5:
        from Outils.monero import monero
        monero()
    else:
        print("Merci de choisir entre 1 et 6 !!!")
        print()
        choix()

# Installation des dependences Windows/Linux


principale()
print()
print("Revenez quand vous voulez :)")

