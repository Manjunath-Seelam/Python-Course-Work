"""
Basic Level Question
7.    Take a number input and print whether it is divisible by 3 and 5.
"""

data = int(input("Enter a number: "))
if data % 3 == 0 and data % 5 == 0:
    print("The number ",data," is divisible by both 3 and 5.")
else:
    print("The number ",data," is not divisible by both 3 and 5.")