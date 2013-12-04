dossier = "/Users/maieul/Sites/sauvegarde"

sites=[
{
	'mode':'SSH',
	'login':'votre login',
	'serveur':'serveur ssh',
	
	'base':'emplacement sur le serveur ssh',
	'recuperation':('IMG','tmp/dump'),
	'exclure':('article_PDF','distant','.svn','.ok'),
	
	'dossier':'nom du dossier local'
},

{
	'mode':'FTP',
	'login':'votre login',
	'serveur':'serveur ftp',
	
	'base':'emplacement sur le serveur ftp',
	'recuperation':('IMG','tmp/dump'),
	'exclure':('article_PDF','distant','.svn','.ok'),
	
	'dossier':'nom du dossier local'
}
       
       
]
