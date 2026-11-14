"""
DAY 10
PYTHON ASSIGNMENT SOLUTIONS

This file contains simple solutions for all 10 questions.
Each question is kept as a separate section.
"""

"""
DAY 10 – CONDITIONAL STATEMENTS IN PYTHON

Topics: Introduction to Conditional Statements, Decision Making in Python, if Statement, if-else
Statement, Indentation, Conditional Expressions, Nested Conditions, Comparison Operators and Logical
Operators in Decision Making.

Total Questions: 10

BASIC LEVEL – 3 QUESTIONS

1. Positive, Negative or Zero Checker
Question: Write a Python program to accept a number from the user and identify whether the entered
number is positive, negative or zero.
Display an appropriate message based on the entered number.
Concepts to Use:
• input() function
• int() type conversion
• if statement
• if-else statement
• if-elif-else statement
• Comparison operators
• Indentation
"""

num = int(input("Enter a desired number: "))

if num > 0:
    print(f"The number {num} entered is positive.")
elif num < 0:
    print(f"The number {num} entered is negative.")
else:
    print(f"The number {num} is Zero.")


"""
2. Even or Odd Number Checker
Question: Develop a Python program to accept an integer from the user and check whether the number
is even or odd.
Display the result with an appropriate message.
Concepts to Use:
• input() function
• int() type conversion
• if-else statement
• Modulus operator (%)
• Comparison operator (==)
• Indentation
"""

num = int(input("Enter a desired number: "))

if num % 2 == 0:
    print(f"The number {num} is Even.")
else:
    print(f"The number {num} is Odd.")


"""
3. Voting Eligibility Checker
Question: Develop a voting eligibility application.
Accept the following details from the user:
• Person's name
• Age
• Country
Check whether the person is eligible to vote based on the age requirement of 18 years or above.
Display the person's name and eligibility status.
Concepts to Use:
• input() function
• int() type conversion
• if-else statement
• Comparison operators
• String variables
• F-string formatting
"""

person_name = input("Enter your name: ")
age = int(input("Enter your age: "))
country = input("Enter your country: ")

if age >= 18:
    print(f"{person_name} is eligible to vote based on the age requirement.")
else:
    print(f"{person_name} is not eligible to vote based on the age requirement.")

print(f"Country: {country}")


"""
MEDIUM LEVEL – 3 QUESTIONS

4. Student Grade Calculation System
Question: Develop a student grade calculation application.
Accept the student's name and marks in five subjects.
Calculate the total marks and percentage.
Assign grades based on the following conditions:
• 90% and above – Grade A
• 80% to below 90% – Grade B
• 70% to below 80% – Grade C
• 60% to below 70% – Grade D
• 40% to below 60% – Grade E
• Below 40% – Fail
Display the student's name, total marks, percentage and final grade.
Concepts to Use:
• input() function
• int() type conversion
• Arithmetic operators
• if-elif-else statement
• Comparison operators
• F-string formatting
"""

student_name = input("Enter student name: ")
telugu = int(input("Enter marks in Telugu: "))
hindi = int(input("Enter marks in Hindi: "))
english = int(input("Enter marks in English: "))
maths = int(input("Enter marks in Maths: "))
science = int(input("Enter marks in Science: "))

total_marks = telugu + hindi + english + maths + science
average_marks = total_marks / 5

print("\n========== STUDENT RESULT ==========")
print(f"Student Name : {student_name}")
print(f"Telugu       : {telugu}")
print(f"Hindi        : {hindi}")
print(f"English      : {english}")
print(f"Maths        : {maths}")
print(f"Science      : {science}")
print(f"Total Marks  : {total_marks}")
print(f"Percentage   : {average_marks:.2f}%")

if average_marks >= 90:
    print("Grade       : A")
elif average_marks >= 80:
    print("Grade       : B")
elif average_marks >= 70:
    print("Grade       : C")
elif average_marks >= 60:
    print("Grade       : D")
elif average_marks >= 40:
    print("Grade       : E")
else:
    print("Grade       : Fail")


"""
5. Electricity Bill Calculator
Question: Develop an electricity bill calculation application.
Accept the following details:
• Customer name
• Customer ID
• Number of electricity units consumed
Calculate the electricity bill using the following rates:
• First 100 units – ₹2 per unit
• Next 100 units (101–200) – ₹3 per unit
• Next 100 units (201–300) – ₹5 per unit
• Above 300 units – ₹7 per unit
Apply the rates progressively to each slab.
Display the customer details, consumed units and total electricity bill.
Concepts to Use:
• input() function
• int() type conversion
• if-elif-else statement
• Nested conditional statements
• Comparison operators
• Arithmetic operators
• F-string formatting
"""

cust_name = input("Enter your name: ")
cust_id = input("Enter your Customer ID: ")
units_used = int(input("Enter No. of units consumed: "))

