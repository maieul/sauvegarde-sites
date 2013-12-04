#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import config
def ssh(site):
	''' récupere le contenu d'un site via SSH (rsync)'''
	
	# vérifier que le base est écrite correctement

	options = '--progress  --delete-after -vrza -e ssh '
	
	destination = os.path.join(config.dossier,site["dossier"])
	# indiquer les exclusions
	for ex in site['exclure']:
		options = options + "--exclude=\"" +ex + "\" "
	
	# créer la requete complete de base
	
	requete_base = "rsync " + options + site["login"] + "@" + site["serveur"] + ":" 
	
	# l'executer sur chaque dossier
	erreurs = {}
	for recup in site['recuperation']:
		if recup[-1] == '/':
			recup = recup[:-1]
		requete = requete_base + os.path.join(site['base'],recup) + " " + destination
		print ("Récup de " + site["dossier"] + " : " + recup)
		resultat = os.system(requete)
		if resultat!=0:
			erreurs[recup] = resultat
	
	# retourner les erreurs éventuelles
	return erreurs
