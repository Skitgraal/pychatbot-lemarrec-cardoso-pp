from fonction import *

#Appel de la fonction
directory = "./speeches/"
cleaned_dir = "./cleaned"
files_names = list_of_files(directory, "txt")

nom_fichier = directory + files_names[0]

nom_du_dossier = directory
waitingroom = extraire_noms_presidents(nom_du_dossier)
print(associationnom(waitingroom))


cleaned(speeches_dir, cleaned_dir, files_names)
files_names = list_of_files(cleaned_dir, "txt")
for i in range (0,8):
    print(tf(files_names[i], cleaned_dir))

