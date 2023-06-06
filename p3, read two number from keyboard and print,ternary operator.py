# read two number from keyboard and print minimum value

val1 = int(input("please enter first value : "))
val2 = int(input("please enter second value : "))
minimum = val1 if val1<val2 else val2
print(minimum)
