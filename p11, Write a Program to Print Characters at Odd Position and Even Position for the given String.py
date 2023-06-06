# Write a Program to Print Characters at Odd Position and Even Position for the given String?

#first way
s="Hi this is darshan lal how are you?"
# print("charector at even position : ", s[0::2])
# print("charector at ODD position :", s[1::2])

# second way
# even_charector =""
# odd_charector =""
# for i in range(len(s)):
#     if i%2==0:
#         even_charector=even_charector+s[i]
#     else:
#         odd_charector=odd_charector+s[i]
# print("charector at odd position : ", even_charector)
# print("charector at even position : ",odd_charector)


# Third way
i=0
print("charector at even position")
while i<len(s):
    print(s[i],end=',')
    i=i+2
print()
print("charector at odd position")    
i=1
while i<len(s):
    print(s[i],end=',')
    i=i+2


    

