# inner class 2
class Person:
    def __init__(self):
        self.name="darshan"
        self.db =self.DOB()
    def display(self):
        print("Name : ", self.name)
    
    class DOB:
        def __init__(self):
            self.dd = 13
            self.mm = 10
            self.yy = 97

        def display(self):
            print('DOB = {}/{}/{}'.format(self.dd, self.mm, self.yy))
            

p= Person()
p.display()

x= p.db
x.display()