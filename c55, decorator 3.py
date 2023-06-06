# decorator 3

def decor_division(func):
    def solution(a,b):
        if a<b:
            c=b/a
            return c
        else:
            func(a,b) 
    return solution


@decor_division
def division(a,b):
    c=a/b
    print("your sum is : ",c)

division(10,2)
division(2,10)
