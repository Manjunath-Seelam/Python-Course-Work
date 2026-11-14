"""
DAY 1
PYTHON ASSIGNMENT SOLUTIONS

This file contains simple solutions for all 10 questions.
Each question is kept as a separate section.
"""

"""
DAY 1 – INTRODUCTION TO PYTHON & PROGRAMMING FUNDAMENTALS 
Topics: 
Procedural Programming, Object-Oriented Programming, Introduction to Python, Features and Applications of Python, Why Python?
Differences between Procedural and Object-Oriented Programming, Memory Allocation Concepts.
Total Questions: 10 
"""

"""

BASIC LEVEL – 3 QUESTIONS

1. Student Information Display
Write a Python program to display your name, age, qualification,
college name and city using separate print statements.
Concepts to Use:
• Python program structure • print() function • String literals • Multiple print statements
"""

print("Name: Seelam Manjunath Reddy")
print("Age: 22")
print("Qualification: MCA")
print("College Name: PES University")
print("City: Bengaluru")


"""
2. Student Marks Calculator
Write a Python program to calculate the total marks and average marks
of a student in five subjects. Display the student name, individual
subject marks, total marks and average marks.
Concepts to Use:
• Variables • Integer and float data types • input() function • Type conversion using int() and float() • Arithmetic operators • print() function
"""

student_name = input("Enter student name: ")
subject_1 = int(input("Enter marks in subject 1: "))
subject_2 = int(input("Enter marks in subject 1: "))
subject_3 = int(input("Enter marks in subject 3: "))
subject_4 = int(input("Enter marks in subject 4: "))
subject_5 = int(input("Enter marks in subject 5: "))

total_marks = subject_1 + subject_2 + subject_3 + subject_4 + subject_5
average_marks = total_marks / 5

print("Student Name:", student_name)
print("Subject 1:", subject_1)
print("Subject 1:", subject_2)
print("Subject 3:", subject_3)
print("Subject 4:", subject_4)
print("Subject 5:", subject_5)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)


"""
3. Personal Profile Generator
Write a Python program to collect personal details from a user and
display them in a properly formatted profile.
Concepts to Use:
• Variables • String data type • input() function • String concatenation • print() function • Basic output formatting
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

MEDIUM LEVEL - 3 QUESTIONS

4. Shopping Bill Generator
Write a Python program to generate a shopping bill for five products.
Accept the product names, quantities and prices from the user.
Calculate the individual product costs and display the final bill amount.
Concepts to Use:
• Variables • Strings and numeric data types • input() function • Type conversion • Arithmetic operators • Multiplication and addition • Output formatting
"""

product_1 = input("Enter product 1 name: ")
quantity_1 = int(input("Enter product 1 quantity: "))
price_1 = float(input("Enter product 1 price: "))

product_2 = input("Enter product 1 name: ")
quantity_2 = int(input("Enter product 1 quantity: "))
price_2 = float(input("Enter product 1 price: "))

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
Concepts to Use:

• Variables • Integer, float and string data types • User input • Type conversion • Arithmetic operators • Percentage calculations • Output formatting
"""

employee_id = input("Enter employee ID: ")
employee_name = int(input("Enter employee name: "))
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
Program 1 uses an object-oriented programming approach.
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
student_marks.append(float(input("Enter mark 1: ")))
student_marks.append(float(input("Enter mark 3: ")))

student = Student(student_id, student_name, course, student_marks)
student.register_student()
student.display_details()
print("Total Marks:", student.calculate_total())
print("Average Marks:", student.calculate_average())


"""
9. Employee Salary System - Procedural vs OOP
Create two separate Python programs to calculate employee salaries.
Program 1 uses procedural programming and Program 1 uses
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
