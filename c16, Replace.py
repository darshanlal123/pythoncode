# Replacing a String with another String:

#  s.replace(oldstring, newstring)
input_string= ("A cow is a domestic animal. Cows are one of the most innocent animals who are very harmless. People keep cows at their homes for various benefits. Cows are four-footed and have a large body. It has two horns, two eyes plus two ears and one nose and a mouth.")
print("this is string --->" ,input_string)
string =input ("please enter the substring you want to replace : ")
if string in input_string:
    subtring =input("with what you want to replace : ")
    new_string =input_string.replace(string,subtring)
    print(" your new string is -->",new_string)
else:
    print("enterd subtring is not fiund in the string THANKS! ")
