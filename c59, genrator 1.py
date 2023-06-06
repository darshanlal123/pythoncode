# genrator 1
def countdown(num):
    print("count down satarted")
    while (num>0):
        # returinig values
        yield num
        num =num-1

g= countdown(10)
for x in g:
    print(x)