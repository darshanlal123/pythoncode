# To add all elements to list upto 100 which are divisible by 10

a =range(101)
l=[]
for x in a:
    if x%10==0:
        l.append(x)
print(l)
    