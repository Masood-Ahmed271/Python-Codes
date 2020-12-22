num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
total = num_1 + num_2 + num_3
mean = total/3
product = num_1*num_2*num_3
if num_1 <= num_2 and num_1 <= num_3:
    smallest = num_1
elif num_2 <= num_1  and num_2 <= num_3:
    smallest = num_2
else:
    smallest = num_3
if num_1 >= num_2 and num_1 >= num_3:
    largest = num_1
elif num_2 >= num_1  and num_2 >= num_3:
    largest = num_2
else:
    largest = num_3
if num_1 <= num_2 <= num_3 or num_3 <= num_2 <= num_1:
    median = num_2
elif num_2 <= num_1 <= num_3 or num_3 <= num_1 <= num_2:
    median = num_1
else :
    median = num_3
print('sum:',total)
print('mean:', "{:.1f}".format(mean) )
#print('mean:', str(mean)[0:3])
print('median:',median)
print('product:', product)
print('smallest:', smallest)
print('largest:', largest)