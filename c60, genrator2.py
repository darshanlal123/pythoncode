# in genral word we can say that tupple coprihension is genrator

# genrator = (expression for item in sequence/itrable)

a=[1,2,3,4,5,6]
genrator = (x*x for x in a)
print(type(genrator))
for x in genrator:
    print(x)

# or

genrator = (x*x for x in range(1,7))
print(type(genrator))
for x in genrator:
    print(x)