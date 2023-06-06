# decorator chaining
def decor_mul_1(func):
    def inner1(a,b):
        x=func(a,b)
        return x*10
    return inner1

def decor_mul_2(func):
    def inner2(a,b):
        x=func(a,b)
        return x*10
    return inner2

@decor_mul_2
@decor_mul_1
def add(a,b):
    return a+b
print(add(5,5))
