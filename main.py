import logging

# Le module logging: est un puissant module de journalisation
# inégré de python. Nous pouvons ainsi ajouter rapidement
# la journalisation à notre application en l'important
# On examinera les differents :
# --> niveaux de bloc,
# --> options de configuration,
# --> comment verrouiller les diff modules
# --> comment utiliser diff gestionnaires de verrouillage
# --> comment capturer les traces de pile dans notre journal
# --> comment utiliser le gestionnaire de fichiers rotatif


# configuration de base
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)-15s %(levelname)-8s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
import help
"""
Et si je crée ce journal ici, cela créera une hierachie d'enregistreurs. cela commence au niveau de l'enregistreur racine et nous tous ces nouveaux renregistreurs sont ajoutés à cette hierarchie.
Et ils prolongent ses messages jusqu'au logger de base.
Alors, je ne veux pas avoir cette propagation, je peux dire que la propagation des points de l'enregistreur est égale à faux(logger.propagate=False dans help.py). Donc par defaut, c'est vrai. Et maintenant, cela ne se propagera pas au logger de base.
Donc, en ce moment quand j'exécute, rien ne sera vérrouillé car il ne se propage pas à notre enregistreur de base.
"""


# Il est préférable de ne pas utilser cet enregistreur avec le root mais de créer notre propre enregistreur interne dans un module.
# apres configuration de base, je peux supprimer ces logging
# logging.debug('This is a debug message')
# logging.info('This is a info message')
# logging.warning('This is a wornind message')
# logging.error('This is a error message')
# logging.critical('This is a critical message')

