"""
CONDITIONAL STATEMENTS
If Statement
13. Write a Python program to display “Best Seller” if product sales are greater than 1000.
"""
sales=int(input("Enter sales amount: "))
if sales>=1000:
    print(f"The Best Seller")
if sales<1000:
    print(f"The sales are less than 1000")