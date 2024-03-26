# Dictionary: clé-valeur, unordered, mutable 




# Une methode pour fussioner deux dictionaires
# Appelée methode de mise à jour
# mydict = {"name": "Max", "age": 28, "email": "issif@gmail.com"}
# mydict2 = dict(name= "Mary", age= 27, city= "Boston")
# mydict.update(mydict2)
# print(mydict)

#copier un dictionaire
# mydict_cpy = mydict.copy()
# mydict_cpy = dict(mydict)
# mydict_cpy['email'] = 'issif@gmail.com'
# print(mydict_cpy)
# print(mydict)

# parcour un dictionaire:
# for key in mydict:
#     print(key)
# for key in mydict.keys():
#     print(key)
# for value in mydict.values():
#     print(value)
# for key, value in mydict.items():
#     print(key, value)


# check on element: with if or try/accept
# if "lastname" in mydict:
#     print(mydict["lastname"])
# try:
#     print(mydict["name"])
# except:
#     print("erreur")


#delete
# mydict.popitem()
# mydict.pop("name")
# del mydict["name"]
# print(mydict)

# modification 
# mydict["email"] = "issifi@gmail.com"
# print(mydict)

# accés aux valeurs
# valeur = mydict['age']
# print(valeur)