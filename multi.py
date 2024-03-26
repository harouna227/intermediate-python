from multiprocessing import Process
import os
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

# if __name__ == '__main__':

#     processes = []
#     num_processes = os.cpu_count()

#     # create processes
#     for i in range(num_processes):
#         p = Process(target=square_numbers)
#         processes.append(p)

#     # start
#     for p in processes:
#         p.start()

#     #join
#     for p in processes:
#         p.join()

#     print('End main')

"""
MultiThreading.
L'api de threading est donc tres similaire a la precedente api.
l'api multiprocessing est tres similaire à l'api multithreading.
"""
from threading import Thread

if __name__ == '__main__':

    threads = []
    num_threads = 10

    # create processes
    for i in range(num_threads):
        t = Process(target=square_numbers)
        threads.append(t)

    # start
    for t in threads:
        t.start()

    #join
    for t in threads:
        t.join()

    print('End main')