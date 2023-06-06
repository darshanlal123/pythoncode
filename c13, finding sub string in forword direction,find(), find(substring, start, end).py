# finding sub string in forword direction

# find()

# Returns index of first occurrence of the given substring. If it is not available then we will get -1.

input_string= input("please enter your string : ")
sub_string= input("please enter your string : ")
sub_string1 = input_string.find(sub_string)
if sub_string1 == -1:
    print("sub string is not found..")
else:
    print("{} is on index {}".format(sub_string, sub_string1))

# By default find() method can search total string. We can also specify the boundaries to search.
# s.find(substring,bEgin,end)

sub_string= input("please enter your string to find in range : ")
range1,range2 = [int(x) for x in input("plfease enter the range : ").split(",")]
sub_string1 = input_string.find(sub_string,range1,range2)
if sub_string1 == -1:
    print("sub string is not found between range..")
else:
    print("{} is on index {}".format(sub_string, sub_string1))


""" Please make this program using function and (abstract function so that we can get diffrent output for difrent case...)"""