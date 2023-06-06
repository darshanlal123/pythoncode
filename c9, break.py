# break 

# we can use break statement inside loop to break loop exicution based on some condition

for i in range(10):
    if i ==7:
        print("processing is enough.. please break")
        break
    print(i)

print("example 2 ...\n")

cart=[10,20,600,60,70]
for item in cart:
    if item>500:
        print("to place this order insurence must be required")
        break
    print(item)