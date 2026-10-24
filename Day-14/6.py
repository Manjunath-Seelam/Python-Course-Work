"""
Basic Level Questions - elif
6.Input the number of sides and determine the type of polygon:
3 → Triangle
4 → Quadrilateral
5 → Pentagon
Else → Unknown shape
"""

data=int(input("Enter a number: "))
if data==3:
    print("Triangle")
elif data==4:
    print("Quadrilateral")
elif data==5:
    print("Pentagon")
else:
    print("Unknown shape")
