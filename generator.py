import generator
import sys

"""
les generateurs d'etat ou les fonctions qui renvoient
un objet pouvant etre iteré. 
Et la particularité est qu'ils generent pareusement
les element à l'interieur de l'objet, ce qui signifie
qu'ils generent les elements un seul à la fois et uniquement
lorsque vous le demander.
Et pour cette raison, ils sont beaucoup plus efficace
en terme de memoire que les autres objects sequence
lorsqu'on doit gerer de grands ensemble de données.
Il s'agit d'une puissante technique Python avancée.
"""

""" Exemple pratique des generateurs"""
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
    
# fib = fibonacci(30)
# for i in fib:
#     print(i)

""" Les expressions generatrices:
    elles ecrites de la meme maniere, comme les
    comprehension de listes, mais avec des parentheses
    au lieu de crochets. Et il s'agit d'une syntaxe et 
    d'un raccourci tres simple d'implementer l'expression du generateur.
"""
mygenerator = (i for i in range(10000) if i % 2 == 0)
# for i in mygenerator:
#     print(i)
# print(list(mygenerator))
print(sys.getsizeof(mygenerator))

mylist = [i for i in range(10000) if i % 2 == 0]
print(sys.getsizeof(mylist))



""" Regardons de plus prés l'exécution d'une fonction generatrice"""
def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

# cd = countdown(4)

# value = next(cd)
# print(value)

# print(next(cd))
# print(next(cd))
# print(next(cd))

""" Voila maintenant le gros avantage des generateurs"""
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums
    # Quand j'execute de fonction tous les nombres
    # seront stockés dans cette liste. Cela prend beaucoup de memoire.
# print(sum(firstn(10)))

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

# print(sum(firstn_generator(10)))

""" Comparaison """
# print(sys.getsizeof(firstn(100)))
# print(sys.getsizeof(firstn_generator(100)))


def mygenerator():
    yield 1
    yield 2
    yield 3

# g = mygenerator()

# print(sorted(g))

# value = next(g)
# print(value)

# value = next(g)
# print(value)

# value = next(g)
# print(value)

# value = next(g)
# print(value)