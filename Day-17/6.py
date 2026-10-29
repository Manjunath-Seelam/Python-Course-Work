"""
CONDITIONAL STATEMENTS
If Statement
6. Write a Python program that checks if a number is divisible by both 2 and 3.
Divisible by → Can I divide it without a remainder?
"""

num=int(input("Enter a number: "))
if num%2==0 and num%3==0:
    print(f"The number {num} is a divisible of both 2 and 3")
if num%2!=0 and num%3!=0:
    print(f"The number {num} is not a divisible of both 2 and 3")