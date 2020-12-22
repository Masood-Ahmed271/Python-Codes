user = input('a b: ').split(' ')
intlst = []
for i in user:
    intlst.append(int(i))
Flag = False
while Flag == False:
    if (intlst[0]>0 and (intlst[1]>intlst[0] and intlst[1]>0)):
        Flag =  True
    else:
        user = input('a b: ').split(' ')
        intlst.clear()
        for i in user:
            intlst.append(int(i))
divisors = input('Divisors: ').split(' ')
divisorlst = []
for divisor in divisors:
    if int(divisor) not in divisorlst:
        divisorlst.append(int(divisor))
Flag = False
while Flag == False:
    count = 0
    for d in divisorlst:
        if (d>0 and d <= intlst[1]):
            count += 1
            if count == len(divisorlst):
                Flag =  True
        else:
            divisors = input('Divisors: ').split(' ')
            divisorlst.clear()
            for divisor in divisors:
                divisorlst.append(int(divisor))
divisorlst.sort()
print('M',end = ' ')
whitespace = 1
for j in divisorlst:
    if whitespace < (len(divisorlst)):
        print(j,end = ' ')
        whitespace += 1
    else:
        print(j, end = '')
        print()
for i in range(intlst[0],intlst[1]):
    print(i,end = ' ')
    whitespace = 1
    for h in divisorlst:
        if i%h == 0:
            if whitespace < len(divisorlst):
                print(1, end = ' ')
                whitespace += 1
            else:
                print(1, end = '')
                print()
        else:
            if whitespace < len(divisorlst):
                print(0, end = ' ')
                whitespace += 1
            else:
                print(0, end = '')
                print()