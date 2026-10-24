"""
Basic Level Question - elif
8.Student Grade Calculator:
If average marks > 90 → “Excellent”
Between 70-90 → “Good”
Below 70 → “Needs Improvement”
"""

tel=int(input("Enters marks in Telugu: "))
hin=int(input("Enters marks in Hindi: "))
eng=int(input("Enters marks in English: "))
mat=int(input("Enters marks in Maths: "))
sci=int(input("Enters marks in Science: "))
soc=int(input("Enters marks in Social: "))
Total = tel+hin+eng+mat+sci+soc
print("Total marks: ", Total)
average= Total/6
print ("Average of 6 subjects: ", average)

if average>90:
    print("Excellent")
elif average>=70 and average<90:
    print("Good")
else:
    print("Needs Improvement")

