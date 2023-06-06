# Write a Program to perform the following Activity 
# Input: a4k3b2 
# Outpt: aeknbd

s = 'a4k3b2'
output=''
for x in s:
    if x.isalpha():
        output =output+x
        previous=x
    else:
        output = output+chr(ord(previous)+int(x))
print(output)