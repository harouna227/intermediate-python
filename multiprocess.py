from multiprocessing import Process, Value, Array, Lock
from multiprocessing import Queue, Pool
import time

"""
Partage de données entre les processus
Pour les processus, ceux-ci ne vivent pas dans le meme 
espace memoire, ils n'ont donc pas accès aux memes données publiées.
Pour cette raison, ils ont besoin d'objets de memoire partagée
speciaux pour partager des données.

Et il existe deux objets de memoire partagée que nous
pouvons utiliser:
- on peut utiliser une valeur unique
- on peut egalement utiliser un tableau.
"""


""" Utisation avec valuer unique"""
def add100(number, Lock):
    for i in range(100):
        time.sleep(0.01)
        with Lock:
            number.value += 1

# if __name__ == '__main__':
    
    # lock = Lock()
    # share_number = Value('i', 0)
    # print('Number at beginning is', share_number.value)

    # p1 = Process(target=add100, args=(share_number, lock))
    # p2 = Process(target=add100, args=(share_number, lock))

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    # print('Number at end is', share_number.value)

    # print("End main")


""" Utilisation avec un tableau """
def add_100(numbers, Lock):
    for i in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            with Lock:
                numbers[i] += 1

# if __name__ == '__main__':
    
#     lock = Lock()
#     shared_array = Array('d', [0.0, 100.0, 200.0])
#     print('Array at beginning is', shared_array[:])

#     p1 = Process(target=add_100, args=(shared_array, lock))
#     p2 = Process(target=add_100, args=(shared_array, lock))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     print('Array at end is', shared_array[:])

#     print("End main")


""" 
Un file d'attente peut etre utilisée pour des echanges 
de données sécurisées.
"""
def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)

def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1*i)

# if __name__ == '__main__':

#     numbers = range(1, 6)
#     q = Queue()

#     p1 = Process(target=square, args=(numbers, q))
#     p2 = Process(target=make_negative, args=(numbers, q))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     while not q.empty():
#         print(q.get())

#     print("End main")


""" Pool de Processus: Process Pool 
On les utilise pour gerer plusieurs processus.
Un objet pool de processus controle un pool de processus
de travail auquel les cotelettes peuvent etre soumises.
Et il peut gerer pour les processus disponibles et diviser.
Par exemple, les données en morceaux plus petits, qui peuvent
ensuite etre traités en parallele par differents processus. 
"""

def cuber(number):
    return number * number * number

if __name__ == '__main__':

    numbers = range(10)
    pool = Pool()

    # map, apply, join, close
    result = pool.map(cuber, numbers)

    pool.close()
    pool.join()

    print(result)