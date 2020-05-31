#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import config
import inclure.outils as outils

def ssh(site):
	''' récupere le contenu d'un site via SSH (rsync)'''
	resultats = {}
	# vérifier que le base est écrite correctement

	options = '--progress --delete-after -vrza -R -e ssh '

	destination_commune = os.path.join(config.dossier,site["dossier"])
	# indiquer les exclusions
	for ex in site['exclure']:
		options = options + "--exclude=\"" +ex + "\" "

	# créer la requete complete de base

	requete_base = "rsync " + options + site["login"] + "@" + site["serveur"] + ":'"
	requete = requete_base
	# recuperer plusieurs dossier à la fois
	for recup in site['recuperation']:
		# pour avoir bien l'arbo complète en local
		if recup[-1] != '/':
			recup += '/'

		requete +=  os.path.join(site['base'],recup) + " "

	requete += "' " + destination_commune

	print ("Récup de " + site["dossier"])
	resultats = os.system(requete)

	return resultats

def ftp(site):
	'''récupere le contenu d'un site via ftp ou ftps (lftp)'''

	resultats={}
	# récupération du mot de passe, interrogation le cas échéant
	from keyring import get_password,set_password
	pwd = outils.pwd(site['serveur'],site['login'])

	# paramètre globaux
	ouverture = "open " + site["serveur"] + " -u " + site["login"] + "," + pwd
	destination = os.path.join(config.dossier,site["dossier"])

	## exclusion
	exclusion = ""
	for ex in site["exclure"]:
		exclusion += "--exclude "+ ex + " "
	for recup in site["recuperation"]:
		cd = "cd " +  os.path.join(site['base'],recup)
		req = "lftp -c \"set ftp:list-options -a; set net:max-retries 2;"
		req += ouverture + ";"
		if 'lftpopen' in site:
 			req = req + site['lftpopen']
		req += cd + ";"
		req += "lcd " + destination + ";"
		req += "mirror --delete --verbose " + exclusion
		req += "-O " + recup + ";"
		req += "\""
		print ("Récup de " + site["dossier"] + " : " + recup)
		resultats[recup] = os.system(req)

	return resultats
