# Write a Program to perform the following Task? Input: 'one two three four five six seven' Output: 'one owt three ruof five xis seven'

s='one two three four five six seven'
list1=s.split()
list2 =[]
i=0
while i<len(list1):
    if i%2==0:
        list2.append(list1[i])
    else:
        list2.append(list1[i][::-1])
    i=i+1
output=" ".join(list2)
print(output)