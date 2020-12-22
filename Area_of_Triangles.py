import math
print('**********************************************\n**** WELCOME TO AREA OF TRIANGLE ****\n**********************************************' )
#\n is used to change lines
choice = 0
while choice != 1:
    print("1. Exit")
    print("2. Area of Triangle 1")
    print("3. Area of Triangle 2")
    print("4. Area of Triangle 3")
    choice = int(input("Choice: "))
    if choice == 1:
        print("Bye Bye!")
    if choice == 2:
        base = int(input('Base: ')) 
        height = int(input('Height: ')) 
        Area = (height*base)/2
        print('The area is', "{}".format(Area)+ '.')
    if choice == 3:
        a,b,y = float(input('A: ')),float(input('B: ')),float(input('Gamma: '))
        x = math.sin(math.radians(y))
        A = (a*b*x)/2
        print('The area is',f'{A}'+'.')
    if choice == 4:
        a = float(input('A: '))
        b = float(input('B: '))
        c = float(input('C: '))
        s = (a + b + c)/2
        A = (s*(s-a)*(s -b)*(s-c))**0.5
        print('The area is', "% s" % A +".")