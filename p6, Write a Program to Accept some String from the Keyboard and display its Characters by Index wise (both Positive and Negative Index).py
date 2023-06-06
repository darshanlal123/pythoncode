# Write a Program to Accept some String from the Keyboard and display its Characters by Index wise (both Positive and Negative Index)

s = input("enter your string : ")
# print(len(s))
for i in range(len(s)):
    print("+ve index = {}, -ve index{}, string is {} ".format(i,i-len(s),s[i]))