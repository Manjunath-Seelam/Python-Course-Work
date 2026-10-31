"""
CONDITIONAL STATEMENTS
If Statement
4. Write a Python program that checks if a number is a multiple of both 3 and 5.
Multiple of → Can I obtain it by multiplying the given number by an integer?
"""

num=int(input("Enter a number: "))
if num%3==0 and num%5==0:
    print(f"The number {num} is a multiple of both 3 and 5")
if num%3!=0 and num%5!=0:
    print(f"The number {num} is not a multiple of both 3 and 5")