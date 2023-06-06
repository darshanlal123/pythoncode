# decorator 
def decor(func):    #<---this is taking a funtion as argument, funtion name can be anything
    def inner():    # <---this is inner function responsible to enhance the feature
        print("this is exicution of decor function")
    return inner    #  <--- it return the funtion object to the test fuction, not a a function but function object.

@decor 
def test():
     print("this is main function exicution...")

test()