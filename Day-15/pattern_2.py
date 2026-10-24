"""
*****
*****
*****
*****
*****
"""

n=5
print ("FIRST ROW")# first row
for i in range (n):
    for j in range (n):
        if i==0:
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()
print ()
print ("LAST ROW")# last row
for i in range (n):
    for j in range (n):
        if i==n-1:
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()
print()
print ("FIRST COLUMN") #First Column
for i in range (n):
    for j in range (n):
        if j==0:
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()
print()
print("LAST COLUMN") #Last Column
for i in range (n):
    for j in range (n):
        if j==n-1:
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()
print()
print ("RIGHT DIAGONAL") #Right Diagonal
for i in range (n):
    for j in range (n):
        if i==j:
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()
print()
print ("LEFT DIAGONAL") #Left Diagonal
for i in range (n):
    for j in range (n):
        if i+j==n-1:
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()
print()
print ("MIDDLE ROW") # Middle Row
for i in range (n):
    for j in range (n):
        if i==n//2:
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()
print("MIDDLE COLUMN")
for i in range (n):
    for j in range (n):
        if j==n//2:
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()
print()
print("END")