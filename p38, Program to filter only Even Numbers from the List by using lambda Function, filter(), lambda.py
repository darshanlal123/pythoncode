# Program to filter only Even Numbers from the List by using lambda Function

l= range(1,100)
a = list(filter(lambda x:x%2==0,l))
print(a)
b = list(filter(lambda x:x%2!=0,l))
print(b)