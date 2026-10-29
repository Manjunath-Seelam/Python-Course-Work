"""
CONDITIONAL STATEMENTS
If Statement
2. Write a Python program that checks if given string length is empty
"""

string=str(input("Enter the String: "))
if len(string)>0:
    print(f"The entered string is {string}")
if len(string)==0:
    print(f"The entered string is empty")
