# fetching the data of dictionary1
d= {100:'darshan lal',
    101:'harsh lal',
    102:'jaya lal',
    103:'Abhishek',
    104:'di'}
while True:
    key = int(input('please enter the key : '))
    if key in d:
        print(d[key])
    else:
        print('key is not found in the dictionary thanks!')
