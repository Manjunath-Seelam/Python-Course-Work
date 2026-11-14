"""
DAY 11
PYTHON ASSIGNMENT SOLUTIONS

This file contains simple solutions for all 10 questions.
Each question is kept as a separate section.
"""

"""
DAY 11 – CONTROL STATEMENTS IN PYTHON

Topics: Introduction to Loops, for Loop, while Loop, range() Function, Iterating Through Strings and
Collections, for-else, while-else, break Statement, continue Statement and assert Keyword.

Total Questions: 10

BASIC LEVEL – 3 QUESTIONS

1. Number Printing Application
Question: Write a Python program to accept a positive integer from the user and display all numbers
from 1 up to the entered number.
For example, if the user enters 10, display numbers from 1 to 10.
Perform the same task using both a for loop and a while loop.
Concepts to Use:
• input() function
• int() type conversion
• for loop
• while loop
• range() function
• Incrementing variables
• print() function
"""

num = int(input("Enter a positive integer: "))

if num > 0:
    print("\nUsing for loop:")
    for i in range(1, num + 1):
        print(i, end=" ")

    print("\n\nUsing while loop:")
    i = 1
    while i <= num:
        print(i, end=" ")
        i += 1
    print()
else:
    print("Please enter a positive integer.")


"""
2. Multiplication Table Generator
Question: Develop a multiplication table generator.
Accept a number from the user and display its multiplication table from 1 to 20.
Display the output in the following format:
• 5 × 1 = 5
• 5 × 2 = 10
• Continue up to 5 × 20 = 100.
Allow the user to choose whether the table should be generated using a for loop or a while loop.
Concepts to Use:
• input() function
• int() type conversion
• for loop
• while loop
• range() function
• Arithmetic operators
• F-string formatting
• Conditional statements
"""

num = int(input("Enter a number to generate its multiplication table: "))
choice = input("Choose loop type (for/while): ").lower()

if choice == "for":
    for i in range(1, 21):
        print(f"{num} × {i} = {num * i}")
elif choice == "while":
    i = 1
    while i <= 20:
        print(f"{num} × {i} = {num * i}")
        i += 1
else:
    print("Invalid choice. Please choose for or while.")


"""
3. Sum and Average of Numbers
Question: Write a Python program to accept a positive integer N from the user.
Calculate and display:
• Sum of numbers from 1 to N.
• Average of numbers from 1 to N.
• Count of numbers.
• Sum of even numbers.
• Sum of odd numbers.
Perform the calculations using a for loop and a while loop.
Concepts to Use:
• input() function
• int() type conversion
• for loop
• while loop
• range() function
• Accumulator variables
• Modulus operator (%)
• Arithmetic operators
"""

n = int(input("Enter a positive integer N: "))

if n > 0:
    # Calculations using for loop
    total = 0
    even_sum = 0
    odd_sum = 0
    count = 0

    for i in range(1, n + 1):
        total += i
        count += 1

        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i

    average = total / count

    print("\nUsing for loop:")
    print(f"Sum of numbers : {total}")
    print(f"Average        : {average:.2f}")
    print(f"Count          : {count}")
    print(f"Sum of even    : {even_sum}")
    print(f"Sum of odd     : {odd_sum}")

    # Calculations using while loop
    total = 0
    even_sum = 0
    odd_sum = 0
    count = 0
    i = 1

    while i <= n:
        total += i
        count += 1

        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i

        i += 1

    average = total / count

    print("\nUsing while loop:")
    print(f"Sum of numbers : {total}")
    print(f"Average        : {average:.2f}")
    print(f"Count          : {count}")
    print(f"Sum of even    : {even_sum}")
    print(f"Sum of odd     : {odd_sum}")
else:
    print("Please enter a positive integer.")


"""
MEDIUM LEVEL – 3 QUESTIONS

4. Student Marks Analysis System
Question: Develop a student marks analysis application.
Accept the number of students and collect the marks of each student.
Calculate and display:
• Total marks obtained by all students.
• Average marks.
• Highest marks.
• Lowest marks.
• Number of students who passed.
• Number of students who failed.
Assume that students scoring 40 or above have passed.
Display a separate result for every student.
Concepts to Use:
• input() function
• Lists
• for loop
• range() function
• Conditional statements
• if-else statement
• sum(), max() and min() functions
• Accumulator and counter variables
• Arithmetic operators
"""

