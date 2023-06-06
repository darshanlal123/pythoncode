# else in loop 

# inside loop exicution, if break statement is not exicuted , then only the else part will be exicuted

# Else meanse loop without break


cart=[10,20,65,60,70]
for item in cart:
    if item>500:
        print("to place this order insurence must be required")
        break
    print(item)
else:
    print("congrats... all item processed successfully")