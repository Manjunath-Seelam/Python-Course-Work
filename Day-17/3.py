"""
CONDITIONAL STATEMENTS
If Statement
3. Write a Python program that determines if a number is positive, negative, or zero using only if statements and no elif or else.
"""

num=int(input("Enter a Number: "))
if num>0:
    print(f"The number {num} is Positive +ve")
if num==0:
    print(f"The number {num} is Zero")
if num<0:
    print(f"The number {num} is Negative -ve")