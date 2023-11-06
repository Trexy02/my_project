import os
from .tools import tool

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
        if tool.is_identifiant(line) :
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


def parse(filename):
    """
    Lit un fichier et retourne les lignes sous forme de listes puis parcourt les lignes du fasta pour créer un dictionnaire {identifiant : séquence}
    Paramètres ------ nom du fichier
    ------ Retourne : un dictionnaire {identifiant : séquence}
    """
    lines = tool.read_file(filename)
    dict_seq = parse_fasta(lines)
    print(dict_seq)

def convert_RNA(dict_seq):
    """
    Convertir les séquences d'ADN en séquence d'ARN
    
    Le dictiionnaire de séquence à convertir.
    
    Un dictionnaire de séquence converties
    """
    ndict_seq = {}
    for key, seq in dict_seq.items():
        seq_rna = seq.replace('T', 'U')
        ndict_seq[key] = seq_rna
    return(ndict_seq)
    
import sys
import argparse
def run():
    #filename=sys.argv[1]
    #parse(filename)
    parser = argparse.ArgumentParser(
        prog="genomic",
        usage="genomic filename --RNA",
        description="Il peut lire un fichier fasta"
    )
    parser.add_argument(
        "filename",
        type=str,
        help="Required argument: Your folder",
    )
    parser.add_argument(
        "--RNA",
        action='store_true',
        help="Optional argument: If present, converts the sequence into RNA",
    )

    args = parser.parse_args()
    filename = args.filename
    
    lines=tool.read_file(filename)
    dict_seq = parse_fasta(lines)
    if args.RNA :
        dict_seq = convert_RNA(dict_seq)
    print(dict_seq)
    

if __name__=="__main__":
    run()