students = int(input("Enter number of students: "))

if students > 0:
    marks_list = []
    passed = 0
    failed = 0

    for i in range(students):
        marks = float(input(f"Enter marks of student {i + 1}: "))
        marks_list.append(marks)

        if marks >= 40:
            passed += 1
        else:
            failed += 1

    total_marks = sum(marks_list)
    average_marks = total_marks / students
    highest_marks = max(marks_list)
    lowest_marks = min(marks_list)

    print("\n========== STUDENT RESULTS ==========")
    for i in range(students):
        if marks_list[i] >= 40:
            result = "Pass"
        else:
            result = "Fail"
        print(f"Student {i + 1}: Marks = {marks_list[i]:.2f}, Result = {result}")

    print("-------------------------------------")
    print(f"Total Marks   : {total_marks:.2f}")
    print(f"Average Marks : {average_marks:.2f}")
    print(f"Highest Marks : {highest_marks:.2f}")
    print(f"Lowest Marks  : {lowest_marks:.2f}")
    print(f"Passed        : {passed}")
    print(f"Failed        : {failed}")
    print("=====================================")
else:
    print("Enter at least one student.")


"""
5. ATM PIN Verification System Using While Loop
Question: Develop an ATM PIN verification application.
Set the correct PIN as 1234.
Ask the user to enter their PIN.
Apply the following conditions:
1. Allow a maximum of three attempts.
2. If the PIN is correct, display a successful login message.
3. If the PIN is incorrect, display the number of attempts remaining.
4. If all three attempts are incorrect, display an account access blocked message.
5. Once the correct PIN is entered, stop asking for the PIN.
Concepts to Use:
• input() function
• int() type conversion
• while loop
• Counter variables
• Conditional statements
• if-else statement
• break statement
• Comparison operators
"""

correct_pin = 1234
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    entered_pin = int(input("Enter your ATM PIN: "))
    attempts += 1

    if entered_pin == correct_pin:
        print("PIN verified successfully. Login successful!")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Incorrect PIN. Attempts remaining: {remaining}")
        else:
            print("All attempts used. Account access blocked.")


"""
6. Number Searching Application Using Loop Else
Question: Develop a number searching application.
Create a list containing at least 15 numbers.
Accept a number from the user and search for it in the list using a for loop.
Apply the following conditions:
1. If the number is found, display its position in the list.
2. Stop searching immediately after finding the number.
3. If the number is not found after checking the entire list, display an appropriate message using the
loop's else block.
Repeat the same task using a while loop with an else block.
Concepts to Use:
• Lists
• input() function
• int() type conversion
• for loop
• while loop
• else with loops
• break statement
• Conditional statements
• List indexing
"""

numbers = [10, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150]
search_num = int(input("Enter the number to search: "))

print("\nUsing for loop:")
for i in range(len(numbers)):
    if numbers[i] == search_num:
        print(f"Number found at position {i + 1}.")
        break
else:
    print("Number not found in the list.")

print("\nUsing while loop:")
i = 0
while i < len(numbers):
    if numbers[i] == search_num:
        print(f"Number found at position {i + 1}.")
        break
    i += 1
else:
    print("Number not found in the list.")


"""
ADVANCED LEVEL – 4 QUESTIONS

7. Electricity Bill Analysis System
Question: Develop an electricity bill analysis application for multiple customers.
Accept the number of customers and collect the following details for each customer:
• Customer ID
• Customer name
• Electricity units consumed
Calculate the electricity bill using the following rates:
• First 100 units – ₹2 per unit.
• Next 100 units – ₹3 per unit.
• Next 100 units – ₹5 per unit.
• Above 300 units – ₹7 per unit.
Apply the rates progressively to each slab.
Perform the following operations:
• Calculate the bill for every customer.
• Display each customer's bill.
• Calculate the total revenue collected.
• Identify the customer with the highest bill.
• Calculate the average electricity bill.
• Count the number of customers whose bills exceed ₹2,000.
Concepts to Use:
• Lists
• Dictionaries
• for loop
• range() function
• Conditional statements
• Nested if-elif-else
• Accumulator variables
• Counter variables
• max() function
• Arithmetic operators
• F-string formatting
"""

customer_count = int(input("Enter number of customers: "))

