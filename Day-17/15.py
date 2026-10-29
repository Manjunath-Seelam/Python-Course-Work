"""
CONDITIONAL STATEMENTS
If Statement
15. Write a Python program that checks whether it is raining and displays “Extra Rain Charges Applied” if the condition is True.
    Use an if statement only.
"""

data=input("Enter the status is raining or not raining: ").lower()
if data=="raining":
    print(f"Extra rain charges applied")
if data == "not raining":
    print(f"No extra charges")
