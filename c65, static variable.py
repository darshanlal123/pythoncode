# Static Variables: 
"""
☕ If the value of a variable is not varied from object to object, such type of variables we have to declare with in the class directly but outside of methods. Such types of variables are called Static variables. 
☕ For total class only one copy of static variable will be created and shared by all objects of that class. 
☕ We can access static variables either by class name or by object reference. But recommended to use class name.
"""
# Instance Variable vs Static Variable:

"""
☕ In the case of instance variables for every object a seperate copy will be created,but in the case of static variables for total class only one copy will be created and shared by every object of that class."""

# class Student:
#     college ="KVS varanasi"
#     def __init__(self,name, rollno):
#         self.name= name
#         self.age = rollno

# s1 = Student("Arvind",88)
# s2 = Student("darshan",26)

# print(s1.name, s1.college)
# print(s2.name, s2.college)





# Various Places to declare Static Variables:

"""
1) In general we can declare within the class directly but from out side of any method 
2) Inside constructor by using class name 
3) Inside instance method by using class name 
4) Inside classmethod by using either class name or cls variable 
5) Inside static method by using class name
"""

# class Test: 
#     a=10
#     def __init__(self):
#         Test.b=20

#     def m1(self):
#         Test.c=30

#     @classmethod
#     def m2(cls):
#         cls.d1=40 
#         Test.d2=400 

#     @staticmethod
#     def m3():
#         Test.e=50


# print(Test.__dict__)
# t=Test()
# print(Test.__dict__)
# t.m1()
# print(Test.__dict__) 
# Test.m2() 
# print(Test.__dict__) 
# Test.m3() 
# print(Test.__dict__)
# Test.f=60 
# print(Test.__dict__)




# How to access Static Variables: 

""" 
1) inside constructor: by using either self or classname 
2) inside instance method: by using either self or classname 
3) inside class method: by using either cls variable or classname 
4) inside static method: by using classname 
5) From outside of class: by using either object reference or classname"""

# Where we can modify the Value of Static Variable:

"""Anywhere either with in the class or outside of class we can modify by using classname. But inside class method, by using cls variable."""

"""If we change the Value of Static Variable by using either self OR Object Reference Variable: If we change the value of static variable by using either self or object reference variable, then the value of static variable won't be changed, just a new instance variable with that name will be added to that particular object."""


# How to Delete Static Variables of a Class 
"""1) We can delete static variables from anywhere by using the following syntax 

del classname.variablename


2) But inside classmethod we can also use cls variable 

del cls.variablename"""


"""Note: 


⚽ By using object reference variable/self we can read static variables, but we cannot modify or delete. 
⚽ If we are trying to modify, then a new instance variable will be added to that particular object. 
⚽ t1.a = 70 
⚽ If we are trying to delete then we will get error."""