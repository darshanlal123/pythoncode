# write a program to find out biggest of three number

a,b,c = [int(x) for x in input("Please enter three number : ").split()]
if a>b and a>c:
    print("a is biggest number...")
elif b>c:
    print("b is biggest number...")
else:
    print("c is biggest number...")
