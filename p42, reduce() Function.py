# reduce() Function: 
# reduce() function reduces sequence of elements into a single element by applying the specified function. 

# reduce(function,sequence) 

# reduce() function present in functools module and hence we should write import statement.

from functools import*
list1 = [1,2,3,4,5,6,7,8,9]
result = reduce(lambda x,y:x+y, list1)
print("sum of all list elements : ",result)
result2 = reduce(lambda x,y:x*y, list1)
print("multiplication of all list elements : ",result2)