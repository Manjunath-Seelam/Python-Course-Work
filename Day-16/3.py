"""
Basic Level Question - Nested-if/nested if-else conditional statement:
Question for Nested if-else Statement
Q2. Write a Python program to check whether a number is a multiple of 5 or not.
 If it is not a multiple of 5, check whether the number is positive or negative and print the result using nested if-else.
"""

num=int(input("Enter a number: "))
if num%5!=0:
    if num>=0:
        print("The given number is not divisible by 5 and is positive")
    else:
        print("The given number is not divisible by 5 and is negative")
else:
    if num<0:
        print("The given number is divisible by 5 and is negative")
    else:
        print("the given number is divisible by 5 and is positive")
