class Student:
    """Python supports 2 types of variables
        Class Variable/Static Variable
        Instance Variable
    """
    #Class Variable/Static Variable
    schoolName = "HJ School"
    #Instance Variable
    def __init__(self,name):
        print("=== Inside class ====")
        #We can access class/static variable using self and ClassName
        print(self.schoolName)
        print(Student.schoolName)
        
        self.name=name
        
myObj = Student("hjwasim")
myObj1 = Student("Code")

print("Student name is {}".format(myObj.name)) # Accessing Instace variables through object name.
print("Student name is {}".format(myObj1.name)) 
#Different student same school
print(myObj.schoolName) #HJ School
print(myObj1.schoolName) #HJ School

#Instance variables is changeable based on object, but class/static doesnt change. it is same for all the objects.