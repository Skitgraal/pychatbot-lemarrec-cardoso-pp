import os


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
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
            noms_presidents.add(nom_president)

    return list(noms_presidents)


