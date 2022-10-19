# Destructor is called when the object is destroyed.

class Student:
    """
    __init__ is constructor
    __del__ is destructor
    """
    
    # constructor
    def __init__(self, name):
        print('Inside Constructor')
        self.name = name
        print('Object initialized')

    def show(self):
        print('Hello, my name is', self.name)

    # destructor
    def __del__(self):
        print('Inside destructor')
        print('Object destroyed')


# create object
s1 = Student('Hjwasim')
s1.show()

#__del__ It will only invoke when all references to the objects get deleted.
#delete object
del s1
