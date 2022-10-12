class Vector:


    def __init__(self, dim, tensor):
        self.dim=dim
        self.tensor=tensor

    def __repr__(self):
        print(f"You have printed a {self.dim} dimensional vector")
        if self.tensor == False:
            print("it isnt a tensor")
        else:
            print("It is a tensor")
'''This covers the basics of dunder methods, double underscore methods that allow for deeper OOP'''