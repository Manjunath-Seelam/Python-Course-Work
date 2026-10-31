"""
CONDITIONAL STATEMENTS
If Statement
5. Write a Python program that determines if a given number is a perfect square.
"""
num = int(input("Enter a Number: "))
s=int(num**0.5)
print(s)
if s*s==num:
    print("PS")
else:
    print("NPS")
