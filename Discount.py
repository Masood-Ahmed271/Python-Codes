name = str(input('Name: '))
price = float(input('Price: '))
"""
y = str('H')
z = str('e')
x = str('r')
print('Original price was', price)
#if (price >=10 and name[] >= 5):
if (name[0] == y):
        discount1= price - 10
        saved = price - discount1
        print('Discount price is', discount1)
        print('You saved', saved)
if (name[1] == z and price >= 1000):
        discount2 = price - 100
        saved = price - discount2
        print('Discount price is', discount2)
        print('You saved', saved)
if (name[2] == x and price >= 5000):
        discount3 = price - 500
        saved = price - discount3
        print('Discount price is', discount3)
        print('You saved', saved)
if (name[2] == x and (price >= 500 and price < 5000)):
        discount4 = price - 300
        saved = price - discount4
        print('Discount price is', discount4)
        print('You saved', saved)
else:
        print('Discount price is', price)
        saved= price - price
        print('You saved', saved)
        """
discount = 0        
if name[0] == 'H':
        discount += 10
if name[1] == 'e' and price >=1000:
        discount += 100 
if name[2] == 'r' and price >=5000:
        discount +=500
if name[2] == 'r' and (price >= 500 and price <5000):
        discount += 300
new_price = price - discount
print('Original price was', price)
print('Discount price is', new_price)
print('You saved', price - new_price)