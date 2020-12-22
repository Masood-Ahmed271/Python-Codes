users = int(input('Number of users: '))
n = 1
Final_puppies = []
while n <= users:
    position_userx,position_usery = input(f'Position of User {n}: '). split()
    number_puppies = input(f'Number of puppies for User {n}: ')
    i = 1
    puppies = []
    while i <= int(number_puppies):
        a,b = input(f'Position of Puppy {i}: ').split()
        if ((abs(int(a)- int(position_userx)) + abs(int(b) - int(position_usery))) > 10):
            x = (f'Puppy {i} (User {n}) and ')
            puppies.append(x)
            Final_puppies.append(str(''.join(puppies)))
            puppies.clear()
        i +=1
    n +=1
if len(Final_puppies) == 0:
    y = ('No puppies     ')
    Final_puppies.append(y)
print(''.join(Final_puppies)[:-4:] + 'too far away')