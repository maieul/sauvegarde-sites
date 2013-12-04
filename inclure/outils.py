#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import config
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



