#Using the approach that second line should always be greater than first line
start = int(input())
stop = int(input())
count = 0
lst = []
for i in range(start, stop+1):
    for x in range(start,stop + 1):
        if x >= i:
            for z in range(start,stop + 1):
                if ((i**2) + (x**2)) == (z**2):
                    print(i,x,z)