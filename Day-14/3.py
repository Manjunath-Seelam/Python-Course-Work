"""
Basic Level Question - elif
3.Take temperature input and:
If above 30: print “It’s hot”
If between 15 and 30: print “Pleasant”
If below 15: print “Cold”
"""

temperature=int(input("Enter the temperature in Celsius: "))
if temperature > 30:
    print("It's HOT")
elif temperature >= 15 and temperature <=30:
    print("It's Pleasant")
else:
    print("It's Cold")