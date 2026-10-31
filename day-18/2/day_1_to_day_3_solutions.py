"""
DAY 1 TO DAY 3
PYTHON ASSIGNMENT SOLUTIONS

This file contains simple solutions for all 30 questions.
Each question is kept as a separate section.
"""


"""
DAY 1 - INTRODUCTION TO PYTHON AND PROGRAMMING FUNDAMENTALS

1. Student Information Display
Write a Python program to display your name, age, qualification,
college name and city using separate print statements.
"""

print("Name: Manjunath")
print("Age: 20")
print("Qualification: B.Tech")
print("College Name: ABC College")
print("City: Bengaluru")


"""
2. Student Marks Calculator
Write a Python program to calculate the total marks and average marks
of a student in five subjects. Display the student name, individual
subject marks, total marks and average marks.
"""

student_name = input("Enter student name: ")
subject_1 = int(input("Enter marks in subject 1: "))
subject_2 = int(input("Enter marks in subject 2: "))
subject_3 = int(input("Enter marks in subject 3: "))
subject_4 = int(input("Enter marks in subject 4: "))
subject_5 = int(input("Enter marks in subject 5: "))

total_marks = subject_1 + subject_2 + subject_3 + subject_4 + subject_5
average_marks = total_marks / 5

print("Student Name:", student_name)
print("Subject 1:", subject_1)
print("Subject 2:", subject_2)
print("Subject 3:", subject_3)
print("Subject 4:", subject_4)
print("Subject 5:", subject_5)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)


"""
3. Personal Profile Generator
Write a Python program to collect personal details from a user and
display them in a properly formatted profile.
"""

profile_name = input("Enter your name: ")
profile_age = input("Enter your age: ")
profile_qualification = input("Enter your qualification: ")
profile_college = input("Enter your college name: ")
profile_city = input("Enter your city: ")

print("\n----- Personal Profile -----")
print("Name: " + profile_name)
print("Age: " + profile_age)
print("Qualification: " + profile_qualification)
print("College: " + profile_college)
print("City: " + profile_city)


"""
4. Shopping Bill Generator
Write a Python program to generate a shopping bill for five products.
Accept the product names, quantities and prices from the user.
Calculate the individual product costs and display the final bill amount.
"""

product_1 = input("Enter product 1 name: ")
quantity_1 = int(input("Enter product 1 quantity: "))
price_1 = float(input("Enter product 1 price: "))

product_2 = input("Enter product 2 name: ")
quantity_2 = int(input("Enter product 2 quantity: "))
price_2 = float(input("Enter product 2 price: "))

product_3 = input("Enter product 3 name: ")
quantity_3 = int(input("Enter product 3 quantity: "))
price_3 = float(input("Enter product 3 price: "))

product_4 = input("Enter product 4 name: ")
quantity_4 = int(input("Enter product 4 quantity: "))
price_4 = float(input("Enter product 4 price: "))

product_5 = input("Enter product 5 name: ")
quantity_5 = int(input("Enter product 5 quantity: "))
price_5 = float(input("Enter product 5 price: "))

cost_1 = quantity_1 * price_1
cost_2 = quantity_2 * price_2
cost_3 = quantity_3 * price_3
cost_4 = quantity_4 * price_4
cost_5 = quantity_5 * price_5
final_amount = cost_1 + cost_2 + cost_3 + cost_4 + cost_5

print("\n----- Shopping Bill -----")
print(product_1, "-", cost_1)
print(product_2, "-", cost_2)
print(product_3, "-", cost_3)
print(product_4, "-", cost_4)
print(product_5, "-", cost_5)
print("Final Bill Amount:", final_amount)


"""
5. Employee Salary Calculator
Write a Python program to collect employee ID, name, department and
basic salary. Calculate HRA (20% of basic salary), DA (10% of basic
salary) and gross salary. Display the complete employee salary details.
"""

employee_id = input("Enter employee ID: ")
employee_name = input("Enter employee name: ")
department = input("Enter department: ")
basic_salary = float(input("Enter basic salary: "))

