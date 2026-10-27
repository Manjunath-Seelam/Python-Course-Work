"""
Basic Level Question - Nested-if/nested if-else conditional statement:
Q1. Write a Python program to check whether a given number is a multiple of 5.
 If the number is a multiple of 5, then check whether it is also even or odd and print the appropriate message using nested if.
"""

num=int(input("Enter a number: "))
print()
if num%5==0:
    if num%2==0:
        print("Input number",num,"is even and is divisible by 5")
    else:
        print("Input number",num,"is odd and is divisible by 5")
else:
    print("Input number",num,"is not divisible by 5")