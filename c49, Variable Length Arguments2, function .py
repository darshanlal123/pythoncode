# Variable Length Arguments:

# We can mix variable length arguments with positional arguments.

def sum(n1,*n):
    print("positional argument is : ", n1)
    print("variable argument is : ", n)
sum(10,20,30,40,50)
# After variable length argument,if we are taking any other arguments then we should provide values as keyword arguments.
