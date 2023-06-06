# contineu 

# we can use contineu statement inside loop to skip the iteration and comtineu next iteration

for i in range(10):
    if i ==7:
        print("skiping nuber 7")
        continue
    print(i)

print("example 2 ...\n")

cart=[10,20,600,60,70]
for item in cart:
    if item>500:
        print("we can not process item : ", item)
        continue
    print(item)