if customer_count > 0:
    customers = []
    total_revenue = 0
    above_2000 = 0

    for i in range(customer_count):
        print(f"\nEnter details for customer {i + 1}:")
        customer_id = input("Enter Customer ID: ")
        customer_name = input("Enter Customer Name: ")
        units = float(input("Enter electricity units consumed: "))

        if units < 0:
            print("Units cannot be negative. Please enter the details again.")
            units = float(input("Enter valid electricity units consumed: "))

        if units <= 100:
            bill = units * 2
        elif units <= 200:
            bill = (100 * 2) + ((units - 100) * 3)
        elif units <= 300:
            bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)
        else:
            bill = (100 * 2) + (100 * 3) + (100 * 5) + ((units - 300) * 7)

        customer = {
            "id": customer_id,
            "name": customer_name,
            "units": units,
            "bill": bill
        }
        customers.append(customer)
        total_revenue += bill

        if bill > 2000:
            above_2000 += 1

        print(f"Bill for {customer_name}: ₹{bill:.2f}")

    bills = [customer["bill"] for customer in customers]
    highest_bill = max(bills)
    average_bill = total_revenue / customer_count
    highest_customer = max(customers, key=lambda customer: customer["bill"])

    print("\n========== ELECTRICITY BILL ANALYSIS ==========")
    for customer in customers:
        print(f"ID: {customer['id']}, Name: {customer['name']}, "
              f"Units: {customer['units']}, Bill: ₹{customer['bill']:.2f}")

    print("-----------------------------------------------")
    print(f"Total Revenue             : ₹{total_revenue:.2f}")
    print(f"Highest Bill              : ₹{highest_bill:.2f}")
    print(f"Highest Bill Customer     : {highest_customer['name']}")
    print(f"Average Electricity Bill : ₹{average_bill:.2f}")
    print(f"Customers Above ₹2,000   : {above_2000}")
    print("================================================")
else:
    print("Enter at least one customer.")


"""
8. Number Guessing Game with Limited Attempts
Question: Develop a number guessing game.
Set a secret number in the program.
Ask the user to guess the number.
Apply the following conditions:
1. Allow the user a maximum of five attempts.
2. If the guessed number is lower than the secret number, display "Too Low".
3. If the guessed number is higher than the secret number, display "Too High".
4. If the guessed number is correct, display a winning message.
5. Stop the game immediately when the user guesses correctly.
6. If all five attempts are unsuccessful, display the correct secret number.
Concepts to Use:
• Variables
• input() function
• int() type conversion
• while loop
• Counter variables
• if-elif-else statements
• break statement
• Comparison operators
• F-string formatting
"""

secret_number = 27
attempts = 0
max_attempts = 5

print("Welcome to the Number Guessing Game!")

while attempts < max_attempts:
    guess = int(input("Guess the secret number: "))
    attempts += 1

    if guess < secret_number:
        print("Too Low")
    elif guess > secret_number:
        print("Too High")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempt(s).")
        break
else:
    print(f"Game Over! The correct secret number was {secret_number}.")


"""
9. Online Shopping Cart Using Break and Continue
Question: Develop an online shopping cart application.
Create a product list containing at least ten products with their prices.
Allow the customer to select products and enter their quantities.
Apply the following conditions:
1. If the customer enters an invalid product number, display an error message and use continue to
skip that iteration.
2. If the customer enters quantity zero, skip that product using continue.
3. If the customer enters 0 as the product selection, stop shopping using break.
4. Calculate the total price for every selected product.
5. Display the selected products, quantities, individual prices and final bill.
Concepts to Use:
• Lists
• Dictionaries
• while loop
• for loop
• break statement
• continue statement
• Conditional statements
• Arithmetic operators
• Accumulator variables
• F-string formatting
"""

products = [
    {"name": "Laptop", "price": 45000},
    {"name": "Mobile", "price": 15000},
    {"name": "Headphones", "price": 1200},
    {"name": "Keyboard", "price": 800},
    {"name": "Mouse", "price": 500},
    {"name": "Monitor", "price": 9000},
    {"name": "USB Drive", "price": 600},
    {"name": "Speaker", "price": 1800},
    {"name": "Webcam", "price": 2200},
    {"name": "Power Bank", "price": 1400}
]

cart = []
total_bill = 0

