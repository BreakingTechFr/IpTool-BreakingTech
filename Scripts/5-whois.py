import whois
import socket
import colorama
import requests
import sys
import re

colorama.init()

CLEAR_SCREEN = "\033[2J"
RED = "\033[31m"
RESET = "\033[0m"
BLUE = "\033[34m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
WHITE = "\033[37m"

# Fonction pour obtenir les informations Whois
def get_whois_info(domain_name):
    try:
        # Utilisation d'une expression régulière pour extraire le nom de domaine
        url_pattern = re.compile(r"^(https?://)?(www\.)?(?P<domain>[a-zA-Z0-9.-]+)")
        match = url_pattern.match(domain_name)
        
        if match:
            domain_name = match.group("domain")
        
        # Résoudre le nom de domaine en une adresse IP
        ip = socket.gethostbyname(domain_name)

        # Résoudre le nom de domaine en une adresse IPv6
        ip6 = socket.getaddrinfo(domain_name, None, socket.AF_INET6)
        ipv6 = ip6[0][4][0] if ip6 else "N/A"

        # Afficher l'adresse IP et IPv6
        print(f"\nAdresse IPv4 de {domain_name} : \033[32m{ip}\033[0m")
        print(f"Adresse IPv6 de {domain_name} : \033[32m{ipv6}\033[0m")

        w = whois.whois(domain_name)
        print("\n----------------------------------------------------------------------------")
        print(GREEN + "\nInformations sur le nom de domaine" + RESET)
        print(f"\nServeur Whois : {w.whois_server}")
        print(f"Statut du domaine : {w.status}")
        print(f"Date d'enregistrement : {w.creation_date}")
        print(f"Date d'expiration : {w.expiration_date}")
        print(f"Nom du Fournisseur : {w.registrar}")
        # Titulaire
        if w.name is None:
            print(BLUE + "\nInformations sur le propriétaire :" + RESET)
            print("Le propriétaire a dissimulé ses informations personnelles.")
        else:
            print(BLUE + "\nInformations sur le propriétaire :" + RESET)
            print(f"\nNom du titulaire : {w.name}")
            print(f"Adresse email du titulaire : {w.email}")
            print(f"Pays du titulaire : {w.country}")
        # Informations supplémentaires
        print(CYAN + "\nInformations sur le fournisseur d'accès internet :" + RESET)
        print(f"\nNom du fournisseur FAI : {w.org}")
        print(f"Organisation : {w.name}")
        print(f"Fuseau horaire : {w.timezone}")
        print(f"Ville : {w.city}")
        print(f"Région : {w.regionName}")
        print(f"Pays : {w.country}")
        print(f"Latitude : {w.lat}")
        print(f"Longitude : {w.lon}")
        print("\n------------------------------------------------------------------------------")
        print(f"{YELLOW}Remarque : Les informations sur l'adresse IP peuvent être approximatives.{RESET}")
        print("------------------------------------------------------------------------------")
    except whois.parser.PywhoisError as e:
        print(f"{RED}Erreur : impossible de récupérer les informations Whois.{RESET}")
        print(f"Message d'erreur : {e}")

def get_geo_info(ip):
    try:
        url = f"http://ipapi.co/{ip}/json/"
        response = requests.get(url)
        data = response.json()
        print(MAGENTA + "\nInformations de géolocalisation :" + RESET)
        print(f"Pays : {data['country_name']}")
        print(f"Ville : {data['city']}")
        print(f"Code postal : {data['postal']}")
        print(f"Latitude : {data['latitude']}")
        print(f"Longitude : {data['longitude']}")
        print(f"Fuseau horaire : {data['timezone']}")
        print("\n------------------------------------------------------------------------------")
        print(f"{YELLOW}Remarque : Les informations sur l'adresse IP peuvent être approximatives.{RESET}")
        print("------------------------------------------------------------------------------")
    except Exception as e:
        print(f"{RED}Erreur : impossible de récupérer les informations de géolocalisation.{RESET}")
        print(f"Message d'erreur : {e}")

# Fonction pour obtenir les informations sur une adresse IP
def get_ip_info(ip):
    try:
        # Nom d'hôte correspondant à l'adresse IP
        host_name = socket.gethostbyaddr(ip)[0]
        print(f"Nom de domaine correspondant à l'adresse IP : {host_name}")
        # Informations Whois pour le nom d'hôte
        get_whois_info(host_name)
    except Exception as e:
        print(f"{RED}Erreur : impossible de récupérer les informations sur l'adresse IP.{RESET}")
        print(f"Message d'erreur : {e}")

# La boucle de menu
while True:
    try:
        print("\nQue souhaitez-vous faire ?")
        print("\n\033[35m--------------------------------------------------------------------")
        print("1 - Entrer un nom de domaine")
        print("2 - Entrer une adresse IP")
        print("3 - Retourner au menu principal")
        print("--------------------------------------------------------------------\033[0m")
        choice = input("\nEntrez votre choix : ")

        if choice == "1":
            user_input = input("\nEntrez un nom de domaine : ")
            get_whois_info(user_input)
        elif choice == "2":
            ip = input("Entrez une adresse IP : ")
            get_ip_info(ip)
        elif choice == "3":
            sys.exit()
        else:
            print("Choix invalide. Veuillez entrer un numéro valide.")
    except KeyboardInterrupt:
        print("\nInterruption faite par l'utilisateur.")
        sys.exit()