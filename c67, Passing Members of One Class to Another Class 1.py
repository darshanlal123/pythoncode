# Passing Members of One Class to Another Class:

class Employee:
    def __init__(self, ename, eno, esal):
        self.ename = ename
        self.eno = eno
        self.esal = esal

    def display(self):
        print("Employee number : ", self.eno)
        print("Employee name : ", self.ename)
        print("Employee salary : ", self.esal)


class Test:
    def modify(emp):
        emp.esal = emp.esal+1000
        emp.display()

'''what happen here is all the member of employee come in 'e' object and clculation are taken care by new Test class

and here emp.esal refrencing the same object which is reffrenced by self.esal ---> objecwt value changes and reflacted every where
'''
e = Employee("darshan", 58, 1000)
Test.modify(e)
