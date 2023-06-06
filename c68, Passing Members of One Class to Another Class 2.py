# Passing Members of One Class to Another Class:

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
    def display(self):
        print("Student name is : ",self.name)
        print("Student roll number is : ", self.roll)

class User:
    @staticmethod
    def show(object):
        object.display()

s= Student("darshan",88)
print(s.__dict__)
# s.display()
User.show(s)
