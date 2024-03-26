# Strings: ordered, immutable, text representation

# formatage: %, .format(), f-string

# First Method
# var = 'Tom' 
# my_string = "the variable is %s" % var
# var = 2
# my_string = "the variable is %d" % var
# var = 3.88005544
# my_string = "the variable is %f" % var # on peut specifier le nombre apres la virgule en fait %.2f or %.3f, etc
# print(my_string)

# Second Method
# var = 'Tom'
# my_string = "the variable is {}".format(var)
# var = 3.01263
# var2 = 2
# my_string = "the variable is {:.2f} and {}".format(var, var2)

# Therd Method
# var = 3.01263
# var2 = 2
# my_string = f"the variable is {var} and {var2}"
# print(my_string)



# from timeit import default_timer as timer
# my_list = ['a'] * 1000000

# bad
# start = timer()
# my_string = ''
# for i in my_list:
#     my_string += i
# stop = timer()
# print(stop-start)

# good
# start = timer()
# my_string = ''.join(my_list)
# stop = timer()
# print(stop-start)




# my_list = my_string.split(",") # converte my_string en liste
# print(my_list)
# new_string = ' '.join(my_list) # converte list to string
# print(new_string)


# print(my_string.lower())
# print(my_string.upper())
# print(my_string.startswith('H'))
# print(my_string.endswith('d'))
# print(my_string.find('o')) # renvoit la position
# print(my_string.count('o'))
# print(my_string.replace('world', 'universe')) 



 



# strip pour effacer les espace en debut et fin de la chaine
# my_string = my_string.strip()

