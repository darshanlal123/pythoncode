# Program to Reverse Internal Content of each Word 
# Input: Durga Software Solutions
# Output: agruD erawtfoS snoituloS

input_string= 'Durga Software Solutions'
splited_string =input_string.split(' ') # create a list of splited string['durga','softeare', 'solutions']
lenth_of_string=len(splited_string)-1
i=0
reversed_string=[] #--> ['agruD', 'erawtfoS', 'snoituloS']
while i<=lenth_of_string:
    reversed_string.append(splited_string[i][::-1])
    i=i+1
final_string=' '.join(reversed_string)
print(final_string)


