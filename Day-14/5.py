"""
Basic Level Questions -elif
5. Take the user's marks and print:
A if 90 and above
B if 80 to 89
C if 70 to 79
D if 60 to 69
F if below 60
"""

marks=int(input("Enter your marks: "))
if marks>=90:
    print("A Grade")
elif marks>=80 and marks<=89:
    print("B Grade")
elif marks>=70 and marks<=79:
    print("C Grade")
elif marks>=60 and marks<=69:
    print("D Grade")
else:
    print("F Grade")
