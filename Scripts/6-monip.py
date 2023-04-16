import requests
import subprocess
import sys
import colorama

colorama.init()

CLEAR_SCREEN = "\033[2J"
RED = "\033[31m"
RESET = "\033[0m"
BLUE = "\033[34m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"


while True:
    try:
        print("1) Afficher mon IPV4 et IPV6")
        print("2) Retourner au menu principal\n")

        choix = input("Entrez votre choix : ")

        if choix == "1":
            # Obtenir l'adresse IPv4 publique
            ipv4_response = requests.get("https://api.ipify.org?format=json")
            ipv4_address = ipv4_response.json()["ip"]

            # Obtenir l'adresse IPv6 publique
            ipv6_response = requests.get("https://api6.ipify.org?format=json")
            ipv6_address = ipv6_response.json()["ip"]

            # Obtenir des informations sur l'adresse IP
            ipinfo_response = requests.get(f"https://ipinfo.io/{ipv4_address}/json")
            ipinfo_data = ipinfo_response.json()
            ipinfo_city = ipinfo_data["city"]
            ipinfo_region = ipinfo_data["region"]
            ipinfo_country = ipinfo_data["country"]
            ipinfo_org = ipinfo_data["org"]
            ipinfo_timezone = ipinfo_data["timezone"]
            ipinfo_location = ipinfo_data["loc"]
            ipinfo_postal_code = ipinfo_data["postal"]

            # Afficher les informations
            print(f"\nAdresse IPv4 publique : {GREEN}{ipv4_address}{RESET}")
            print(f"Adresse IPv6 publique : {YELLOW}{ipv6_address}{RESET}")
            print(BLUE + "\nInformations supplémentaires :" + RESET)
            print(f"Localisation : {ipinfo_city}, {ipinfo_region}, {ipinfo_country}")
            print(f"Organisation : {ipinfo_org}")
            print(f"Fuseau horaire : {ipinfo_timezone}")
            print(f"Latitude, Longitude : {ipinfo_location}")
            print(f"Code Postal : {ipinfo_postal_code}\n")

        elif choix == "2":
            sys.exit()

        else:
            print(f"{RED}Choix invalide. Veuillez entrer un numéro valide.{RESET}\n")

    except KeyboardInterrupt:
        print("\nInterruption par l'utilisateur.")
        sys.exit()
