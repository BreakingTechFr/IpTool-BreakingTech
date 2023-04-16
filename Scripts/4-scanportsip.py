import socket
import sys
import subprocess
import colorama
import nmap

colorama.init()

CLEAR_SCREEN = "\033[2J"
RED = "\033[31m"  
RESET = "\033[0m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
YELLOW = "\033[33m"

def get_service(port):
    nm = nmap.PortScanner()
    nm.scan(hosts=ip, ports=str(port), arguments='-sV')
    try:
        service = nm[ip]['tcp'][port]['name']
    except KeyError:
        service = "N/A"
    try:
        product = nm[ip]['tcp'][port]['product']
    except KeyError:
        product = "N/A"
    try:
        service_info = nm[ip]['tcp'][port]['extrainfo']
    except KeyError:
        service_info = "N/A"
    return service, product, service_info

while True:
    try:
        ip = input("Entrez une adresse IP : ")
        host_name = socket.gethostbyaddr(ip)[0]
        print(f"\nScan en cours pour l'adresse IP : {GREEN}{ip}{RESET} ({YELLOW}{host_name}{RESET})")

        start_port = int(input("Entrez le port de début : "))
        end_port = int(input("Entrez le port de fin : "))

        print("Scan en cours...")
        open_ports = []
        processes = []
        for port in range(start_port, end_port+1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                try:
                    process = subprocess.check_output(f"lsof -i:{port}", shell=True).decode("utf-8").split("\n")[1].split()[0]
                except subprocess.CalledProcessError:
                    process = "N/A"
                service, product, service_info = get_service(port)
                open_ports.append(port)
                print(f"Port {GREEN}{port}{RESET} ouvert {YELLOW}(TCP){RESET} : Service : {CYAN}{service}{RESET} Service Produit : {MAGENTA}{product}{RESET} Information sur le service : {YELLOW}{service_info}{RESET}")
            else:
                result_udp = sock.connect_ex((ip, port))
                if result_udp == 0:
                    try:
                        process = subprocess.check_output(f"lsof -i:{port}", shell=True).decode("utf-8").split("\n")[1].split()[0]
                    except subprocess.CalledProcessError:
                        process = "N/A"
                    service, product, service_info = get_service(port)
                    open_ports.append(port)
                    print(f"Port {GREEN}{port}{RESET} ouvert {YELLOW}(UDP){RESET} : {CYAN}{service}{RESET} / {MAGENTA}{product}{RESET} / {YELLOW}{service_info}{RESET}")
                sock.close()

        if len(open_ports) == 0:
            print("Aucun port ouvert trouvé.")
        else:
            print(f"\nFin du scan.\n\nTentative de récupération de l'OS utilisé...")

            # Obtention de l'OS utilisé pour l'IP scannée
            try:
                output = subprocess.check_output(f"nmap -O {ip}", shell=True).decode("utf-8")
                os_used = output.split("OS details: ")[1].split("\n")[0]
                print(f"\n{MAGENTA}OS utilisé : {os_used}{RESET}")
            except (subprocess.CalledProcessError, IndexError):
                print(f"\n{RED}Impossible de déterminer l'OS utilisé.{RESET}")

            # Affichage des choix de l'utilisateur
            response = input("\nQue voulez-vous faire ? \n1) Lancer le scan d'une autre adresse IP\n2) Retourner au menu principal\n\nQuel est votre choix ? ")
            if response == "1":
                continue
            elif response == "2":
                sys.exit()
            else:
                print(f"{RED}Choix invalide. Veuillez entrer un numéro valide.{RESET}\n")
                continue

    except KeyboardInterrupt:
        print("\nInterruption faite par l'utilisateur.")
        sys.exit()
    except socket.herror:
        print(f"{RED}Erreur : adresse IP non valide ou machine inactive.{RESET}")
        continue