hra = basic_salary * 20 / 100
da = basic_salary * 10 / 100
gross_salary = basic_salary + hra + da

print("\n----- Employee Salary Details -----")
print("Employee ID:", employee_id)
print("Employee Name:", employee_name)
print("Department:", department)
print("Basic Salary:", basic_salary)
print("HRA:", hra)
print("DA:", da)
print("Gross Salary:", gross_salary)


"""
6. Procedural vs Object-Oriented Programming
Write two Python programs to calculate the area of a rectangle.
Program 1 uses a procedural programming approach.
Program 2 uses an object-oriented programming approach.
Compare both programs and explain how the code is organized.
"""

length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))


def calculate_area(length, width):
    return length * width


procedural_area = calculate_area(length, width)
print("Area using procedural programming:", procedural_area)


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


rectangle = Rectangle(length, width)
object_area = rectangle.calculate_area()
print("Area using object-oriented programming:", object_area)
print("Procedural programming uses functions.")
print("Object-oriented programming uses a class, object and method.")


"""
7. Banking Management System Using Procedural Programming
Develop a simple banking application using a procedural programming
approach. Display account holder details, deposit money, withdraw money,
check account balance and display transaction details.
"""

account_holder = input("Enter account holder name: ")
account_number = input("Enter account number: ")
balance = float(input("Enter opening balance: "))
transactions = []


def deposit_money(balance, amount):
    balance = balance + amount
    transactions.append("Deposited " + str(amount))
    return balance


def withdraw_money(balance, amount):
    if amount <= balance:
        balance = balance - amount
        transactions.append("Withdrawn " + str(amount))
    else:
        print("Insufficient balance")
    return balance


deposit_amount = float(input("Enter deposit amount: "))
balance = deposit_money(balance, deposit_amount)

withdraw_amount = float(input("Enter withdrawal amount: "))
balance = withdraw_money(balance, withdraw_amount)

print("\n----- Bank Details -----")
print("Account Holder:", account_holder)
print("Account Number:", account_number)
print("Account Balance:", balance)
print("Transactions:")
for transaction in transactions:
    print(transaction)


"""
8. Student Management System Using OOP
Design a student management application using classes and objects.
Store student ID, name, course and marks. Create methods to register a
student, display student details and calculate total and average marks.
"""


