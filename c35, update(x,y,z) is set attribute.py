# update(x,y,z): To add multiple items to the set.  Arguments are not individual elements and these are Iterable objects like List, Range etc.  All elements present in the given Iterable objects will be added to the set.

s={10,20,30} 
l=[40,50,60,10]
s.update(l,range(5))
print(s)