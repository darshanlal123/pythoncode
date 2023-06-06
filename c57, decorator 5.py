def decor_division(func):
    def solution(a,b):
        if a<b:
            c=b/a   
            return c
        else:
            return func(a,b)
    return solution

@decor_division
def division(a,b):
    d=a/b
    return d

a=division(5,10)
b=division(10,2)

print(a)
print(b)
