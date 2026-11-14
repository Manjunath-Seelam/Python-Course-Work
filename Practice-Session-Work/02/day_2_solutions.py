"""
DAY 1 TO DAY 3
PYTHON ASSIGNMENT SOLUTIONS

This file contains simple solutions for all 30 questions.
Each question is kept as a separate section.
"""
"""
DAY 2 - OPERATORS IN PYTHON

1. Mathematical Operations Calculator
Write a Python program to accept two numbers and perform addition,
subtraction, multiplication, division, floor division, modulus and
exponentiation. Display all the results.
"""

number_1 = float(input("Enter first number: "))
number_2 = float(input("Enter second number: "))

print("Addition:", number_1 + number_2)
print("Subtraction:", number_1 - number_2)
print("Multiplication:", number_1 * number_2)

if number_2 != 0:
    print("Division:", number_1 / number_2)
    print("Floor Division:", number_1 // number_2)
    print("Modulus:", number_1 % number_2)
else:
    print("Division, floor division and modulus are not possible with zero.")

print("Exponentiation:", number_1 ** number_2)


"""
1. Number Comparison Program
Write a Python program to accept two numbers and compare them.
Display whether the first number is greater than, less than or equal
to the second number.
"""

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

print("First number is greater:", first_number > second_number)
print("First number is less:", first_number < second_number)
print("Both numbers are equal:", first_number == second_number)
print("Numbers are not equal:", first_number != second_number)
print("First number is greater than or equal:", first_number >= second_number)
print("First number is less than or equal:", first_number <= second_number)


"""
3. Assignment Operators Demonstration
Write a Python program to initialize a variable with a value of 50
and demonstrate all assignment operators. Display the value after
every operation.
"""

assignment_number = 50
print("Initial value:", assignment_number)

assignment_number += 10
print("After += 10:", assignment_number)

assignment_number -= 5
print("After -= 5:", assignment_number)

assignment_number *= 2
print("After *= 1:", assignment_number)

assignment_number /= 5
print("After /= 5:", assignment_number)

assignment_number //= 2
print("After //= 1:", assignment_number)

assignment_number %= 3
print("After %= 3:", assignment_number)

assignment_number **= 2
print("After **= 1:", assignment_number)


"""
4. Student Eligibility Checker
Write a Python program to check whether a student is eligible for a
scholarship. Age must be between 18 and 25, percentage must be at least
85 and family annual income must be less than 300000.
"""

student_age = int(input("Enter student age: "))
student_percentage = float(input("Enter student percentage: "))
family_income = float(input("Enter family annual income: "))

if student_age >= 18 and student_age <= 25:
    age_condition = True
else:
    age_condition = False

if student_percentage >= 85:
    percentage_condition = True
else:
    percentage_condition = False

if family_income < 300000:
    income_condition = True
else:
    income_condition = False

if age_condition and percentage_condition and income_condition:
    print("Student is eligible for scholarship")
else:
    print("Student is not eligible for scholarship")


"""
5. Membership Operators - Search Program
Accept a list of five programming languages from the user.
Ask the user for a language to search for and use membership operators.
Also demonstrate membership operators with strings.
"""

languages = []
languages.append(input("Enter programming language 1: "))
languages.append(input("Enter programming language 1: "))
languages.append(input("Enter programming language 3: "))
languages.append(input("Enter programming language 4: "))
languages.append(input("Enter programming language 5: "))

search_language = input("Enter a language to search: ")
if search_language in languages:
    print(search_language, "is available in the list")
else:
    print(search_language, "is not available in the list")

word = "Python"
print("Py" in word)
print("Java" not in word)


"""
6. Identity Operators Demonstration
Create two different lists containing the same elements.
Compare them using equality and identity operators. Then assign one list
to another variable and repeat the comparison.
"""

list_1 = ["Python", "Java", "C"]
list_2 = ["Python", "Java", "C"]

print("list_1 == list_2:", list_1 == list_2)
print("list_1 is list_2:", list_1 is list_2)
print("ID of list_1:", id(list_1))
print("ID of list_2:", id(list_2))

list_3 = list_1
print("list_1 == list_3:", list_1 == list_3)
print("list_1 is list_3:", list_1 is list_3)
print("Equal means values are the same.")
print("Identity means both variables refer to the same object.")


"""
7. Job Eligibility Verification System
Accept candidate age, educational qualification, percentage, years of
experience and technical skills availability.
The candidate must be at least 21, have a degree, have at least 60 marks,
and have either two years of experience or the required technical skills.
"""

candidate_age = int(input("Enter candidate age: "))
qualification = input("Enter educational qualification: ").lower()
candidate_percentage = float(input("Enter percentage: "))
experience = int(input("Enter years of experience: "))
technical_skills = input("Does the candidate have technical skills? yes/no: ").lower()

has_degree = qualification == "degree"
has_experience = experience >= 2
has_skills = technical_skills == "yes"

if (
    candidate_age >= 21
    and has_degree
    and candidate_percentage >= 60
    and (has_experience or has_skills)
):
    print("Candidate is eligible for the job")
else:
    print("Candidate is not eligible for the job")


"""
8. Bitwise Operations Calculator
Accept two integer values and perform bitwise AND, OR, XOR, NOT,
left shift and right shift operations.
"""

bit_number_1 = int(input("Enter first integer: "))
bit_number_2 = int(input("Enter second integer: "))

print("Binary of first number:", bin(bit_number_1))
print("Binary of second number:", bin(bit_number_2))
print("Bitwise AND:", bit_number_1 & bit_number_2)
print("Bitwise OR:", bit_number_1 | bit_number_2)
print("Bitwise XOR:", bit_number_1 ^ bit_number_2)
print("Bitwise NOT of first number:", ~bit_number_1)
print("Left shift of first number:", bit_number_1 << 1)
print("Right shift of first number:", bit_number_1 >> 1)


"""
9. Even or Odd Without Modulus
Check whether an integer is even or odd without using the modulus
operator. Also check whether the number is positive, negative or zero.
"""

check_number = int(input("Enter an integer: "))

if check_number & 1:
    print("The number is odd")
else:
    print("The number is even")

if check_number > 0:
    print("The number is positive")
if check_number < 0:
    print("The number is negative")
if check_number == 0:
    print("The number is zero")


"""
10. ATM Transaction Validation System
Accept account balance, withdrawal amount, daily withdrawal limit and
minimum transaction amount. Validate the withdrawal and display the
remaining balance or the rejection reason.
"""

account_balance = float(input("Enter account balance: "))
withdrawal_amount = float(input("Enter withdrawal amount: "))
daily_limit = float(input("Enter daily withdrawal limit: "))
minimum_amount = float(input("Enter minimum transaction amount: "))

if withdrawal_amount <= 0:
    print("Transaction rejected: amount must be greater than zero")
elif withdrawal_amount < minimum_amount:
    print("Transaction rejected: amount is less than minimum amount")
elif withdrawal_amount > account_balance:
    print("Transaction rejected: insufficient balance")
elif withdrawal_amount > daily_limit:
    print("Transaction rejected: daily withdrawal limit exceeded")
elif withdrawal_amount % 100 != 0:
    print("Transaction rejected: amount must be a multiple of 100")
else:
    account_balance = account_balance - withdrawal_amount
    print("Transaction successful")
    print("Remaining balance:", account_balance)
