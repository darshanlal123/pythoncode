# remove() Function: We can use this function to remove specified item from the list.If the item present multiple times then only first occurrence will be removed.

# If the specified item not present in list then we will get ValueError
# Hence before using remove() method first we have to check specified element present in the list or not by using in operator.

n=[10,20,10,30] 
n.remove(10) 
print(n)