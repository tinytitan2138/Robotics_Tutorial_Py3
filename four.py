#this file will describe multiproccesing
import multiprocessing
import time
import functools as ft
import os

def performace(func):
    @ft.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} took {end_time-start_time} second(s) to complete")
    return wrapper

@performace
def computationallyLargeFunction(num):
    i = 0
    while i < num:
        #print(i)
        i += 1

if __name__ == '__main__':
    #computationallyLargeFunction(100)
    argument = 1000000
    A = multiprocessing.Process(target=computationallyLargeFunction, args=(argument/4,))
    B = multiprocessing.Process(target=computationallyLargeFunction, args=(argument/4,))
    C = multiprocessing.Process(target=computationallyLargeFunction, args=(argument/4,))
    D = multiprocessing.Process(target=computationallyLargeFunction, args=(argument/4,))

    print(f"Your cpu core count is given by the cpu_count function, for this computer it is "
          f"{os.cpu_count()}")
    A.start()
    B.start()
    C.start()
    D.start()

    A.join()
    B.join()
    C.join()
    D.join()

print(f"TIME ELAPSE: {time.perf_counter()}")

'''This is the basic example of multiprocessing, it is dependant on the number of cpu cores you have 
if you have a large computational problem it is easier to divide up the work amongst several cores 
rather than to just have it all run on the main thread. You create the process then pass in arguments
then start the process and join it, the join function essentially just tells the program to cancel once
the process is complete but this is automatic'''