if units_used < 0:
    print("Enter valid units consumed.")
else:
    if units_used <= 100:
        bill_amount = units_used * 2
    elif units_used <= 200:
        bill_amount = (100 * 2) + ((units_used - 100) * 3)
    elif units_used <= 300:
        bill_amount = (100 * 2) + (100 * 3) + ((units_used - 200) * 5)
    else:
        bill_amount = (100 * 2) + (100 * 3) + (100 * 5) + ((units_used - 300) * 7)

    print("\n========== ELECTRICITY BILL ==========")
    print(f"Customer Name : {cust_name}")
    print(f"Customer ID   : {cust_id}")
    print(f"Units Used    : {units_used}")
    print(f"Bill Amount   : ₹{bill_amount:.2f}")
    print("======================================")


"""
6. Employee Bonus Eligibility System
Question: Develop an employee bonus eligibility application.
Accept the following details:
• Employee name
• Employee salary
• Years of experience
• Performance rating (1 to 5)
Apply the following conditions:
• Employees with at least 5 years of experience and a performance rating of 4 or 5 receive a 20%
bonus.
• Employees with at least 3 years of experience and a performance rating of 3 or above receive a
10% bonus.
• All other employees receive a 5% bonus.
Calculate the bonus amount and final salary after adding the bonus.
Display the employee details, bonus percentage, bonus amount and final salary.
Concepts to Use:
• input() function
• int() and float() type conversion
• if-elif-else statement
• Nested conditions
• Logical operators (and, or)
• Comparison operators
• Arithmetic operators
• F-string formatting
"""

emp_name = input("Enter your name: ")
emp_salary = float(input("Enter your salary: ₹"))
exp = int(input("Enter your experience in years: "))
perf_rating = int(input("Enter your performance rating from 1-5: "))

if emp_salary <= 0 or exp < 0 or not 1 <= perf_rating <= 5:
    print("Enter valid employee details.")
else:
    if exp >= 5 and perf_rating >= 4:
        bonus_percentage = 20
    elif exp >= 3 and perf_rating >= 3:
        bonus_percentage = 10
    else:
        bonus_percentage = 5

    bonus = emp_salary * bonus_percentage / 100
    total_salary = emp_salary + bonus

    print("\n========== EMPLOYEE BONUS DETAILS ==========")
    print(f"Employee Name      : {emp_name}")
    print(f"Employee Salary    : ₹{emp_salary:.2f}")
    print(f"Experience         : {exp} years")
    print(f"Performance Rating : {perf_rating}")
    print(f"Bonus Percentage   : {bonus_percentage}%")
    print(f"Bonus Amount       : ₹{bonus:.2f}")
    print(f"Final Salary       : ₹{total_salary:.2f}")
    print("============================================")


"""
ADVANCED LEVEL – 4 QUESTIONS

7. ATM Withdrawal Validation System
Question: Develop an ATM withdrawal validation application.
Accept the following details:
• Account holder name
• Account balance
• Withdrawal amount
• ATM PIN
Assume the correct ATM PIN is 1234.
Apply the following conditions:
1. If the entered PIN is incorrect, display an invalid PIN message.
2. If the withdrawal amount is less than or equal to zero, display an invalid amount message.
3. If the withdrawal amount exceeds the account balance, display insufficient balance.
4. If the withdrawal amount is a multiple of ₹100 and all other conditions are satisfied, process the
withdrawal.
5. Otherwise, display an appropriate withdrawal amount error.
Display the transaction status and remaining account balance.
Concepts to Use:
• input() function
• int() and float() type conversion
• if-elif-else statement
• Nested conditional statements
• Logical operators (and, or)
• Comparison operators
• Modulus operator (%)
• Arithmetic operators
• F-string formatting
"""

name = input("Enter Account Holder Name: ")
balance = float(input("Enter Account Balance: ₹"))
withdrawal = float(input("Enter Withdrawal Amount: ₹"))
pin = int(input("Enter PIN Number: "))

if pin != 1234:
    print("Invalid PIN Entered.")
elif balance < 0:
    print("Invalid account balance.")
elif withdrawal <= 0:
    print("Entered withdrawal amount is invalid.")
elif withdrawal > balance:
    print("Insufficient funds.")
elif withdrawal % 100 != 0:
    print("Enter the withdrawal amount in multiples of 100.")
else:
    balance = balance - withdrawal
    print("\n========== ATM TRANSACTION ==========")
    print(f"Account Holder       : {name}")
    print(f"Amount Withdrawn     : ₹{withdrawal:.2f}")
    print(f"Remaining Balance    : ₹{balance:.2f}")
    print("Transaction Status  : Successful")
    print("=====================================")


