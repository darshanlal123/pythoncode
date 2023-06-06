# List Comprehensions:

# list = [expression for item in list if condition]
s=[x*x for x in range(2,20)]
print(s)

y= [x for x in s if x %2==0]

print(y)