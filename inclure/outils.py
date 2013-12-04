#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import config
from keyring import get_password,set_password

def pwd(serveur,login):
	"""Retourne le mdp associé au serveur / login, ou a défaut le demande"""
	pwd  = get_password("sauvegarde " + serveur,login)
	if pwd==None :
		pwd = raw_input("Mot de passe "+login + "@" + serveur + " ? ")
		set_password(serveur,login,pwd)
	return pwd
	
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



