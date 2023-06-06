# Removing Spaces from the String:

# 1) rstrip()--> To remove spaces at right hand side 
# 2) lstrip()--> To remove spaces at left hand side 
# 3) strip()-->  To remove spaces both sides

city = input("please enter the city name : ").lower()
scity = city.strip()
if scity=='hydrabad':
    print("hellow haidrabadi.... Adab")
elif scity=='chennai':
    print("hellow Madrasi.... Vannakam")
elif scity=='banglore':
    print("hellow Kannadiga.... Subhodya")
else:
    print("your enterd city is invalid.")