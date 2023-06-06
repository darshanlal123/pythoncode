
# filter() Function: We can use filter() function to filter values from the given sequence based on some condition.

# filter(function,sequence)

#  Where Function Argument is responsible to perform conditional check Sequence can be List OR Tuple OR String.

# Program to filter only Even Numbers from the List by using filter() Function
def is_even(num):
    if num % 2==0:
        return True
    else:
        return False
sec = range(1,100)
l1=list(filter(is_even,sec))
print(l1)