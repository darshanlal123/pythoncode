# pop(): d.pop(key) It removes the entry associated with the specified key and returns the corresponding value.
# If the specified key is not available then we will get KeyError.


d= {100:'darshan lal',
    101:'harsh lal',
    102:'jaya lal',
    103:'Abhishek',
    104:'di'}
while True:
    key = int(input("enter the key : "))
    if key in d:
        print("removed value : ",d.pop(key))
        print("other key value")
        for k,v in d.items():
            print(k, "==", v)
    else:
        print("key is not found ")
