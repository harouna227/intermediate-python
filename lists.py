# Lists: ordered, mutable, allows duplicate elements
mylist = [1, 2, 3, 4, 5, 6]

# comprenhension des listes
# une maniére de créer une liste sur une seule ligne
b = [x*x for x in mylist]
print(mylist)
print(b) 


# copy the orginal list: Trois façon de faire
#                       une copie avec les listes   
# list_cpy =  list_org.copy()
# list_cpy =  list(list_org)
# list_cpy =  list_org[:]
# list_cpy.append('lemon')
# print(list_cpy)
# print(list_org)



# # the slices
# a = mylist[::-1]
# print(a)

# # create list of 4 items
# mylist = [4] * 5
# print(mylist)


# # create new list and concat with either list
# mylist2 =[1, 2, 3, 4]
# new_list = mylist + mylist2
# print(new_list)




# #create new list
# new_list = sorted(mylist)
# print(mylist)
# print(new_list)


# # modify orginal list
# mylist.sort()
# print(mylist)

# item = mylist.clear()
# print(mylist)

# item = mylist.remove('banana')
# print(mylist)

# item = mylist.pop()
# print(item)

# mylist.append("lemon")
# print(mylist)

# mylist.insert(1, "bonbon")
# print(mylist)