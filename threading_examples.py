from threading import Thread, Lock, current_thread
from queue import Queue
import time


def square_numbers():
    for i in range(100):
        i * i

# if __name__ == '__main__':

#     """ Creation et Demarrage d'un thread"""
#     threads = []
#     num_threads = 10

#     # create processes
#     for i in range(num_threads):
#         t = Thread(target=square_numbers)
#         threads.append(t)

#     # start
#     for t in threads:
#         t.start()

#     #join
#     for t in threads:
#         t.join()

#     print('End main')

"""
- Comment paratger des données entre les threads
- Comment utiliser les verrous pour eviter les conditions de concurrence
- Nous apprenons egalement ce qu'un processus démon et 
    comment utiliser une file d'attente pour les echanges de données thread-safe
"""

""" Comment paratger des données entre les threads """

# database_value = 0

def incrise(Lock):
    global database_value

    # Deuxieme facon d'utiliser lock avec with
    with Lock:
        local_copy = database_value
        # Traitement
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy

    # Premiere facon d'utiliser lock    
    # Lock.acquire()
    # local_copy = database_value
    # # Traitement
    # local_copy += 1
    # time.sleep(0.1)
    # database_value = local_copy
    # Lock.release()

# if __name__ == "__main__":

    # lock = Lock()
    # print('Start value', database_value)

    # thread1 = Thread(target=incrise, args=(lock,))
    # thread2 = Thread(target=incrise, args=(lock,))

    # thread1.start()
    # thread2.start()

    # thread1.join()
    # thread2.join()

    # print('End value', database_value)

    # print('End main')


"""
Une condition de concurrence critique se produit, 
lorsque deux threads ou plus tentent de modifier 
la meme variable en meme temps.
Danc ce cas on utilise LOOK en l'important
"""


""" Les files d'attentes: structure de données linaire qui suit le principe FIFO
Ils sont donc excellent pour les echange de données et
traitement de données securisées par les threads et les
processus dans des environnements multithreads ou 
multiprocessing.
"""

def worker(q, Lock):
    while True:
        value = q.get()
        # traitement
        with Lock:
            print(f'in {current_thread().name} got {value}')
        q.task_done()

if __name__ == "__main__":

    """ Creation d'une file d'attente """
    # q = Queue()

    # q.put(1)
    # q.put(2)
    # q.put(3)

    # # 3, 2, 1 --> sortie
    # first = q.get()
    # print(first)

    # q.task_done()
    # q.join()

    """ Creatu=ion file d'attente with thread """

    q = Queue()
    lock = Lock()
    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q,lock))
        thread.daemon=True # Pas de daemon pas defaut
        thread.start()

    for i in range(1, 21):
        q.put(i)
    
    q.join()

    print("End main")
