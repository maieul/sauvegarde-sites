#!/usr/bin/python
# -*- coding: utf-8 -*-

# Version 1.2.0
# Maïeul Rouquette ; 2013-*
# Licence : GNU/GPL 3 (https://www.gnu.org/licenses/gpl.html)

import os
import config
import inclure.recuperer as recuperer
import sys
from inclure.outils import *



def main():
	'''Fonction principale, qui se contente de
		1. Créer le dossier ad hoc si besoin.
		2. Tourner sur l'ensemble des sites, pour
			a. Créer si besoin le dossier
			b. Appeler ensuite la fonction ad hoc
		3. Appeler l'affichage des erreurs
	'''

	#1
	creer_dossier(config.dossier)


	#2a
	todo = []
	if len(sys.argv) > 1:
		todo = sys.argv[1:]
	resultats = {}
	for site in config.sites:
		if todo == [] or site['dossier'] in todo:
			resultat={}
			creer_dossier (os.path.join(config.dossier,site["dossier"]))

			if site['mode'].upper() == 'SSH':
				resultat = recuperer.ssh(site)
			elif site['mode'].upper() == 'FTP':
				resultat = recuperer.ftp(site)

			resultats[site["dossier"]] = resultat

	afficher_resultats(resultats)

main()
