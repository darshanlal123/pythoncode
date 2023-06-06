# fetching the data of dictionary3, d.get
# d.get(key,default value)

d= {100:'darshan lal',
    101:'harsh lal',
    102:'jaya lal',
    103:'Abhishek',
    104:'di'}
while True:
    key = int(input('enter the key : '))
    print(d.get(key, "key not found"))