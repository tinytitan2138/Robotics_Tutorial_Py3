def setName(name):
    if not isinstance(name, str):
        raise TypeError
    else:
        return name

def setAge(age):
    if not isinstance(age, int):
        raise TypeError
    else:
        return age

def setRace(race):
    if not isinstance(race, str):
        raise TypeError
    else:
        return race

class Human:



    def __init__(self, name, age, race):
        self.name = setName(name)
        self.age = setAge(age)
        self.race = setRace(race)

    def hello(self, name):
        print(f"Hello {name}")


#The essential description with the init dunder method and a defined function

class Wagie(Human):
    def work(self, hours):
        print(f"{self.name} has worked for {hours} hour(s)")
#basic inhereticance and defined functions within class

class nine_to_five(Wagie):
    def work(self, hours, location):
        print(f"{self.name} has worked for {hours} hour(s) at {location}")
# basic polymorphism, essentially redefining functions within classes.



