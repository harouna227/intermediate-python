"""
Il y a deux type de decorateur.
les decorateurs de fonction et les decorateurs de classe.
La fonction decorateur est plus courante.
"""

"""Decorateur sans Argument:"""

# def start_end_decorator(func):
    
#     def wrapper():
#         print('Start')
#         func()
#         print('End')
#     return wrapper

# @start_end_decorator
# def print_name():
#     print("Alex")

# # print_name = start_end_decorator(print_name)
# print_name()

"""Decorateur avec Argument"""
import functools
from typing import Any
def mydecorator(func):
    
    @functools.wraps(func) # reserve les info de ma fonction utilisée
    def wrapper(*args, **kwargs):
        # Faire quelque chose avant....
        result = func(*args, **kwargs)
        # Faire quelque chose aprés....
        return result
    return wrapper

@mydecorator
def add10(x):
    return x + 5

# result = add10(10)
# print(result)
# print(help(add10))
# print(add10.__name__)

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=5)
def greet(name):
    print(f"hello {name}")

# greet("Haroun")
    
"""
Parlons maintenant des décorateurs imbriqués.
On peut impriquer les décorateurs les ainsi apres les autres.
"""
def start_end_decorator(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

def debug(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

@debug
@start_end_decorator
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting

# say_hello("Haroun")

"""
Les decorateurs de classe font la meme chose que celui de fonction.
Mais on les utilise generalement quand on veut maintenir
et mettre à jour un etat.
"""

class CountCalls():

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is excecuted {self.num_calls} times")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print('Hello')

# say_hello()
# say_hello()

"""
Maintenant parlons de qlq cas d'utilisation typiques
des decorateurs.
- on peut implementer un decorateur de niluterie
  pour calculer le temps d'execution d'une fonction.
- on peut utiliser un decorateur de debogage. 
- on peut utiliser un decorateur de controle pour 
  verifier so les arguments remplisent certaines exigences
  et la profondeur du comportement en consequence.
- on peut enregistrer des fonctions comme des plug-in,
  aupres de decorateur, on peut mettre en cache les valeurs de retour.
- on egalement ajouter des informations ou mettre à jour.
"""