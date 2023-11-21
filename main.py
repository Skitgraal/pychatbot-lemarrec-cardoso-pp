from fonction import *

#Appel de la fonction
directory = "./speeches/"
files_names = list_of_files(directory, "txt")
print(files_names)

nom_fichier = directory + files_names[0]

with open(nom_fichier, "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line)


print("Noms des présidents :", noms_presidents)