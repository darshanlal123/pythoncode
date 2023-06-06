# Write a Program to Remove Duplicate Characters from the given Input String?
# Input: ABCDABBCDABBBCCCDDEEEF Output: ABCDEF

s= 'ABCDABBCDABBBCCCDDEEEF'
list1=[]
for x in s:
    if x not in list1:
        list1.append(x)
output="".join(list1)
print(output)
