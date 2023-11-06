import os

def read_file(filename):
    """
    Lire un fichier et retourner les lignes sous forme de listes.
    Paramètres ------ nom du fichier
    ------ Retourne : les lignes sous forme de listes
    """
    if os.path.exists(filename) :
        print(f"{filename} a ete trouve")
        # Lecture du fichier
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
    else :
        print(f"{filename} n'a pas ete trouve, veuillez changer le chemin du fichier.")
        lines = []
    return lines    
def is_identifiant(line) :
    """
    Test si une ligne de fasta est un identifant ou une séquence.
    Paramètres ------ ligne dans le fichier fasta
    Retourne : True or False selon si la ligne est un identifiant ou une séquence.
    """
    if ">" in line :
        return True
    else:
        return False
    
def parse_fasta(lines) :
    """
    Parcourir les lignes du fasta pour créer un dictionnaire {identifiant : séquence} 
    Paramètres ------ listes dans le fichier fasta
    ------ Retourne : les listes sous forme de dictionnaires
    """
    i = 0
    dict_seq = {}
    identifiant = ""
    # Parcours des lignes
    while i < len(lines) :
        line = lines[i].strip()
        # Recupere l'identfiant de séquence
        if is_identifiant(line) :
            identifiant = line
        else :
            # Si la sequence est sur plusieurs lignes, ajoute la nouvelle ligne de sequence à la sequence existante
            if identifiant in dict_seq :
                dict_seq[identifiant] = dict_seq[identifiant] + line
            # Crée une nouvelle entrée dans le dictionnaire
            else :
                identifiant = identifiant.replace('>','')
                dict_seq[identifiant] = line
        i = i+1
    return dict_seq