class Student:
    def __init__(self, student_id, name, course, marks):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.marks = marks

    def register_student(self):
        print("Student registered successfully")

    def display_details(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Marks:", self.marks)

    def calculate_total(self):
        return sum(self.marks)

    def calculate_average(self):
        return self.calculate_total() / len(self.marks)


student_id = input("Enter student ID: ")
student_name = input("Enter student name: ")
course = input("Enter course: ")
student_marks = []
student_marks.append(float(input("Enter mark 1: ")))
student_marks.append(float(input("Enter mark 2: ")))
student_marks.append(float(input("Enter mark 3: ")))

student = Student(student_id, student_name, course, student_marks)
student.register_student()
student.display_details()
print("Total Marks:", student.calculate_total())
print("Average Marks:", student.calculate_average())


"""
9. Employee Salary System - Procedural vs OOP
Create two separate Python programs to calculate employee salaries.
Program 1 uses procedural programming and Program 2 uses
object-oriented programming. Compare code organization and reusability.
"""

salary_name = input("Enter employee name: ")
salary_basic = float(input("Enter employee basic salary: "))


def calculate_salary(basic_salary):
    hra = basic_salary * 20 / 100
    da = basic_salary * 10 / 100
    return basic_salary + hra + da


procedural_salary = calculate_salary(salary_basic)
print("Salary using procedural programming:", procedural_salary)


class EmployeeSalary:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        hra = self.basic_salary * 20 / 100
        da = self.basic_salary * 10 / 100
        return self.basic_salary + hra + da


employee_salary = EmployeeSalary(salary_name, salary_basic)
object_salary = employee_salary.calculate_salary()
print("Salary using object-oriented programming:", object_salary)
print("Functions are used in the procedural program.")
print("Attributes and methods are used in the OOP program.")


"""
10. Employee Management Mini Application
Develop an employee management application using OOP.
Create an Employee class with employee ID, name, department and salary.
Store details, display information, calculate annual salary and update salary.
"""


class Employee:
    def __init__(self, employee_id, name, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary

    def display_information(self):
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Monthly Salary:", self.salary)

    def calculate_annual_salary(self):
        return self.salary * 12

    def update_salary(self, new_salary):
        self.salary = new_salary


employee = Employee(
    input("Enter employee ID: "),
    input("Enter employee name: "),
    input("Enter department: "),
    float(input("Enter salary: ")),
)

print("\n----- Employee Information -----")
employee.display_information()
print("Annual Salary:", employee.calculate_annual_salary())

updated_salary = float(input("Enter updated salary: "))
employee.update_salary(updated_salary)
print("\n----- Updated Employee Information -----")
employee.display_information()


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
2. Number Comparison Program
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
print("After *= 2:", assignment_number)

assignment_number /= 5
print("After /= 5:", assignment_number)

assignment_number //= 2
print("After //= 2:", assignment_number)

assignment_number %= 3
print("After %= 3:", assignment_number)

assignment_number **= 2
print("After **= 2:", assignment_number)


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
languages.append(input("Enter programming language 2: "))
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


"""
DAY 3 - STRINGS IN PYTHON

1. String Information Display
Accept a user's full name, city and college name. Display all details
separately and display the length of each string.
"""

full_name = input("Enter your full name: ")
city_name = input("Enter your city: ")
college_name = input("Enter your college name: ")

print("Full Name:", full_name)
print("Length of full name:", len(full_name))
print("City:", city_name)
print("Length of city:", len(city_name))
print("College Name:", college_name)
print("Length of college name:", len(college_name))


"""
2. String Indexing and Slicing
Accept a word and display the first character, last character,
first three characters, last three characters and reverse order.
"""

word = input("Enter a word: ")
print("First character:", word[0])
print("Last character:", word[-1])
print("First three characters:", word[:3])
print("Last three characters:", word[-3:])
print("Reverse order:", word[::-1])


"""
3. String Operations
Accept two strings. Join both strings, display them with a space,
repeat the first string five times and display uppercase and lowercase.
"""

string_1 = input("Enter first string: ")
string_2 = input("Enter second string: ")
combined_string = string_1 + string_2
combined_with_space = string_1 + " " + string_2

print("Joined strings:", combined_string)
print("Strings with space:", combined_with_space)
print("First string repeated five times:", string_1 * 5)
print("Uppercase:", combined_with_space.upper())
print("Lowercase:", combined_with_space.lower())


"""
4. Name Formatting Application
Accept a full name with unnecessary spaces and different letter cases.
Display the cleaned name, uppercase, lowercase, title case, character
count, first name and last name separately.
"""

entered_name = input("Enter your full name: ")
cleaned_name = entered_name.strip()
name_parts = cleaned_name.split()

print("Name without extra spaces:", cleaned_name)
print("Uppercase:", cleaned_name.upper())
print("Lowercase:", cleaned_name.lower())
print("Title case:", cleaned_name.title())
print("Number of characters:", len(cleaned_name))
print("First name:", name_parts[0])
print("Last name:", name_parts[-1])


"""
5. Character and Word Counter
Accept a sentence and calculate total characters, words, spaces, vowels,
consonants and digits.
"""

sentence = input("Enter a sentence: ")
lower_sentence = sentence.lower()
words = sentence.split()
vowels = "aeiou"
vowel_count = 0
consonant_count = 0
digit_count = 0
space_count = 0

for character in lower_sentence:
    if character in vowels:
        vowel_count += 1
    elif character.isalpha():
        consonant_count += 1
    if character.isdigit():
        digit_count += 1
    if character == " ":
        space_count += 1

print("Total characters:", len(sentence))
print("Total words:", len(words))
print("Total spaces:", space_count)
print("Total vowels:", vowel_count)
print("Total consonants:", consonant_count)
print("Total digits:", digit_count)


"""
6. String Replacement and Search Application
Accept a paragraph and search for a word. Count it, replace it,
and check whether the paragraph starts and ends with given words.
"""

paragraph = input("Enter a paragraph: ")
search_word = input("Enter the word to search: ")
replace_word = input("Enter the replacement word: ")
starting_word = input("Enter the starting word: ")
ending_word = input("Enter the ending word: ")

print("Word is present:", search_word in paragraph)
print("Word count:", paragraph.count(search_word))
print("Updated paragraph:", paragraph.replace(search_word, replace_word))
print("Starts with given word:", paragraph.startswith(starting_word))
print("Ends with given word:", paragraph.endswith(ending_word))


"""
7. Palindrome String Checker
Check whether a word or sentence is a palindrome. Ignore spaces and
differences between uppercase and lowercase letters.
"""

palindrome_text = input("Enter a word or sentence: ")
clean_palindrome_text = palindrome_text.lower().replace(" ", "")

if clean_palindrome_text == clean_palindrome_text[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")


"""
8. Password Strength Analyzer
Accept a password and check its length, uppercase letter, lowercase
letter, numeric digit and special character. Display weak, medium or
strong based on the number of conditions satisfied.
"""

password = input("Enter a password: ")
has_uppercase = False
has_lowercase = False
has_digit = False
has_special = False

for character in password:
    if character.isupper():
        has_uppercase = True
    if character.islower():
        has_lowercase = True
    if character.isdigit():
        has_digit = True
    if not character.isalnum():
        has_special = True

conditions_satisfied = 0
if len(password) >= 8:
    conditions_satisfied += 1
if has_uppercase:
    conditions_satisfied += 1
if has_lowercase:
    conditions_satisfied += 1
if has_digit:
    conditions_satisfied += 1
if has_special:
    conditions_satisfied += 1

if conditions_satisfied >= 5:
    print("Password strength: Strong")
elif conditions_satisfied >= 3:
    print("Password strength: Medium")
else:
    print("Password strength: Weak")


"""
9. Text Analysis and Word Frequency System
Accept a paragraph and count words and characters, find the longest
and shortest word, count each word, display repeated words and display
the paragraph in reverse order.
"""

text = input("Enter a paragraph: ")
text_words = text.lower().split()
word_count = {}

for text_word in text_words:
    text_word = text_word.strip(".,!?")
    if text_word in word_count:
        word_count[text_word] += 1
    else:
        word_count[text_word] = 1

if len(text_words) > 0:
    print("Total words:", len(text_words))
    print("Total characters:", len(text))
    print("Longest word:", max(text_words, key=len))
    print("Shortest word:", min(text_words, key=len))
    print("Word count:", word_count)
    print("Words appearing more than once:")
    for text_word in word_count:
        if word_count[text_word] > 1:
            print(text_word)
    print("Paragraph in reverse order:", text[::-1])
else:
    print("No words were entered")


"""
10. Username and Email Validation System
Accept a username and email address.
The username must have at least five characters, no spaces, start with
an alphabet and contain only letters, numbers or underscores.
The email must contain exactly one @, a domain name, a dot after @ and
no spaces.
"""

username = input("Enter username: ")
email = input("Enter email: ")

username_characters_are_valid = True
for character in username:
    if not (character.isalnum() or character == "_"):
        username_characters_are_valid = False

valid_username = (
    len(username) >= 5
    and " " not in username
    and username[0].isalpha()
    and username_characters_are_valid
)

at_position = email.find("@")
email_has_domain = at_position > 0 and at_position < len(email) - 1
email_has_dot = "." in email[at_position + 1:] if at_position >= 0 else False

valid_email = (
    email.count("@") == 1
    and " " not in email
    and email_has_domain
    and email_has_dot
)

if valid_username:
    print("Username is valid")
else:
    print("Username is invalid")

if valid_email:
    print("Email is valid")
else:
    print("Email is invalid")
