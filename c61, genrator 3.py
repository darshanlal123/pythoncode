# To generate first n numbers

# first method

def genrator(num):
    value =1
    while value<=num:
        yield value
        value = value+1

for x in genrator(5):
    print(x) 



# 2nd method

genrator= (x for x in range(1,6))
print(type(genrator))
for x in genrator:
    print(x)
