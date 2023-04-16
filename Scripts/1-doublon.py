import os
import colorama
import shutil
import subprocess
import sys

colorama.init()

CLEAR_SCREEN = "\033[2J"
RED = "\033[31m"
RESET = "\033[0m"
BLUE = "\033[34m"
CYAN = "\033[36m"
GREEN = "\033[32m"
BOLD = "\033[m"
REVERSE = "\033[m"
BLACK = "\033[30m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

try:
    while True:
        print("\nQuel est votre choix ?")
        print("\n1) Supprimer les doublons de lignes d'un fichier texte")
        print("2) Retourner au menu principal")
        option = input("\nEntrez le numéro de l'option : ")
        option = option.strip()

        if option == '1':
            # Demander à l'utilisateur de spécifier le chemin d'un fichier ou de le glisser-déposer dans le terminal
            print(YELLOW + "\nAttention : Les lignes en doublon seront effacées dans le fichier que vous allez insérer ici" + RESET)
            filepath = input("\nEntrez le chemin d'un fichier .txt ou faites-le glisser-déposer ici : ")
            filepath = filepath.strip()

            # Vérifier si le chemin de fichier est valide
            if os.path.isfile(filepath) and filepath.endswith('.txt'):
                # Ouvrir le fichier d'entrée en mode lecture
                with open(filepath, "r") as input_file:
                    # Lire toutes les lignes dans une liste et créer un ensemble (set) de lignes uniques
                    unique_lines = set(input_file.readlines())
                # Ouvrir le fichier d'entrée en mode écriture pour effacer les doublons
                with open(filepath, "w") as output_file:
                    # Écrire les lignes uniques dans le fichier en écrasant les doublons
                    output_file.writelines(unique_lines)
                print(GREEN + "Les doublons de lignes ont été supprimés avec succès dans le fichier {}.".format(filepath) + RESET)
                break
            else:
                print("Le fichier n'existe pas ou n'est pas un fichier texte.")
        
        elif option == '2':
            break
        
        else:
            print(f"{RED}Choix invalide. Veuillez entrer un numéro valide.{RESET}\n")
            print("--------------------------------------------------------")

except KeyboardInterrupt:
    print("\nInterruption faite par l'utilisateur.")
