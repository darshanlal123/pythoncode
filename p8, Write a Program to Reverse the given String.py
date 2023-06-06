# Write a Program to Reverse the given String

# first method
string1 = "this is darshan lal"
# revers_string = string1[::-1]
# print(revers_string)


# second method
# s="".join(reversed(string1))
# print(s)


# third method
lenth_of_string = len(string1)-1
target=''
while lenth_of_string>=0:
    target =target+string1[lenth_of_string]
    lenth_of_string=lenth_of_string-1
print(target)
