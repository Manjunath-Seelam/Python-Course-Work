"""
Basic Level Question - elif
2. Take an input number and check whether it is a three-digit number.(if-else)
Input:
34
Output:
Not a three digit number
Input:
453
Output:
Its three digit number
Input: -898
Output: Its three digit number
"""

data = int(input("Enter a number: "))
if  data>=100:
    print(" The number is three-digit number")
elif data<0 and data<-99:
    print(" The number is three-digit number")
else:
    print("Not a three digit number")