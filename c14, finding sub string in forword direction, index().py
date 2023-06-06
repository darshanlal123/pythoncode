# finding sub string in forword direction

# index - index() method is exactly same as find() method except that if the specified substring is not available then we will get ValueError.


input_string= input("Please enter your string : ")
sub_string = input("please enter your sub string : ")
try: 
    index1 = input_string.index(sub_string)
except ValueError:
    print("Sub string is not found ")
else:
    print("your sub string found on", index1)
