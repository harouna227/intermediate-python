# Sets: unordered, mutable, no duplicates

# on peut creer un frosenset (ensemble gelé qu'on
#                              ne peux modifier )
# example:
# a = frozenset([1, 2, 3, 4])
# a.add[1]
# print( a)


# Difference de deux sets
# setA = {1, 2, 3, 4, 5, 6} 

# copie de deux sets: copy or set()
# setB = setA.copy()
# setB = set(setA)
# setB.add(7)
# print(setB)
# print(setA)



# Vérification de sous ensemble
# --> Veriifier si setB est sous ensemble de setB
# print(setA.issubset(setB)) # --> Fasle

# --> Return vrai because elements setB sont in setA
# print(setA.issuperset(setB)) 

# Calculer si deux sets sont disjoins:
# --> si les deux sets ont une intersection nulle
# --> alors, ont de meme elements(pas de disjoinction)
# print(setA.isdisjoint(setB)) # --> Fasle

# --> pas de meme elements (disjoinction)
# print(setA.isdisjoint(setC))



# ************ Methode de modification ************
# modifier un set avec les methodes:

# setA.symmetric_difference_update(setB)
# print(setA)

# setA.difference_update(setB)
# print(setA)

# setA.intersection_update(setB)
# print(setA)  
 
# setA.update(setB)
# print(setA)

# diff = setA.symmetric_difference(setB)
# print(diff)

# diff = setA.difference(setB)
# print(diff)

# ******* Fin ******


# union et intersection
# odds = {1,3, 5, 7, 9}
# evans = {0, 2, 4, 6, 8}
# primes = {2, 3, 5, 7}
# u = odds.union(evans)
# print(u)
# i = evans.intersection(primes)
# print(i)

# parcourir un set
# for x in myset:
#     print(x)

# myset.remove(3)
# myset.discard()
# myset.clear()
# myset.pop()
# myset.add(4)

