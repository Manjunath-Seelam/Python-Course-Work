"""
Basic Level Questions - elif
7.Bus Fare:
Age < 5: "Free"
Age 5 to 18: "Half Ticket"
Age > 18: "Full Ticket"
"""
age=int(input("Enter the age: "))
if age<5:
    print("The fare is Free")
elif age>=5 and age<=18:
    print("The fare is Half Ticket")
else:
    print("The fare is Full Ticket")