"""
8. Online Shopping Discount and Delivery System
Question: Develop an online shopping discount calculation application.
Accept the following details:
• Customer name
• Product name
• Product price
• Quantity
• Customer membership type (Regular, Silver or Gold)
• Delivery location (Local or Other City)
Apply the following discount conditions:
• Regular customers – No membership discount.
• Silver members – 5% discount.
• Gold members – 10% discount.
Apply an additional 5% discount if the total purchase amount before membership discount is ₹5,000 or
above.
Delivery charges:
• Local delivery – ₹50.
• Other City delivery – ₹100.
• Free delivery if the final purchase amount after discounts is ₹5,000 or above.
Calculate and display the original amount, applicable discounts, delivery charges and final payable
amount.
Concepts to Use:
• input() function
• int() and float() type conversion
• if-elif-else statement
• Nested conditional statements
• Logical operators
• Comparison operators
• Arithmetic operators
• F-string formatting
"""

customer_name = input("Enter Customer Name: ")
product_name = input("Enter Product Name: ")
product_price = float(input("Enter Product Price: ₹"))
quantity = int(input("Enter Quantity: "))

membership_type = input("Enter Membership Type (Regular/Silver/Gold): ").lower()
delivery_location = input("Enter Delivery Location (Local/Other City): ").lower()

if product_price <= 0 or quantity <= 0:
    print("Enter a valid product price and quantity.")
elif membership_type not in ("regular", "silver", "gold"):
    print("Invalid membership type!")
elif delivery_location not in ("local", "other city"):
    print("Invalid delivery location!")
else:
    original_amount = product_price * quantity

    if membership_type == "regular":
        membership_discount = 0
    elif membership_type == "silver":
        membership_discount = original_amount * 0.05
    else:
        membership_discount = original_amount * 0.10

    if original_amount >= 5000:
        additional_discount = original_amount * 0.05
    else:
        additional_discount = 0

    total_discount = membership_discount + additional_discount
    final_purchase_amount = original_amount - total_discount

    if final_purchase_amount >= 5000:
        delivery_charges = 0
    elif delivery_location == "local":
        delivery_charges = 50
    else:
        delivery_charges = 100

    final_payable_amount = final_purchase_amount + delivery_charges

    print("\n========== SHOPPING BILL ==========")
    print(f"Customer Name          : {customer_name}")
    print(f"Product Name           : {product_name}")
    print(f"Product Price          : ₹{product_price:.2f}")
    print(f"Quantity               : {quantity}")
    print(f"Membership Type        : {membership_type.title()}")
    print(f"Delivery Location      : {delivery_location.title()}")
    print("-----------------------------------")
    print(f"Original Amount        : ₹{original_amount:.2f}")
    print(f"Membership Discount    : ₹{membership_discount:.2f}")
    print(f"Additional Discount    : ₹{additional_discount:.2f}")
    print(f"Total Discount         : ₹{total_discount:.2f}")
    print(f"Amount After Discounts : ₹{final_purchase_amount:.2f}")
    print(f"Delivery Charges       : ₹{delivery_charges:.2f}")
    print("-----------------------------------")
    print(f"Final Payable Amount   : ₹{final_payable_amount:.2f}")
    print("===================================")


"""
9. Hospital Patient Billing and Consultation System
Question: Develop a hospital billing application.
Accept the following details:
• Patient name
• Patient age
• Consultation type (General or Specialist)
• Number of laboratory tests
• Cost per laboratory test
• Number of hospital room days
• Room type (General, Semi-Private or Private)
Apply the following charges:
Consultation Charges:
• General consultation – ₹300.
• Specialist consultation – ₹700.
Room Charges Per Day:
• General – ₹500.
• Semi-Private – ₹1,000.
• Private – ₹2,000.
Additional Conditions:
• Patients aged 60 years or above receive a 10% discount on consultation charges.
• Laboratory charges are calculated based on the number of tests and cost per test.
• Room charges depend on room type and number of days.
Calculate the total consultation charges, laboratory charges, room charges, discount and final hospital
bill.
Display a complete patient billing statement.
Concepts to Use:
• input() function
• int() and float() type conversion
• if-elif-else statement
• Nested conditional statements
• Logical operators
• Comparison operators
• Arithmetic operators
• F-string formatting
"""

patient_name = input("Enter Patient Name: ")
patient_age = int(input("Enter Patient Age: "))
consultation_type = input("Enter Consultation Type (General/Specialist): ").lower()
number_of_tests = int(input("Enter Number of Laboratory Tests: "))
cost_per_test = float(input("Enter Cost Per Laboratory Test: ₹"))
room_days = int(input("Enter Number of Hospital Room Days: "))
room_type = input("Enter Room Type (General/Semi-Private/Private): ").lower()

if patient_age < 0 or number_of_tests < 0 or cost_per_test < 0 or room_days < 0:
    print("Enter valid patient, test and room details.")
