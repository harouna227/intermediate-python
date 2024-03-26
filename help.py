import logging
import time
import logging.config
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler # creer un verrou rotatif basé sur le temps écoule
# Cela créera donc un enregistreur avec le nom du module.
# Et cela s'appelle donc assistance dans ce cas. Et nous pouvous 
# ensuite utiliser celui pour verrouiller quelque chose

# logger = logging.getLogger(__name__) # par exemple
# logger.propagate = False
# logger.info('hello from helper')

"""
Gestionnaire de verrous.
Les objets gestionnaires sont ddonc chargés de distribuer le message de verrouillage approprié à la destination spécifique du gestionnaire.
Par exemple on peut utiliser differents gestionnaires pour envoyer des messages de journal à ce flux de sortie standard vers des fichier via HTTP ou par e-mail.
"""
# logger = logging.getLogger(__name__)

# # create handler
# stream_h = logging.StreamHandler()
# file_h = logging.FileHandler('filr.log')

# # level and the format
# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)

# formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)

# logger.addHandler(stream_h)
# logger.addHandler(file_h)

# logger.warning('this is a worning')
# logger.error('this is an error')

"""
Maintenant, on va voir la methode file config ou dict config.
Et pour cela, nous allons créer un fichier dans notre dossier.
Et puis on défini les enregistreurs, les gestionnaires
et les formateurs dans ce fichier.
"""
# logging.config.fileConfig('logging.conf')

# logger = logging.getLogger('simpleExample')
# logger.debug('this is a debut message')

"""
ON va voir la methode de capture de pile dans notre verrou.
Cela peut etre tres utile pour resoudre les problémes dans le code
en nous donnant la trace de l'erreur qui se effectuais.
"""
# supposons que nous voulons voir ligne d'erreur dans le code
# try:
#     a = [1, 2, 3]
#     val = a[4]
# except IndexError as e:
#     logging.error(e, exc_info=True)
# except:
#     logging.error("this error is %s", traceback.format_exc())

"""
on va voir la methode de rotation des gestionnaires de fichiers.
on suppose qu'on a une grande application avec de nombreux messages
de journal e qu'on souhaite et qu'on veut garder une trace des
evenements les plus recents.
Donc, on peut utiliser un gestionnaire de fichier rotatif qui 
va maintenir les fichiers petits.
"""
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# rouler sur 2 Ko après et conserver les journaux de sauvegarde app.log.1, app.log.2, etc.
# handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
# logger.addHandler(handler)

# creation d'un gestionnaire de fichier à rotation chronometrée
handler = TimedRotatingFileHandler('timed_test.log', when='S', interval=5, backupCount=5)
logger.addHandler(handler)

for _ in range(6):
    logger.info('hello world')
    time.sleep(5)