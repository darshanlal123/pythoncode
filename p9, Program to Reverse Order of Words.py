# Program to Reverse Order of Words

# Input: Learning Python is very Easy
# Output: Easy Very is Python Learning

string ="Learning Python is very Easy"
list1=string.split(" ")
rstring=list1[::-1]
fstring=' '.join(rstring)
print(fstring)