elif consultation_type not in ("general", "specialist"):
    print("Invalid consultation type!")
elif room_type not in ("general", "semi-private", "private"):
    print("Invalid room type!")
else:
    if consultation_type == "general":
        consultation_charges = 300
    else:
        consultation_charges = 700

    if patient_age >= 60:
        discount = consultation_charges * 0.10
    else:
        discount = 0

    laboratory_charges = number_of_tests * cost_per_test

    if room_type == "general":
        room_charges = 500 * room_days
    elif room_type == "semi-private":
        room_charges = 1000 * room_days
    else:
        room_charges = 2000 * room_days

    final_consultation_charges = consultation_charges - discount
    total_bill = final_consultation_charges + laboratory_charges + room_charges

    print("\n========== HOSPITAL BILL ==========")
    print(f"Patient Name                  : {patient_name}")
    print(f"Patient Age                   : {patient_age}")
    print(f"Consultation Type             : {consultation_type.title()}")
    print(f"Room Type                     : {room_type.title()}")
    print(f"Number of Room Days           : {room_days}")
    print(f"Number of Laboratory Tests    : {number_of_tests}")
    print("-----------------------------------")
    print(f"Consultation Charges          : ₹{consultation_charges:.2f}")
    print(f"Senior Citizen Discount       : ₹{discount:.2f}")
    print(f"Final Consultation Charges    : ₹{final_consultation_charges:.2f}")
    print(f"Laboratory Charges            : ₹{laboratory_charges:.2f}")
    print(f"Room Charges                  : ₹{room_charges:.2f}")
    print("-----------------------------------")
    print(f"Final Hospital Bill           : ₹{total_bill:.2f}")
    print("===================================")


"""
10. Smart Loan Eligibility and EMI Estimation System
Question: Develop a loan eligibility and EMI estimation application.
Accept the following details:
• Applicant name
• Applicant age
• Monthly salary
• Existing monthly loan commitments
• Requested loan amount
• Credit score
Apply the following eligibility conditions:
1. Applicant must be at least 21 years old and not older than 60 years.
2. Monthly salary must be ₹25,000 or above.
3. Credit score must be 650 or above.
4. Existing monthly loan commitments must not exceed 40% of the monthly salary.
5. Requested loan amount must not exceed 20 times the monthly salary.
If all conditions are satisfied:
• Display the loan approval message.
• Calculate an estimated monthly EMI using a simple fixed repayment estimate: divide the
requested loan amount by 60 months.
• Display the estimated monthly EMI.
Otherwise, display the reason for loan rejection.
Concepts to Use:
• input() function
• int() and float() type conversion
• if-elif-else statement
• Nested conditional statements
• Logical operators (and, or)
• Comparison operators
• Arithmetic operators
• F-string formatting
"""

applicant_name = input("Enter Applicant Name: ")
applicant_age = int(input("Enter Applicant Age: "))
monthly_salary = float(input("Enter Monthly Salary: ₹"))
existing_commitments = float(input("Enter Existing Monthly Loan Commitments: ₹"))
requested_loan_amount = float(input("Enter Requested Loan Amount: ₹"))
credit_score = int(input("Enter Credit Score: "))

if applicant_age < 21 or applicant_age > 60:
    print("\nLoan Rejected!")
    print("Reason: Applicant age must be between 21 and 60 years.")
elif monthly_salary < 25000:
    print("\nLoan Rejected!")
    print("Reason: Monthly salary must be ₹25,000 or above.")
elif credit_score < 650:
    print("\nLoan Rejected!")
    print("Reason: Credit score must be 650 or above.")
elif existing_commitments < 0 or existing_commitments > monthly_salary * 0.40:
    print("\nLoan Rejected!")
    print("Reason: Existing loan commitments must not exceed 40% of monthly salary.")
elif requested_loan_amount <= 0 or requested_loan_amount > monthly_salary * 20:
    print("\nLoan Rejected!")
    print("Reason: Requested loan amount must be positive and must not exceed 20 times monthly salary.")
else:
    monthly_emi = requested_loan_amount / 60

    print("\n========== LOAN APPROVAL ==========")
    print(f"Applicant Name              : {applicant_name}")
    print(f"Applicant Age               : {applicant_age}")
    print(f"Monthly Salary              : ₹{monthly_salary:.2f}")
    print(f"Existing Loan Commitments   : ₹{existing_commitments:.2f}")
    print(f"Requested Loan Amount       : ₹{requested_loan_amount:.2f}")
    print(f"Credit Score                : {credit_score}")
    print("-----------------------------------")
    print("Loan Status                 : APPROVED")
    print(f"Estimated Monthly EMI       : ₹{monthly_emi:.2f}")
    print("Repayment Period            : 60 Months")
    print("===================================")
