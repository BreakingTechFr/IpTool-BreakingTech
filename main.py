import os
import sys
import subprocess
from platform import system
import colorama

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

os.system('cls' if os.name == 'nt' else 'clear')

logo = '''
 _____        _____           _               ______                _    _           _____         _     
|_   _|      |_   _|         | |              | ___ \              | |  (_)         |_   _|       | |    
  | | _ __     | | ___   ___ | |___   ______  | |_/ /_ __ ___  __ _| | ___ _ __   __ _| | ___  ___| |__  
  | || '_ \    | |/ _ \ / _ \| / __| |______| | ___ \ '__/ _ \/ _` | |/ / | '_ \ / _` | |/ _ \/ __| '_ \ 
 _| || |_) |   | | (_) | (_) | \__ \          | |_/ / | |  __/ (_| |   <| | | | | (_| | |  __/ (__| | | |
 \___/ .__/    \_/\___/ \___/|_|___/          \____/|_|  \___|\__,_|_|\_\_|_| |_|\__, \_/\___|\___|_| |_|
     | |                                                                          __/ | V1.0                 
     |_|                                                                         |___/                   
'''
intro = '''

La boite à outils IP par Breakingtech.fr
'''

choixmenu = '''                                   
--------------------------------------------------------------------
1) Supprimer les doublons de lignes dans un fichier .txt 
2) Obtenir les adresses IP appartenant à un ou plusieurs domaines
3) Vérifier un ou plusieurs domaines en ligne
4) Scan des ports d'une Ip
5) Whois une IP ou un nom de domaine
6) Afficher votre IP aux formats IPV4 et IPV6
9) Quitter le programme
--------------------------------------------------------------------

'''
while True:
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(RED + logo + YELLOW + intro + GREEN + choixmenu + RESET)
        choice = input('Menu Principal | Entrer un choix : ')
        if choice.isdigit():
            if choice == '1':
                subprocess.call(["python3", "Scripts/1-doublon.py"])
            elif choice == '2':
                subprocess.call(["python3", "Scripts/2-ipdudomaine.py"])
            elif choice == '3':
                subprocess.call(["python3", "Scripts/3-verifliveip.py"])
            elif choice == '4':
                subprocess.call(["python3", "Scripts/4-scanportsip.py"])
            elif choice == '5':
                subprocess.call(["python3", "Scripts/5-whois.py"])
            elif choice == '6':
                subprocess.call(["python3", "Scripts/6-monip.py"])
            elif choice == '7':
                print(f"{MAGENTA}\nMerci d'avoir utilisé notre programme, à bientôt !{RESET}")
                sys.exit()
            else:
                print(f"{RED}Choix invalide. Veuillez entrer un numéro valide.{RESET}\n")
        else:
            print(f"{RED}Choix invalide. Veuillez entrer un numéro valide.{RESET}\n")
        if choice not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            input('\nAppuyez sur Entrée pour faire un nouveau choix.')
            choice = ''

    except KeyboardInterrupt:
        print(f"{MAGENTA}\nMerci d'avoir utilisé notre programme, à bientôt !{RESET}")
        sys.exit()
