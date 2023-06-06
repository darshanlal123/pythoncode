class Outer:
    def __init__(self):
        print("this is outer class")
    class Inner:
        def __init__(self):
            print("this is inner class")
        def m1(self):
            print("this is method of inner class")

outer_object = Outer() # on the object creation cunstructure of outer class exicuted
inner_object = outer_object.Inner() # on the object creation cunstructure of Inner class exicuted
inner_object.m1()


# Note: The following are various possible syntaxes for calling inner class method

# 1) outer_objec = Outer() 
# inner_object = outer_objec.Inner() 
# inner_object.m1()


# 2) inner_object = Outer().Inner() 
# inner_object.m1()


# 3) Outer().Inner().m1()