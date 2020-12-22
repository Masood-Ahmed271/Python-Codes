integer_1 = input()
integer_2 = input()
integer_3 = input()
integer_4 = input()
if integer_1[0] == '-':
    reverse_1 = '-' + integer_1[:0:-1]
else:
    reverse_1 = integer_1[::-1]
if integer_2[0] == '-':
    reverse_2 = '-' + integer_2[:0:-1]
else:
    reverse_2 = integer_2[::-1]
if integer_3[0] == '-':
    reverse_3 = '-' + integer_3[:0:-1]
else:
    reverse_3 = integer_3[::-1]
if integer_4[0] == '-':
    reverse_4 = '-' + integer_4[:0:-1]
else:
    reverse_4 = integer_4[::-1]
nums = [int(reverse_1),int(reverse_2),int(reverse_3),int(reverse_4)]
smallest = nums[0]
for i in range (len(nums)):
    if nums[i] < smallest:
        smallest = nums[i]
print('smallest:', smallest)
largest = nums[0]
for a in range(len(nums)):
    if nums[a] > largest:
        largest = nums[a]
print('largest:', largest)