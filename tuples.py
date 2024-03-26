# Tuple: ordered, imutable, allow duplicate elements

# comparaison entre une liste et un tuple
import sys
my_list = [0, 1, 2, 'hello', True]
my_tuple = (0, 1, 2, 'hello', True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

# comparaison entre une liste et un tuple avec le module timeit
import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))



# a = (0, 1, 2, 3, 4)
# i1, *i2, i3 = a
# print(i1)
# print(i3)
# print(i2)

#affectation
# my_tuple = "Max", 23, "Boston"
# name, age, city = my_tuple
# print(name)
# print(age)
# print(city)


#accès avec les slices
# b = a[:: -1]
# print(b)

# tuple en liste et vise versa
# my_list = list(mytuple)
# print(my_list)
# my_tuple = tuple(my_list)
# print(my_tuple)

# print(mytuple.count('p')) 

# print(mytuple.index('p')) 

