import os

speeches_dir =  './speeches'
cleaned_dir = './cleaned'

def list_of_files(speeches_dir, extension):
    files_names = []
    for filename in os.listdir(speeches_dir):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def extraire_noms_presidents(nom_du_dossier):
    # Ensemble pour stocker les noms des présidents uniques
    noms_presidents = set()

    # Parcourir les fichiers du dossier
    for nom_fichier in os.listdir(nom_du_dossier):
        chemin_fichier = os.path.join(nom_du_dossier, nom_fichier)

        # Vérifier si le fichier correspond au format spécifié
        if os.path.isfile(chemin_fichier) and nom_fichier.startswith("Nomination_") and nom_fichier.endswith(".txt"):
            # Extraire le nom du président en utilisant split
            nom_president = nom_fichier.split("_")[1].split(".")[0]
            res = ''
            for c in nom_president:
                if ord('0') > ord(c) or ord(c) > ord('9'):
                    res += c
            noms_presidents.add(res)
    return list(noms_presidents)


def associationnom(noms_presidents):
    for i in range(len(noms_presidents)):
        if noms_presidents[i] == 'Macron':
            noms_presidents[i] = 'Emmanuelle Macron'
        elif noms_presidents[i] == 'Sarkozy':
            noms_presidents[i] = 'Nicolas Sarkozy'
        elif noms_presidents[i] == 'Chirac':
            noms_presidents[i] = 'Jacques Chirac'
        elif noms_presidents[i] == 'Hollande':
            noms_presidents[i] = 'François Hollande'
        elif noms_presidents[i] == 'Mitterrand':
            noms_presidents[i] = 'François Mitterrand'
        elif noms_presidents[i] == 'Giscard dEstaing':
            noms_presidents[i] = 'Valéry Giscard dEstaing'
    return (noms_presidents)


def cleaned (speeches_dir,cleaned_dir, files):
    for filename in files:
        lowered_file = cleaned_dir + '/' + filename.split(".")[0] + "-cleaned.txt"
        with open(speeches_dir + '/' + filename, "r") as f1, open(lowered_file, "w") as f2:
            punct = "-_.#?\|':!(),;:=+`"
            res = ""
            for lettre in f1.read():
                if ord(lettre)>64 and  ord(lettre) < 91:
                    lettre = chr(ord(lettre) + 32)
                if (lettre in punct) or (lettre == '"'):
                    lettre = " "
                res += lettre
            f2.write(res)
