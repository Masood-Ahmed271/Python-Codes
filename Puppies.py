positionx, positiony = input('Position of Queenie: ').split()
Number_of_puppies = int(input('Number of puppies: '))
n = 1
Total_puppies = []
while n <= Number_of_puppies: 
    a, b= input(f'Position of Puppy {n}: ').split()
    if ((abs(int(a)- int(positionx)) + abs(int(b) - int(positiony))) > 10):
        x = (f'Puppy {n} and ')
        Total_puppies.append(x)
    n +=1
if len(Total_puppies) == 0:
    y = ('No puppies     ')
    Total_puppies.append(y)
print(''.join(Total_puppies)[:-4] + 'too far away')