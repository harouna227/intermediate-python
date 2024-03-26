# itertools: product, permutations, combinations, accumulate, groupby, and infinite iteraors
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby


# persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
#            {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

# def smaller_than_3(x):
#     return x < 3

# a = [1, 2, 3, 4]
# group_obj = groupby(persons, key=lambda x: x['age'])
# for key, value in group_obj:
#     print(key, list(value))


# import operator
# e = [1, 2, 5, 3, 4]
# # acc = accumulate(e, func=operator.mul)
# acc = accumulate(e, func=max) # retunr le max de la comparaison
# print(e)
# print(list(acc))


# d = [1, 2, 3, 4]
# comb = combinations(d, 2)
# print(list(comb))
# comb_wr = combinations_with_replacement(d, 2)
# print(list(comb_wr))


# c = [1, 2, 3]
# perm = permutations(c, 2) # longueur en 2eme arg pas obligatoire
# print(list(perm))

# a = [1, 2]
# b = [3]
# prod = product(a, b, repeat=2) # longueur en 2eme arg pas obligatoire
# # print(prod) # Montre le type itertools 
# print(list(prod))