class Student:
    #constuctor
    def __init__(self, name, rollno, age): 
        #instance variable
        self.name = name
        self.rollno = rollno
        self.age = age

#object creation
s1 = Student("darshan", 55,6)
s2 = Student("kavi", 51,8)
s3 = Student("sam", 52,6)
s4 = Student("aditi", 53,5)



print(s1.name)
print(s2.name)
print(s3.name)
print(s4.name)
