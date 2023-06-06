# program for minimum of three numbers

val1 = int(input("please enter first value : "))
val2 = int(input("please enter second value : "))
val3 = int(input("please enter third value : "))
minimum = val1 if val1<val2 and val2<val3 else val2 if val2<val3 else val3
print(minimum)
