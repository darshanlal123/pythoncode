# map() Function3:  For every element present in the given sequence,apply some functionality and generate new element with the required modification. For this requirement we should go for map() function.

# map(function, sequence)

# We can apply map() function on multiple lists also.But make sure all list should have same length.
# Syntax: map(lambda x,y:x*y,l1,l2)) x is from l1 and y is from l2 
l1=[1,2,3,4]
l2=[2,3,4,5]
l3=list(map(lambda x,y:x*y,l1,l2))
print(l3)