import json

"""
JSON: JavaScript Objet Notation.
C'est un format de données leger utilisé pour
l'échange de données. il est généralement utilisé
dans les application Web.
"""
# person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, 'title': ["engineer", "programmer"]}
# Convertir un dictionnaite python en un objet JSON

# personJson = json.dumps(person, indent=4, separators=('; ', "= "), sort_keys=True)
# print(personJson)

"""
Desormais je peux également le convertir ou le transferer
dans un fichier.
"""
# with open('person.json', 'w') as file:
#     json.dump(person, file, indent=4)


"""
On peut convertir les données JSON en dictionnaire python 
"""
# personJson = json.dumps(person, indent=4, sort_keys=True)
# person = json.loads(personJson)
# print(person)

"""
Si on souhaite aussi convertir à partir d'un fichier
Json avec la methode de chagerment par point json.
C'est ainsi, on peut decoder les données coorigées.
"""
# with open('person.json', 'r') as file:
#     person = json.load(file)
#     print(person)

"""
Maintenant, dans ce cas nous travaillons avec un dictionnaire.
Disons que nous avons un objet personnalisé.
supposons donc qu'on a une classe personnalisée.
"""
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age 

user = User('Max', 27)

# Creons une fonction d'encodage personalisée
def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')

# userJSON = json.dumps(user, default=encode_user)
# print(userJSON)


"""
Il y'a également une deuxiéme methode d'implementer
un encodeur JSON personnalisé.
"""
from json import JSONEncoder
class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)

# userJSON = json.dumps(user, cls=UserEncoder)
    
# je peux directement utiliser cet encodeur aussi.UserEncoder
# userJSON = UserEncoder().encode(user)
# print(userJSON)

"""
Decoder nos objets.
Disons que j'ai ici un utilisateur au format JSON.
Et je veux l'avoir dans un objet python normal.
"""
# donc là, je ne peux pas appeler le nom du pt utilisateur
# car ce n'est pas un objet utilisateur.

# user = json.loads(userJSON)
# print(user.name)

"""
Pour appeler l'objet utilisateur, je dois donc
ecrire une methode de décodage personnalisée.
"""
def decode_user(dict):
    if User.__name__ in dict:
        return User(name=dict['name'], age=dict['age'])
    return dict

# user = json.loads(userJSON, object_hook=decode_user)
# print(user.name)
