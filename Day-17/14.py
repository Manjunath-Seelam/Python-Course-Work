"""
CONDITIONAL STATEMENTS
If Statement
14. Write a Python program to check whether a user gets a verified badge:
    if the account is eligible for verification and the Meta Verified subscription is active, display “Verified Badge Granted”.
"""

name=str(input("Enter your name: "))
age=int(input("Enter you age: "))
subscription_status=input("Your Subscription Status is Active or Inactive: ").lower()

if len(name)>0 and  age>=18 and subscription_status=="active":
    print(f"Verified Badge Granted")
