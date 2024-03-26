# lambda arguments: expression

# la fonction reduce(func, seq)
# from functools import reduce
# a = [1, 2, 3, 4]

# product_a = reduce(lambda x,y: x*y, a)
# print(product_a)

# la fonction filter(func, seq)
# a = [1, 2, 3, 4, 5, 6]
# b = filter(lambda x: x%2==0, a)
# print(list(b))
# # on peut celui d'haut avec la comprehension de liste
# c = [x for x in a if x%2==0]
# print(c)

# la fonction map(func, seq)
# a = [1, 2, 3, 4, 5]
# b = map(lambda x: x*2, a)
# print(list(b))
# # on peut celui d'haut avec la comprehension de liste
# c = [x*2 for x in a]
# print(c)


# points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
# Tri en fonction des sommes de chaque tuple
# Voilà donc la methode du segent avec lambda comme argument clé
# points2D_sorted =  sorted(points2D, key=lambda x: x[0] + x[1])

# points2D_sorted =  sorted(points2D, key=lambda x: x[1])

# print(points2D)
# print(points2D_sorted)


# add10 = lambda x: x + 10
# print(add10(5))

# def add10_func(x):
#     return x + 10

# mult = lambda x, y: x * y
# print(mult(2,3))