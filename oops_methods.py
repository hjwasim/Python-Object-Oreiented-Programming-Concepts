"""
Methods is nothing. It just functions inside the class
Python class supports 3 types of methods
-Class methods
-Instance methods
-Static Methods
"""


class InstanceMethodClass:
    cname = "python"
    #To create instance_method, put self as a parameter
    #Access to class and instance variables
    #Instance_methods contains self
    def instance_method(self):
        return "This is an instance method."

instancevar = InstanceMethodClass()

# We can call instance methods using object, we can any no.of parameters for instance variable initialization.
# self automatically passed by python
print(instancevar.cname) 
print(instancevar.instance_method())
#If We call instance method using Classname,we must pass our reference_variable/object to the method parameter
print(InstanceMethodClass.instance_method(instancevar))

class ClassMethodClass:
    # To create static method, we need @classmethod decorator.
    # we must give 'cls' like self as parameter to class methods
    # No access to class attributes
    cname = "Hiiii"

    @classmethod
    def class_method(cls):
        print(cls.cname)  # class variables only accesible, Not instance variable
        return "This is a class method."


clsvar = ClassMethodClass()
# We can call class methods using object or classname.
print(clsvar.class_method())
print(ClassMethodClass.class_method())

class StaticMethodClass:
    # To create static method, we need @staticmethod decorator.
    # No access to class attributes
    @staticmethod
    def static_method():
         # we cannot access any class/instance attributes
        return "This is a static method."


static = StaticMethodClass()
# We can call static methods using object or classname.
print(StaticMethodClass.static_method())
print(static.static_method())
