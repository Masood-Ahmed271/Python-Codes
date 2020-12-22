ISBN = (input('ISBN: '))
x = int(ISBN[0])
number_1 = x * 1
x = int(ISBN[1])
number_2 = x * 3
x = int(ISBN[2])
number_3 = x * 1
x = int(ISBN[3])
number_4 = x * 3
x = int(ISBN[4])
number_5 = x * 1
x = int(ISBN[5])
number_6 = x * 3
x = int(ISBN[6])
number_7 = x * 1
x = int(ISBN[7])
number_8 = x * 3
x = int(ISBN[8])
number_9 = x * 1
x = int(ISBN[9])
number_10 = x * 3
x = int(ISBN[10])
number_11 = x * 1
x = int(ISBN[11])
number_12 = x * 3
Sum = number_1 + number_2 + number_3 + number_4 + number_5 +number_6 + number_7 + number_8 + number_9 + number_10 + number_11 + number_12
left_over = (Sum % 10)
if left_over == 0:
    check_digit = 0
    if check_digit == int(ISBN[12]):
        print('Valid')
    else: 
        print('Invalid')
else:
    check_digit = 10 - left_over
    if check_digit == int(ISBN[12]):
        print('Valid')
    else:
        print('Invalid')