print("========== PRODUCT LIST ==========")
for i in range(len(products)):
    print(f"{i + 1}. {products[i]['name']} - ₹{products[i]['price']}")
print("0. Finish Shopping")
print("==================================")

while True:
    product_choice = int(input("\nEnter product number (0 to finish): "))

    if product_choice == 0:
        break

    if product_choice < 1 or product_choice > len(products):
        print("Invalid product number. Please try again.")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity < 0:
        print("Quantity cannot be negative.")
        continue
    elif quantity == 0:
        print("Quantity is zero. Skipping this product.")
        continue

    selected_product = products[product_choice - 1]
    item_total = selected_product["price"] * quantity

    cart.append({
        "name": selected_product["name"],
        "price": selected_product["price"],
        "quantity": quantity,
        "total": item_total
    })

    total_bill += item_total
    print(f"{selected_product['name']} added to cart.")

print("\n========== SHOPPING CART BILL ==========")
if len(cart) == 0:
    print("No products selected.")
else:
    for item in cart:
        print(f"{item['name']} | Quantity: {item['quantity']} | "
              f"Price: ₹{item['price']} | Total: ₹{item['total']}")
    print("----------------------------------------")
    print(f"Final Bill: ₹{total_bill:.2f}")
print("========================================")


"""
10. Employee Attendance and Payroll Validation System
Question: Develop an employee attendance and payroll validation application.
Accept the number of employees and collect the following details for each employee:
• Employee ID
• Employee name
• Monthly salary
• Number of working days
• Number of days present
Apply the following validation conditions:
1. Monthly salary must be greater than zero.
2. Working days must be greater than zero.
3. Days present cannot be negative.
4. Days present cannot exceed the total working days.
5. Use the assert keyword to validate the entered data.
6. If the employee data is valid, calculate the salary based on the number of days present.
7. If the data is invalid, handle the assertion error and display an appropriate message.
8. Continue processing the remaining employees even if one employee's data is invalid.
Display a payroll report containing employee details, attendance percentage and payable salary for every
valid employee.
Concepts to Use:
• Lists
• Dictionaries
• for loop
• range() function
• assert keyword
• try-except blocks for handling assertion errors
• Conditional statements
• Arithmetic operators
• Accumulator variables
• F-string formatting
"""

employee_count = int(input("Enter number of employees: "))

if employee_count > 0:
    payroll_report = []
    total_payroll = 0

    for i in range(employee_count):
        print(f"\nEnter details for employee {i + 1}:")
        employee_id = input("Enter Employee ID: ")
        employee_name = input("Enter Employee Name: ")
        monthly_salary = float(input("Enter Monthly Salary: ₹"))
        working_days = int(input("Enter Number of Working Days: "))
        days_present = int(input("Enter Number of Days Present: "))

        try:
            assert monthly_salary > 0, "Monthly salary must be greater than zero."
            assert working_days > 0, "Working days must be greater than zero."
            assert days_present >= 0, "Days present cannot be negative."
            assert days_present <= working_days, "Days present cannot exceed working days."

            attendance_percentage = (days_present / working_days) * 100
            payable_salary = (monthly_salary / working_days) * days_present

            employee = {
                "id": employee_id,
                "name": employee_name,
                "salary": monthly_salary,
                "working_days": working_days,
                "days_present": days_present,
                "attendance": attendance_percentage,
                "payable": payable_salary
            }

            payroll_report.append(employee)
            total_payroll += payable_salary

        except AssertionError as error:
            print(f"Invalid employee data: {error}")
            print("Skipping this employee and continuing with the next one.")

    print("\n========== EMPLOYEE PAYROLL REPORT ==========")
    if len(payroll_report) == 0:
        print("No valid employee records available.")
    else:
        for employee in payroll_report:
            print(f"\nEmployee ID       : {employee['id']}")
            print(f"Employee Name     : {employee['name']}")
            print(f"Monthly Salary    : ₹{employee['salary']:.2f}")
            print(f"Working Days      : {employee['working_days']}")
            print(f"Days Present      : {employee['days_present']}")
            print(f"Attendance        : {employee['attendance']:.2f}%")
            print(f"Payable Salary    : ₹{employee['payable']:.2f}")
            print("---------------------------------------------")

        print(f"Total Payroll     : ₹{total_payroll:.2f}")
    print("=============================================")
else:
    print("Enter at least one employee.")
