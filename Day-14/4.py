"""
Basic Level Question - elif
4. Check if a number is +ve, -ve or neutral.
"""

data=int(input("Enter the number: "))
if data>0:
    print("Positive +ve")
elif data==0:
    print("Neutral")
else:
    print("Negative -ve")