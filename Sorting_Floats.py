lst = []
new_lst = []
final_lst = []
another = ""
give_value = input()
index = 0
while give_value != 'x':
    x = 0
    lst.insert(index,give_value)
    index +=1
    give_value = input()
flag = 0
for i in lst:
    count_1 = 0
    for a in i:
        if a == '.':
            new_lst.insert(count_1,'.')
            count_1 += 1
        elif a == '-':
            new_lst.insert(count_1,'-')
            count_1 += 1
        elif int(a)%2 != 0:
            new_lst.insert(count_1,'8')
            count_1 += 1
        else:
            new_lst.insert(count_1,a)
            count_1 += 1
    for i in new_lst:
        another += str(i)
        new_lst = []
    final_lst.insert(flag,another)
    flag += 1
    another = ""
for j in range(len(final_lst)):
    for h in range(j +1, len(final_lst)):
        if float(final_lst[j]) > float(final_lst[h]):
            final_lst[j],final_lst[h] = final_lst[h],final_lst[j]
for g in range(len(final_lst)):
    print(float(final_lst[g]))