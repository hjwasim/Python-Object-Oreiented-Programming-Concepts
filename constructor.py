"""
Python class supports 3 types of constructor

Default constructor
    - just empty constructor
Non-parameterized constructor 
    -No parameters excluding self, but it can initialize variables with default values
Parameterized constructor -
    It accepts Multiple parameters including self, we assign our parameter values to the variables presented in the class.
"""
class Example1:
    def __init__(self):
        print("Default Constructor")
        
class Example2:
    def __init__(self):
        self.message = "Hiiiii!...."
        print("Non-parameterized Constructor")
        
class Example3:
    def __init__(self,message):
        print("Parameterized Constructor")
        self.message = message
        # print(self.message)