# pop() Function:  It removes and returns the last element of the list.  This is only function which manipulates list and returns some element.

# If the list is empty then pop() function raises IndexError
# n.pop(index)  To remove and return element present at specified index.

l =[10,20,30,40,50,60]

if len(l)>0:
    print(l.pop())
    print(l)
else:
    print("list is empty")
