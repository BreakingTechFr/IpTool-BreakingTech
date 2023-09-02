import sys
import os
import re
import socket
import binascii
import time
import json
import random
import threading
import queue
import pprint
import urllib.parse
import smtplib
import telnetlib
import os.path
import hashlib
import string
import urllib.request
import glob
import sqlite3
import argparse
import marshal
import base64
import colorama
import requests
import subprocess
import tkinter as tk
from colorama import Fore, Back, init
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import system
from queue import Queue
from time import strftime
from urllib.parse import urlparse
from urllib.request import urlopen
from tkinter import filedialog


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

def logo():
    clear = "\x1b[0m"
    colors = [36]

    x = """\nAttention : La liste des noms de domaines doit être sans http:// ou https// \n"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)

logo()

def get_IP(site):
    try:
        if "http://" not in site and "https://" not in site:
            IP1 = socket.gethostbyname(site)
            domain = socket.gethostbyaddr(IP1)[0]
            print("Domaine: " + BLUE + site + RESET + " | IP: " + GREEN + IP1 + RESET)
            open("ips.txt", "a").write(site + " " + IP1 + "\n")
        else:
            print(RED + "Erreur : Le domaine ne doit pas commencer par 'http://' ou 'https://'" + RESET)
    except:
        pass

def showIPsOnly():
    try:
        with open("ips.txt") as f:
            for line in f:
                line = line.strip()
                if line:
                    ip = line.split()[1]
                    print("IP: " + GREEN + ip + RESET)
    except:
        pass

def get_txt_file_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Fichier texte", "*.txt")])
    return file_path

try:
    while True:
        print("\033[35m--------------------------------------------------------------------")
        print("1) Entrez le nom de domaine")
        print("2) Entrez le chemin du fichier .txt contenant plusieurs noms de domaines ou glissez déposez le fichier")
        print("3) Lire le fichier contenant les domaines et IP obtenus")
        print("4) Lire le fichier contenant uniquement les IP obtenus")
        print("5) Retour au menu principal")
        print("--------------------------------------------------------------------\033[0m")
        choice = input("\nEntrez un choix: ")

        if choice == "1":
            nam = input("\nEntrez le nom de domaine: ")
            get_IP(nam)
        elif choice == "2":
            while True:
                nam = input("Entrez le chemin d'un fichier .txt ou faites-le glisser-déposer ici : ")
                nam = nam.strip()
                if os.path.isfile(nam):
                    with open(nam) as f:
                        for i in f:
                            get_IP(i.strip())
                    break
                elif os.path.isfile(nam.strip('"')):
                    with open(nam.strip('"')) as f:
                        for i in f:
                            get_IP(i.strip())
                    break
                else:
                    print(RED + "Erreur : Le chemin du fichier est incorrect." + RESET + " Veuillez entrer un nouveau chemin.")
        elif choice == "3":
            nam = "ips.txt"
            if not os.path.isfile(nam):
                print(RED + "Erreur : Le fichier est introuvable." + RESET)
            else:
                with open(nam) as f:
                    for line in f:
                        line = line.strip()
                        if line:
                            domain, ip = line.split()
                            print("\nDomaine: " + BLUE + domain + RESET + " | IP: " + GREEN + ip + RESET)
        elif choice == "4":
            showIPsOnly()
        elif choice == "5":
            sys.exit()
        else:
            print(RED + "Choix invalide. Veuillez entrer un numéro valide." + RESET)

except KeyboardInterrupt:
    print("\nInterruption faite par l'utilisateur.")
    sys.exit()
