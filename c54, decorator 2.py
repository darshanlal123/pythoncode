# decorator 2

def decor_multiplication(func):
    def solution(a,b):
        c=a*b # <===adding feature of multiplication
        print("your multiplication : ",c)
        func(a,b) #<=== again calling the add funtion to get result of addition
    return solution


@decor_multiplication
def add(a,b):
    c=a+b
    print("your sum is : ",c)

add(4,5)
