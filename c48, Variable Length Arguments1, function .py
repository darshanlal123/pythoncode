# Variable Length Arguments:

# We can call this function by passing any number of arguments including zero number. 
# Internally all these values represented in the form of tuple.

def sum(*n):
    total =0
    for i in n:
        total =total+i
    print(" the sum of numbers is : ", total)

sum(25,30,52)