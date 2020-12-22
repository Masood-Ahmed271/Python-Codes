lstprime = []
count = 1
num = int(input())
if num > 2:
    lstprime = [2]
else:
    lstprime = []
for i in range(3,num):
    counter = 0
    for x in range(2,i):
        if (i % x == 0):
            counter = 1
            break
    if counter == 0:
        lstprime.insert(count,i)
        count += 1
final_lst = []
new_count = 0
for j in lstprime:
    if (num % j != 0):
        final_lst.insert(new_count,j)
        new_count +=1
print(len(final_lst))