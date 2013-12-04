#!/usr/bin/python
# -*- coding: utf-8 -*-

# Version 1.0.0
# Maïeul Rouquette - 2013
# Licence : GNU/GPL 3 (https://www.gnu.org/licenses/gpl.html)

import os
import config

def creer_dossier(chemin):
	''' Crée un dossier, si non existant, à partir d'un chemin'''
	try:
		os.makedirs(chemin)
		print ("Création de : " + chemin)
	except  OSError:
		pass
	except:
		print ("Erreur inconnue lors de la création de " + chemin + " " + sys.exc_info()[0])	
	
def main():
	'''Fonction principale, qui se contente de 
		1. Créer le dossier ad hoc si besoin.
		2. Tourner sur l'ensemble des sites, pour 
			a. Créer si besoin le dossier
			b. Appeler ensuite la fonction ad hoc
	'''
	
	#1 
	creer_dossier(config.dossier)
	
	
	#2a
	for site in config.sites:
		creer_dossier (os.path.join(config.dossier,site["dossier"]))

main()