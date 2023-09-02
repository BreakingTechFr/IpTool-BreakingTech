import fastcli
import sys
import time

def lancer_test_connexion():
    print("Le test de connexion va être lancé...")
    server = fastcli.get_best_server()
    print("Serveur le plus proche : {}".format(server['sponsor']))
    download_speed, upload_speed, ping = fastcli.test_speed(
        server['url'], callback=print_progression)
    print("Vitesse de téléchargement : {:.2f} Mbps".format(download_speed))
    print("Vitesse de déversement : {:.2f} Mbps".format(upload_speed))
    print("Ping : {} ms".format(ping))

def print_progression(current, total):
    progress = (current / total) * 100
    sys.stdout.write('\r[{0}] {1}%'.format('#' * int(progress/10), progress))
    sys.stdout.flush()

def menu():
    print("\nMenu :")
    print("\n\033[35m--------------------------------------------------------------------")
    print("1. Lancer le test de connexion")
    print("2. Retourner au script main.py")
    print("--------------------------------------------------------------------\033[0m")
    choix = input("\nEntrez votre choix : ")
    return choix

if __name__ == "__main__":
    while True:
        choix = menu()
        if choix == "1":
            try:
                lancer_test_connexion()
            except KeyboardInterrupt:
                print("\nLe test a été interrompu.")
        elif choix == "2":
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
