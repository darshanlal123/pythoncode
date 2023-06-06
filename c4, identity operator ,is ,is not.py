# identity operator

# is, is not 

# is and is not -----> address comparison
# while == ----------> is content comparison

# x1 is x2 return true whenn x1 and x2 are pointing the same onject 
# x1 is not x2 return true whenn x1 and x2 are not 0pointing the same onject 

a=2
b=2
print(id(a))
print(id(b))
print(a is b)
print(a is not b)


print("second example.....\n")
list1 =["one","two","three"]
list2 =["one","two","three"]
print(id(list1))
print(id(list2))
print(list1 is list2) # address comparison
print(list1 == list2) # content comparison