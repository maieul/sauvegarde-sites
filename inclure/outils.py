#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import config
from keyring import get_password,set_password

def pwd(serveur,login):
	"""Retourne le mdp associé au serveur / login, ou a défaut le demande"""
	chaine =  login +"@" + serveur
	pwd  = get_password("sauvegarde " + chaine,login)
	if pwd==None or pwd==u'' or config.resetmdp==True :
		pwd = raw_input("Mot de passe " + chaine + " ? ")
		set_password("sauvegarde " + chaine,login,pwd)
	return pwd
	
def afficher_resultats(resultats):
	'''Affiche le résultat pour l'ensemble des sites'''

	print "\n****\n"
	for site in resultats:
		print ("Résultats sur " + site + " :")
		try:
			for recup in resultats[site]:
				if (resultats[site][recup]!=0):# une erreur
					print ("\t " + recup + " : " + str(resultats[site][recup]))
				else:
					print ("\t " + recup + " OK")
		except:
			if (resultats[site]!=0):
				print ("\t " + str(resultats[site]))
			else:
				print ("\t OK")
		

def creer_dossier(chemin):
	''' Crée un dossier, si non existant, à partir d'un chemin'''
	try:
		os.makedirs(chemin)
		print ("Création de : " + chemin)
	except  OSError:
		pass
	except:
		print ("Erreur inconnue lors de la création de " + chemin + " " + sys.exc_info()[0])	



