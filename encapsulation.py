"""
Best example for encapsulation is class.
Class contains variables and methods, this is encapsulati
We capsuled everything into one single unit.
Encapsulation prevents direct access to variables, instead do access using getter/setter methods
Proper encapsulation concept = getter/setter, private or protected variables
"""
class Employee:
    # constructor
    def __init__(self, name, salary):
        # public instance instance
        self.name = name
        # private instance instance.
        # __ means private
        self.__salary = salary

    def getSalary(self):
        return self.__salary
    
# creating object of a class
emp = Employee('Hjwasim', 10000)

# accessing private data members
#print('Salary:', emp.__salary) 
# it will throw an error
# Encapulation supports data hiding, we cannot access directly

#To access we need method 
print('Salary:', emp.getSalary()) 