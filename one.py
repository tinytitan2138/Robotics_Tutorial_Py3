from functools import reduce
import functools as ft
from OOP import Human, Wagie, nine_to_five
from five import Vector

#variables, condittionals, if statements, functions
bool = True
bool2 = False
var1 = 5
var2 = 0.3
name = 'hello' #basic variables, booleans, interpereted ints long and floats, and a string
tup = [('name', 5), ('hello', 3)]
dict = {"name": "solomon", "age": 16}
#these are lists, tuples, and dictionaries

for i in range(1,11):
    print(i)
k = 0
while k < 10:
    print(k)
    k += 1
# for and while loops, prints 1 to 10 and 0 to 9
def func(bool):
    print(bool)

if (bool):
    func(bool)

#lambda functions, OOP, args and kwargs

myfunc1 = lambda x,y: x*y
print(myfunc1(x=5, y=5))
print(myfunc1(y=5, x=5))
#lambda functions are to be written in the same format as
#functions within discrete maths, conditionals can also be
#implemented within lamdba
n = [1,2,3,4,5]
myfunc2 = lambda x: x+5
print(list(map(myfunc2, n)))
#the map function function allows us to "map"
# a function to each element within some list, since
# the lamdba function returns a bunch of values, we need
# the list function in order to structure them.

n = [1,2,3,4,5,6,7,8,9,10]
myfunc3 = lambda x: x>=5
print(list(filter(myfunc3, n)))
# the filter function allows a certain iterable datatype
# to go through some conditional, thus printing only
# the values >= 5
n = [4,3,2,1]
myfunc4 = lambda x,y: x*y
print(reduce(myfunc4, n))
# the reduce function applies some function to the continious
# values within the list, so it prints 4 * 3 = 12, 12 * 2 = 24, 24 * 1 = 24
# this could potentially be implemented into a factorial function perhaps

#5! = 5 * 4 * 3 * 2 * 1, n! = n * n-1 * n-2

def fact(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))
# just some random fun recursion

list1 = [('a', 50), ('b', 30), ('c', 10)]
list1.sort(key=lambda x: x[0], reverse=False)
print(list1)
list1.sort(key=lambda x: x[1], reverse=False)
print(list1)
''' the sort function allows us to use the key keyword argument to
 to describe in detail how we want our list to be sorted. '''

list1 = [{"name": "Solomon Saleh", "age": 16, "dead": False}, {"name": "Thomas",
"age": 14, "dead": False}, {"name": "Albert Einstein", "age": 141, "dead": True}]
list2 = sorted(list1, key=lambda x: x['name'], reverse=False)
list3 = sorted(list1, key=lambda x: x['age'], reverse=False)
list4 = sorted(list1, key=lambda x: x['dead'], reverse=False)
print(list2)
print(list3)
print(list4)

'''the sorted function returns a list where it is sorted based on the key 
key word argument, in this case it is a lambda function with the parameter described 
as the word with the value as what is being ordered by'''

#now we must review OOP

test = Human("Solomon", 16, "NA")

test2 = Wagie("Squidward", 30, "Squid")
test2.work(12)

test3 = nine_to_five("bob", 30, "NA")
test3.work(hours=8, location="Corporate")

#you write the name of the object this way and call its function accordingly

def myfunc(*args, **kwargs):
    for i in args:
        print(*i,sep="\n")
    for k,v in kwargs.items():
        print(type(v))

myfunc([1,2,3,4,5], one=False, two="HELLO")
'''these functions describe the basics of args and kwargs, that you can pass in 
any number of positional and keyword arguments and perform some general code with it.'''

#some advanced skills include generators decorators and context managers, as well as parrelel programming

def mydec(myfunc):
    @ft.wraps(myfunc)
    def mywrapper(*args, **kwargs):
        print("start")
        a = myfunc(*args, **kwargs)
        print(a)
        print("end")
        return a

    return mywrapper

@mydec
def myfun(name, message, exit):
    print(f"Hello {name}, {message}, {exit}")
    return 10
myfun(name="Solomon", message="I hate you", exit="goodbye")

'''this is the basic idea behind a decorator, to describe the extended functionality of 
a function, in this case we just added start and ending messaged, the extending functionality
can be times or even context managers.'''

def fib(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def myGen(limit):
    n = 2
    phi = fib(n) / fib(n-1)
    while n <= limit:
        phi = fib(n) / fib(n-1)
        n += 1
        yield phi

#z = myGen(10000)
#for i in z:
    #print(i)

'''this basic code defines what a generator is and does, you define a yielded value, 
over the course of many iteration these values are added to some sequence which an iterable
object, the above example prints the approximation of the golden ratio'''

myvector = Vector(dim=5, tensor=True)
repr(myvector)

