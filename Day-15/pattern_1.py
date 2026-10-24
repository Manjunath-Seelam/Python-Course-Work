"""
TO print the below pattern
***
 **
   *
"""
r=3 # Given pattern is 3*3
for i in range (r,0,-1):
    for k in range (r-i):
        print (' ', end=' ')
    for j in range (i):
        print('*', end=' ')
    print(' ')

r=3
for i in range (1, r+1):
    for k in range (i-1):
        print (' ', end=' ')
    for j in range (r-i+1):
        print('*', end=' ')
    print(' ')