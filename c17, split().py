# Splitting of Strings: 
# We can split the given string according to specified seperator by using split() method. 
# l = s.split(seperator) ---> saprator can be any thing like (sapce,",","-","*".....)
# The default seperator is space. The return type of split() method is List.

s= "durga soft solutions"
l=s.split()
# print(l)---> it split in list format

for x in l:
    print(x)