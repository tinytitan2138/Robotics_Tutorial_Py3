class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)
        print(class_name)
        return type(class_name, bases, attrs)

class Test(metaclass=Meta):
    name='spark'
    status='alive'

new = Test()

'''meta classes essentially allow you to describe the ins and outs on how classes are created within python 
they typical meta class that normal classes inherit from is called type. The best use of metaclasses are 
design patters.'''
