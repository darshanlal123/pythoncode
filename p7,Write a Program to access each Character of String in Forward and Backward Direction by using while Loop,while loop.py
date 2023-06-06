# Write a Program to access each Character of String in Forward and Backward Direction by using while Loop?
s = input("please enter your string : ")
i=0
while i<len(s):
    print("+ve index {}, -ve index {} and the charector is {}".format(i,i-len(s),s[i]))
    i=i+1
