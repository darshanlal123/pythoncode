# n = int(input())
sum=0
student_marks = {'darshan': [53.0, 58.0, 89.0], 'ravi': [70.0, 88.0, 68.0], 'kavi': [70.0, 55.0, 66.0]}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
query_name=input("enter name : ")
result=student_marks[query_name]
number_subject=len(result)
for x in result:
    sum = sum+x
average= sum/number_subject
print(result)
print(number_subject)
print("average : {:.2f}".format(average))