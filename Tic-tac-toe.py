size = int(input('Size--> '))
board = {}
keys = list(range(0, size**2))
values = list(range(0,size**2))
for i in range(0,size**2):
    board[keys[i]] = values[i]
align = len(str(size**2))
flag = False  

def printboard(): 
    for j in range(0,size**2,size):
        whitespace = 1
        for x in range(j,j+size):
            if whitespace < size:
                print(f'{board[x]:>2}', end = ' ')
                whitespace += 1
            else:
                print(f'{board[x]:>2}', end = '')
                print()

def checkwinner():
    global flag
    for a in range(0,size**2,size):
        row1 = 0
        row2 = 0
        for b in range(a,a+size):
            if board[b] == 'X':
                row1 += 1
                if row1 == size:
                    flag = True
            elif board[b] == 'O':
                row2 += 1
                if row2 == size:
                    flag = True
    for c in range(0,size):
        column1 = 0
        column2 = 0
        for d in range(c,((size * (size - 1)) + c + 1),size):
            if board[d] == 'X':
                column1 +=1
                if column1 == size:
                    flag = True
            elif board[d] == 'O':
                column2 += 1
                if column2 == size:
                    flag = True
    rdiagonal1 = 0
    rdiagonal2 = 0
    for e in range(0,(((size - 1)*(size + 1))+1), size+1):
        if board[e] == 'X':
            rdiagonal1 += 1
            if rdiagonal1 == size:
                flag = True
        elif board[e] == 'O':
            rdiagonal2 += 1
            if rdiagonal2 == size:
                flag = True
    ldiagonal1 = 0
    ldiagonal2 = 0
    for f in range((size - 1),(((size-1)*size)+1),(size - 1)):
        if board[f] == 'X':
            ldiagonal1 +=1
            if ldiagonal1 == size:
                flag = True
        elif board[f] == 'O':
            ldiagonal2 += 1
            if ldiagonal2 == size:
                flag = True
    return flag

def no_winner():
    count = 0
    for g in range(0,size**2):
        if board[g] == 'X' or board[g] == 'O':
            count+= 1
            if count == (size**2):
                return True

printboard() 
loop = True
while loop:
    if no_winner():
        print('Winner: None')
        break
    user1 = int(input('X--> '))
    if (board[user1] !=  'X') and (board[user1] != 'O'):
        board[user1] = 'X'
        printboard()
        if checkwinner():
            print('Winner: X')
            loop = False
            break
    if no_winner():
        print('Winner: None')
        break
    user2 = int(input('O--> '))
    if (board[user2] !=  'X') and (board[user2] != 'O'):
        board[user2] = 'O'
        printboard()
        if checkwinner():
            print('Winner: O')
            loop = False
            break
    if no_winner():
        print('Winner: None')
        break