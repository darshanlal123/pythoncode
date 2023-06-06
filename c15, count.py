# We can find the number of occurrences of substring present in the given string by using count() method.

# 1) s.count(substring) --->It will search through out the string.
# 2) s.count(substring, bEgin, end) ---> It will search from bEgin index to end-1 index.

input_string= ("A cow is a domestic animal. Cows are one of the most innocent animals who are very harmless. People keep cows at their homes for various benefits. Cows are four-footed and have a large body. It has two horns, two eyes plus two ears and one nose and a mouth.")
while True:
    input_substring= input("Please enter you substring : ")
    print(input_substring, "is fout for", input_string.count(input_substring), "times")