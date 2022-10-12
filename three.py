#I will now introduce multithreading and multiproccessing
import threading
import time
import multiprocessing

def myfunc1(a):
    time.sleep(a)
    print('function 1 is done')

def myfunc2(b):
    time.sleep(b)
    print('function 2 is done')

def myfunc3(c):
    time.sleep(c)
    print('function 3 is done')

#print(threading.active_count())
#print(threading.enumerate())

if __name__ == '__main__':

    A = threading.Thread(target=myfunc1, args=(2,))
    A.start()

    B = threading.Thread(target=myfunc2, args=(4,))
    B.start()

    C = threading.Thread(target=myfunc3, args=(6,))
    C.start()


    print(threading.active_count())
    print(threading.enumerate())
    print(time.perf_counter())

'''This is an example of multithreading, where the main thread is replaced by several ones, 
these multipiple threads allow for a lower level form of concurrency, each argument in passed into
the args key word argument, each thread is created sort of like an object, and then must be started with 
the start function'''


