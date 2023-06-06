# Write a Program for the following Requirement 
# Input: a4b3c2 
# Output: aaaabbbcc

s= 'a4b3c2'
output=''
for x in s:
    if x.isalpha():
        output = output+x
        previous=x
    else:
        output= output+previous*(int(x)-1)
print(output)