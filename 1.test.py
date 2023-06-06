'''polymorphism - 
1- Duck typing

2- overloading-
    a-operator overloading
    b-methode overloading
    c-constructor overloading

3- Overriding
    a-methode overriding
    b-constructor overriding

'''

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        # st.add(score)
    sec = sorted(set([row[1] for row in records]))[1]
    # print(sec)
    name = [i[0] for i in records if i[1] == sec]
    print(*sorted(name), sep = '\n')