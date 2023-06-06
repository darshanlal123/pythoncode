#  Instance Variables: 
"""If the value of a variable is varied from object to object, then such type of variables are called instance variables. 
For every object a separate copy of instance variables will be created.

# Where we can declare Instance Variables: 
# 1) Inside Constructor by using self variable
# 2) Inside Instance Method by using self variable 
# 3) Outside of the class by using object reference variable"""



# Inside Constructor by using Self Variable: 
"""We can declare instance variables inside a constructor by using self keyword. Once we creates object, automatically these variables will be added to the object."""

# class Student:
#     #constuctor
#     def __init__(self): 
#         #instance variable
#         self.name = "darshan"
#         self.rollno = 55
#         self.age = 30

# s = Student()
# print(s.__dict__)

# inside instance method
"""We can also declare instance variables inside instance method by using self variable. If any instance variable declared inside instance method, that instance variable will be added once we call taht method."""



# class Test:
#     def __init__(self):
#         self.a =25
#         self.b =30
    
#     def m1(self):
#         self.c = 50


# t = Test()
# print(t.__dict__)
# t.m1()
# print(t.__dict__)




# Outside of the Class by using Object Reference Variable:
"""We can also add instance variables outside of a class to a particular object."""


# class Test:
#     def __init__(self):
#         self.a =25
#         self.b =30
    
#     def m1(self):
#         self.c = 50

# t= Test()
# print(t.__dict__)
# t.d=60
# print(t.__dict__)


# How to delete Instance Variable from the Object:

"""1) Within a class we can delete instance variable as follows 
del self.variableName

2) From outside of class we can delete instance variables as follows 
del objectreference.variableName"""


"""If we change the values of instance variables of one object then those changes won't be reflected to the remaining objects, because for every object we are separate copy of instance variables are available."""

# class Test:
#     def __init__(self):
#         self.a =25
#         self.b =30
#         self.c = 50
    
#     def m1(self):
#         del self.c

# t = Test()
# print(t.__dict__)
# t.m1()
# print(t.__dict__)
# del t.a
# print(t.__dict__)

# # another object(uniffected)
# t1 =Test()
# print(t1.__dict__)


        