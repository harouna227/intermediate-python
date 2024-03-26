# Module Collections: Counter, namedtuple, orderedDict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque


# The deque: est une file d'attente à double extrémité.
#           Et, peut etre utilisé pour ajouter ou supprimer
#           aux deux extrémités. Et les deux sont mis en
#           en oeuvres de maniére à ce que cela soit trés 
# d = deque()
# d.append(1)
# d.append(2)
# print(d)

# d.appendleft(3)
# print(d)

# d.rotate(-1)
# d.extend([4, 5, 6])
# d.extendleft([4, 5, 6])
# d.popleft()
# d.pop()
# d.clear()
# print(d)



# The Defaultdict: Est similaire au conteneur de dictionnaire
#                habituel, à la seule difference qu'il aura une
#                une valeur par defaut si la clé n'a pas encore été définie.
# d = defaultdict(int)
# d['a'] = 1
# d['b'] = 2
# print(d['a']) 


# The orderedDict: Est un dictionnaire ordinaire, mais
#                  il se souvient de l'ordre dans lequel
#                  les elts ont été insérés.

# ordered_dict = OrderedDict()
# ordered_dict['b'] = 2
# ordered_dict['c'] = 3
# ordered_dict['d'] = 4
# ordered_dict['a'] = 1
# print(ordered_dict)


# A nemedtuple: est un type d'objet facile à créer 
#              et leger, similaire à une structure

# point = namedtuple('point', 'x, y')
# pt = point(1, -4)
# print(pt)
# print(pt.x, pt.y) # accès aux points



# A Counter: Est un conteneur qui stock les elements
#           sous forme de clés de dictionnaire et leurs
#           comptes sous forme de valeurs de dictionnaire

# a = "aaaabbbccc"
# my_counter = Counter(a)
# print(my_counter)

# print(my_counter.most_common()) # elmt le + courant
# print(my_counter.most_common(1)[0][0])
 
# on peut egament utiliser une liste ou tout autre iterable
# print(my_counter.elements()) # information: if iterable or no
# print(list(my_counter.elements())) # converti en liste


# print(my_counter.values())
# print(my_counter.keys())
# print(my_counter.items())
