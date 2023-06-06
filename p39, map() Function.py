# map() Function:  For every element present in the given sequence,apply some functionality and generate new element with the required modification. For this requirement we should go for map() function.

# map(function, sequence)

# For every element present in the list perform double and generate new list of doubles.

list1 = [1,2,3,4,5,6,7,8,9]
def double(num):
    d = 2*num
    return d
a= list(map(double,list1))
print(a)