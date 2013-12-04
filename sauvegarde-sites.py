#!/usr/bin/python
# -*- coding: utf-8 -*-

# Version 1.0.0
# Maïeul Rouquette - 2013
# Licence : GNU/GPL 3 (https://www.gnu.org/licenses/gpl.html)

import os
import config

def recuperer_ssh(site):
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

def afficher_erreurs(erreurs):
	'''Affiche l'ensemble des sites ou dossier avec des erreurs'''

	print "\n****\n"
	for site in erreurs:
		print "Erreur sur " + site + " :"
		for recup in erreurs[site]:
			print "\t " + recup + " : " + str(erreurs[site][recup])


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
		3. Appeler l'affichage des erreurs
	'''
	
	#1 
	creer_dossier(config.dossier)
	
	
	#2a
	erreurs = {}
	for site in config.sites:
		creer_dossier (os.path.join(config.dossier,site["dossier"]))
		if site['mode'].upper() == 'SSH':
			resultat = recuperer_ssh(site)
		
		if resultat!={}:
			erreurs[site["dossier"]] = resultat
	
	afficher_erreurs(erreurs)

main()