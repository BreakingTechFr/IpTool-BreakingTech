import socket
import os
import sys
import subprocess
from multiprocessing.dummy import Pool as ThreadPool


red = '\033[91m'
green = '\033[92m'
white = '\033[00m'

try:
    while True:
        print("\033[35m--------------------------------------------------------------------")
        print("\n1) Vérifier l'IP pour un nom de domaine")
        print("2) Vérifier que les adresses IP sont en lignes à partir d'une liste d'adresses IP dans un fichier .txt")
        print("3) Revenir au menu principal")
        print("--------------------------------------------------------------------\033[0m")
        choice = input("\nEntrez votre choix : ")

        if choice == '1':
            domain = input("Entrer le nom de domaine: ")
            try:
                ips = list(set(socket.gethostbyname_ex(domain)[2]))
            except:
                print("Impossible de résoudre le nom de domaine")
                continue
        elif choice == '2':
            file_path = input("Importer une liste de domaines à partir d'un fichier .txt: ")
            if not os.path.isfile(file_path):
                print(f"{file_path} n'existe pas")
                continue
            with open(file_path, 'r') as f:
                ips = f.read().splitlines()
        elif choice == '3':
            sys.exit()
        else:
            print(f"{RED}Choix invalide. Veuillez entrer un numéro valide.{RESET}\n")
            continue

        def taz(ip):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                result = sock.connect_ex((ip, 80))
                if result != 0:
                    print(red + '[-] Ip hors ligne --> ' + ip + white)
                else:
                    print(green + '[+] Ip en ligne --> ' + ip + white)
                    with open("Result/LiveIps.txt", "a") as f:
                        f.write(ip + "\n")
            except:
                pass

        if 'ips' not in locals():
            continue

        pool = ThreadPool(100)
        pool.map(taz, ips)
        pool.close()
        pool.join()
        print("Opération Terminée. Les résultats sont sauvegardés dans Result/LiveIps.txt")

except KeyboardInterrupt:
    print("\nInterruption faite par l'utilisateur.")