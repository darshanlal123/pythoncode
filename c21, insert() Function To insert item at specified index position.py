# insert() Function: To insert item at specified index position

l=[10,20,30,40,50,60,70,80]
n=int(input("Please enter the value you wnat to insert : "))
i=int(input("Please enter the index at which you wnat to insert : "))
l.insert(i,n)
print(l)

# Note: If the specified index is greater than max index then element will be inserted at last position. If the specified index is smaller than min index then element will be inserted at first position.