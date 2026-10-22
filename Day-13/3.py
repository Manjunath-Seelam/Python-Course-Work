"""
Basic Level Question - if, if-else
3.    Ask the user for their age. If the age is 18 or more, print “You are eligible to vote.”
"""

age=int(input("Enter your Age: "))
if age>=18:
    print(f"You are eligible to vote as your age is {age}")
else:
    print(f"You are not eligible to vote as your age is {age}")