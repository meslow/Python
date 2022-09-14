#!/usr/bin/python

# Imports des modules necessaire
import os
import shutil
import time

# initialisation des compteurs
deleted_files_count = 0

# Dossier cible
path = "/var/www/html/files/"

# Extension a traiter
extension = ".php"

#Supression fichier plus vieux que 
days = 20


# Fonction supression de fichier (gestion d'erreur)
def remove_file(path):

	# removing the file
	if not os.remove(path):

		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print(f"Unable to delete the {path}")

# Fonction recupération temps ecoulé du fichier
def get_file_or_folder_age(path):

	# getting ctime of the file/folder
	# time will be in seconds
	#
	# utiliser st_mtime sur windows
	# Normalement ctime, mais ne fonctionne que sur unix
	#
	ctime = os.stat(path).st_mtime

	# returning the time
	return ctime


# converting days to seconds
# time.time() returns current time in seconds
seconds = time.time() - (days * 24 * 60 * 60)

# Iterate directory
for file in os.listdir(path):
	# check only text files
	if file.endswith(extension):
		full_path = path+file
		#print(full_path)
		file_time = get_file_or_folder_age(full_path)
		if seconds >= file_time :
			#Lancement de la supression du fichier sur plus ancien que definit
			remove_file(full_path)
			#incrément du compteur de fichiers supprimés
			deleted_files_count += 1 # incrementing count

# Affiche le nb de fichier supprimés
print(deleted_files_count)
