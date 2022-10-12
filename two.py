import contextlib as clib

with open('test.txt', 'w') as file:
    file.write('testing\n')

@clib.contextmanager
def fileManager(filename, method):
    file = open(filename, method)
    yield file
    file.close()

with fileManager('text.txt', 'w') as f:
    f.write('TESTING\n')
    #f.close()

'''these are some basic implementations of context managers, they allow you to bug free
deal with files '''


