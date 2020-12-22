initialize = int(input())
#checking for prime numbers between (1,n+1)
possibilities = [1]
count = 1
for i in range(2, initialize +1):
    checker = 0
    for prime in range (2,i):
        if i % prime == 0:
            checker = 1
            break
    if checker == 0:
        possibilities.insert(count,i)
        count += 1
#print(possibilities) 
total = 0
lst = []
for j in range(1,initialize +1):
    total = 0
    for h in possibilities:
        if j >= h:
            if j - h == 0:
                total += 1
            else:
                total += lst[j - h - 1]
    lst.append(total)
print(total)
