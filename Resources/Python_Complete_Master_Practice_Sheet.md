# Python Complete Master Practice Sheet

**Purpose:** One consolidated, topic-organized practice file built from the supplied reference documents. It contains questions only—no solutions, code, or explanatory answers. Exact duplicate prompts have been consolidated; prompts that use a different loop, method, constraint, or expected behavior remain separate. Source-provided input/output examples are attached to the relevant questions or listed in the execution-reference appendix.

## How to use this sheet

- Practise in topic order; write and run each solution yourself.
- Where an execution example is provided, use it to check your program’s behavior.
- If a source question refers to “the conditions in the source document” but did not provide exact thresholds in the extracted text, the question is retained without inventing thresholds.
- Input/output examples are references from the supplied files; for randomised exercises, outputs may vary.

## Contents

- [Conditional Statements](#conditional-statements)
  - [If Statement](#if-statement) · [If-Else Statement](#if-else-statement) · [If-Elif-Else Statement](#if-elif-else-statement) · [Nested If Statement](#nested-if-statement)
- [Loops](#loops)
  - [While Loop](#while-loop) · [For Loop](#for-loop) · [Break and Continue](#break-and-continue-statements) · [Pass Statement](#pass-statement)
- [Pattern Generation](#pattern-generation-programs)
  - [Star Patterns](#star-patterns) · [Number Patterns](#number-patterns)
- [Data Structures](#data-structures)
  - [Lists](#lists) · [Tuples](#tuples) · [Sets](#sets) · [Dictionaries](#dictionaries)
  - [List Comprehensions](#list-comprehensions) · [Set Comprehensions](#set-comprehensions) · [Dictionary Comprehensions](#dictionary-comprehensions)
- [Shuffling](#shuffling) · [Swapping](#swapping) · [Sorting](#sorting)
- [Strings and String Methods](#strings-and-string-methods)
  - [String Operations](#string-operations) · [String Methods](#string-methods) · [Slicing](#slicing)
- [Functions and Advanced Paradigms](#functions-and-advanced-paradigms)
  - [Functions](#functions) · [Scope](#scope) · [Lambda Functions](#lambda-functions) · [Recursion](#recursion)
  - [Function Arguments](#default-arguments) · [Higher-Order Functions](#higher-order-functions) · [Decorators](#decorators) · [Closures](#closures)
  - [Generators](#generator-functions) · [Standard Library and Built-ins](#python-standard-library-and-built-ins-source-heading-infinite-sequence-generator) · [Custom Modules](#custom-function-libraries-and-modules)
- [Object-Oriented Programming](#object-oriented-programming-oop)
  - [Classes and Objects](#classes-and-objects) · [Inheritance](#inheritance) · [Abstraction](#abstraction) · [Polymorphism](#polymorphism)
  - [Method Overriding and Operator Overloading](#method-overriding-and-operator-overloading) · [Static Methods](#static-methods) · [Property Decorators](#property-decorators) · [Encapsulation](#encapsulation)
- [Supplementary Execution References](#supplementary-execution-references) · [For-Loop Execution References](#supplementary-for-loop-execution-references)
- [Source Coverage Notes](#source-coverage-notes)


# CONDITIONAL STATEMENTS


## If Statement

1. Write a Python program that checks if a number is positive.

2. Write a Python program that checks if a given string is empty.

3. Write a Python program that determines if a number is positive, negative, or zero using only if statements and no elif or else.

4. Write a Python program that checks if a number is a multiple of both 3 and 5.

5. Write a Python program that determines if a given number is a perfect square.

6. Write a Python program that checks if a number is divisible by both 2 and 3.

7. Write a Python program that determines if a number is a perfect cube.

8. Write a Python program that checks if a given number is a multiple of 4.

9. Take a number input and print whether it is even or odd.

10. Check whether a given number is a multiple of 5 or not.

11. Ask the user to enter their name. If the name is “admin”, print “Welcome, Admin!”.

12. Take a number input and print “Zero” if it is 0, otherwise print “Non-Zero”.

13. Write a Python program to display “Best Seller” if product sales are greater than 1000.

14. Write a Python program to check whether a user gets a verified badge: if the account is eligible for verification and the Meta Verified subscription is active, display “Verified Badge Granted”.

15. Write a Python program that checks whether it is raining and displays “Extra Rain Charges Applied” if the condition is True. Use an if statement only.


## If-Else Statement

1. Write a Python program that checks if a given year is a leap year.

2. Write a Python program that checks if a given character is a vowel or a consonant.

3. Write a Python program that checks if a given year is a century year (ending in '00').

4. Write a Python program that checks if a given number is prime.

5. Write a Python program that checks if a person is eligible to vote based on their age.

6. Write a Python program that checks if a number is positive or non-positive (including zero).

7. Write a Python program that compares two numbers and prints the larger one.

8. Write a Python program that checks if a given character is a letter or not.

9. Write a Python program that finds and prints the smallest of three numbers without using inbuilt methods.

10. Write a Python program to check if a given string is a palindrome.

11. Write a Python program that finds and prints the largest of four numbers.

12. Write a Python program that takes two numbers as input and determines the sign of their difference.

13. Write a Python program that checks if a given year is a leap year using an alternative method.

14. Write a Python program that checks if a number is a multiple of 7 or not.

15. Write a Python program that calculates and prints the absolute value of a given number.

16. Take marks as input and print “Pass” if marks are at least 35; otherwise print “Fail”.

17. Write a Python program to validate a username and password.

18. Write a Python program to check whether a product exists in an available product list.

19. A food-delivery app offers free delivery for orders above ₹99. If the order value is ₹99 or below, add a delivery charge of ₹30. Calculate and display the final bill amount using if-else.

20. Username and Password Login: validate credentials and display “Login Successful” or “Invalid Credentials”.

21. Product Search: check whether a requested product exists in the available products list and display “Product Found” or “Product Not Found”.

22. Delivery Charge Calculation: calculate the final bill using free delivery above ₹99 and a ₹30 delivery charge for orders of ₹99 or below.


## If-Elif-Else Statement

1. Write a Python program that converts a temperature in Celsius to Fahrenheit or vice versa based on user input.

2. Write a simple calculator program that performs addition, subtraction, multiplication, or division based on the user’s operation choice.

3. Write a Python program for a simple "Guess the Number" game. Generate a random number, and let the user guess it.

4. Write a Python program that checks the strength of a user's password based on certain criteria.

5. Write a Python program that calculates the final price of an item after applying a discount based on the purchase amount.

6. Write a Python program that simulates an ATM machine, allowing users to check their balance and withdraw money.

7. Write a Python program that greets the user differently based on the time of day.

8. Write a Python program that calculates the final price of an item after applying a discount coupon code.

9. Write a Python program that calculates and prints the grade based on a given score, but also validates the input score.

10. Write a Python program that determines the number of days in a given month.

11. Write a Python program that calculates a person's Body Mass Index (BMI) and categorizes it into different categories (underweight, normal weight, overweight, obese).

12. Write a Python program that converts letter grades (A, B, C, D, F) to their equivalent GPA values.

13. Take an input number and check whether it is a three-digit number. Treat negative three-digit numbers such as -898 as three-digit numbers.

14. Take a temperature as input: above 30 → “It’s hot”; between 15 and 30 → “Pleasant”; below 15 → “Cold”.

15. Take marks and print A for 90 and above, B for 80–89, C for 70–79, D for 60–69, and F below 60.

16. Input the number of sides and determine the polygon: 3 → Triangle, 4 → Quadrilateral, 5 → Pentagon, otherwise → Unknown shape.

17. Calculate bus fare based on age: below 5 → Free; age 5–18 → Half Ticket; above 18 → Full Ticket.

18. Categorize average marks: above 90 → Excellent; 70–90 → Good; below 70 → Needs Improvement.

19. Weekend Planner Based on Budget: Budget > ₹10,000 → Trip; > ₹5,000 → Resort Stay; > ₹3,000 → Movie and Dinner; > ₹1,000 → Cafe and Shopping; > ₹500 → Street Food and Park Visit; otherwise → Stay Home.

20. Hosting Plan Based on Budget: above ₹10,000 → Cloud Hosting; above ₹5,000 → Business Hosting; above ₹2,000 → Premium Hosting; otherwise → Single Hosting.

21. Greeting Based on Time: hour 5–11 → Good Morning; 12–16 → Good Afternoon; 17–20 → Good Evening; otherwise → Good Night.


## Nested If Statement

1. Given x = 10 and y = 5, write a Python program to determine if x is greater than y. If x is greater than y, check if it's also greater than 15 and print appropriate messages accordingly.

2. Write a Python program that takes a grade as input and prints the corresponding letter grade. If the grade is less than 70, also print "You failed."

3. Write a Python program to check if a person is eligible for a credit card based on their age and income. If the person is underage, print "You are underage." If they are of age but have an income below $30,000, print "Your income is too low for a credit card."

4. Write a Python program to determine if a given number num is even or odd. If it's even, check if it's greater than 10 and print appropriate messages.

5. Write a Python program that calculates the ticket price for a theme park based on age and height. If a person is under 12 years old and under 4 feet tall, the ticket price is $10. If they are under 12 but 4 feet tall or taller, the ticket price is $15. If a person is 12 or older and under 4 feet tall, the ticket price is $15. If they are 12 or older and 4 feet tall or taller, the ticket price is $20.

6. Write a Python program for user authentication. Ask the user to enter their username and password. If both the username and password are correct, print "Access granted." If the username is correct but the password is incorrect, print "Incorrect password." If the username is incorrect, print "Invalid username."

7. Write a Python program for ordering food. Ask the user to select a type of food (e.g., "Burger" or "Pizza"). If they choose "Burger," ask if they want fries. If they choose "Pizza," ask if they want extra cheese. Print their order with the additional items if chosen.

8. Write a Python program that takes an integer as input and checks if it's positive, negative, or zero. If it's positive, check if it's even or odd. Print the appropriate messages.

9. Write a Python program that asks for a user's age and checks if they have a driver's license. If the user is 18 or older and has a driver's license, print "You are eligible to drive." Otherwise, print "You are not eligible to drive."

10. Write a Python program that checks if a person is eligible to vote. Ask for the person's age and citizenship. If the person is at least 18 years old and a citizen, print "You are eligible to vote." Otherwise, print "You are not eligible to vote."

11. Write a Python program that takes three numbers as input and prints them in ascending order.

12. Write a Python program for a store that calculates discounts based on the purchase amount and membership status. Ask the user for the purchase amount and whether they have a membership. If the purchase amount is greater than $100 and they have a membership, apply a 20% discount. If the purchase amount is greater than $100 without membership, apply a 10% discount. Otherwise, no discount is applied.

13. Write a Python program that classifies a character as a vowel, consonant, or neither. Ask the user to enter a single character. If it's a vowel (a, e, i, o, u), print "Vowel." If it's a consonant, print "Consonant." If it's neither (e.g., a digit or special character), print "Neither."

14. Write a Python program that recommends books based on the reader's age and genre preference. Ask the user for their age and favorite genre ("Mystery," "Fantasy," or "Science Fiction"). Recommend different books based on their input.

15. Write a Python program that calculates the price of movie tickets based on age and time of day. Ask the user for their age and whether it's a matinee show (before 5 PM). If the person is under 12 or over 65, they get a discount. Apply different pricing rules based on age and showtime.

16. Write a Python program for a delivery service that calculates delivery charges based on distance and order amount. Ask the user for the distance (in miles) and order amount. Apply different charges based on the distance and order amount.

17. Write a Python program that classifies an employee's performance rating based on performance score (Excellent, Good, or Average) and years of service. Calculate and print the bonus based on their rating.

18. Write a Python program for a library that calculates late fees for borrowed books. Ask the user for the number of days the book is overdue and the type of book (regular or reference). Calculate and print the late fee.

19. Write a Python program that determines whether a student is eligible for a scholarship based on their GPA and extracurricular activities. Ask for the student's GPA and the number of extracurricular activities they are involved in. Award the scholarship if GPA is above 3.5 and they are involved in at least 3 activities.

20. Write a Python program that recommends clothing based on the weather temperature and whether it's raining. Ask the user for the temperature (in degrees Celsius) and whether it's raining. Provide clothing recommendations accordingly.

21. Write a Python program that recommends a movie based on the user's preferences. Ask the user for their preferred genre and age group, and provide movie recommendations accordingly.

22. Write a Python program that determines whether a credit card application is approved based on the applicant's credit score and income. Ask the user for their credit score and income, and provide an approval status.

23. Write a Python program for vehicle registration based on the type of vehicle and emissions. Ask the user for the vehicle type (car or truck) and emissions status (clean or high). Provide the registration fee based on the inputs.

24. Take a character input and check whether it is an uppercase letter, lowercase letter, or not a letter.

25. Check whether a number is a multiple of 5; if it is, check whether it is even or odd and print the appropriate message using nested if.

26. Check whether a number is a multiple of 5; if it is not, check whether it is positive or negative and print the result using nested if-else.

27. Instagram Story Visibility: check whether the user follows the account; if they do, check whether they are in the Close Friends list. If both are true, display “Story Visible”; otherwise display the appropriate message.

28. BGMI Tournament Entry: check whether the player has registered; if registered, check whether the entry fee is paid. If both are true, display “Tournament Entry Confirmed”; otherwise display the appropriate message.

29. Google Drive File Access: check whether the file link is active; if active, check whether permission is granted. If both are true, display “File Opened Successfully”; otherwise display the appropriate message.


# LOOPS


## While Loop

1. Basic Counting: Write a while loop that counts from 1 to 10 and prints each number.
   - **Sample input 1:**
     ```text
     No input required
     ```
     **Expected output 1:**
     ```text
     1
     2
     3
     4
     5
     6
     7
     8
     9
     10
     ```
   - **Sample input 2:**
     ```text
     No input required
     ```
     **Expected output 2:**
     ```text
     1
     2
     3
     4
     5
     6
     7
     8
     9
     10
     ```

2. Create a program that asks the user to enter a number, and then use a while loop to count down from that number to 1, printing each value.
   - **Sample input 1:**
     ```text
     Enter a number: 5
     ```
     **Expected output 1:**
     ```text
     5
     4
     3
     2
     1
     ```
   - **Sample input 2:**
     ```text
     Enter a number: 3
     ```
     **Expected output 2:**
     ```text
     3
     2
     1
     ```

3. Write a while loop that calculates the sum of even numbers from 1 to 100.
   - **Sample input 1:**
     ```text
     No input required
     ```
     **Expected output 1:**
     ```text
     Sum of even numbers: 2550
     ```
   - **Sample input 2:**
     ```text
     No input required
     ```
     **Expected output 2:**
     ```text
     Sum of even numbers: 2550
     ```

4. Create a simple number guessing game using a while loop. Generate a random number and have the user guess it, giving hints like "too high" or "too low" until they guess correctly.
   - **Sample input 1:**
     ```text
     Enter your guess: 5
     ```
     **Expected output 1:**
     ```text
     Too low
     Enter your guess: 8
     Too high
     Enter your guess: 7
     Congratulations! Correct guess.
     ```
   - **Sample input 2:**
     ```text
     Enter your guess: 10
     ```
     **Expected output 2:**
     ```text
     Congratulations! Correct guess.
     ```

5. Use a while loop to calculate the factorial of a given number.
   - **Sample input 1:**
     ```text
     Enter number: 5
     ```
     **Expected output 1:**
     ```text
     Factorial: 120
     ```
   - **Sample input 2:**
     ```text
     Enter number: 4
     ```
     **Expected output 2:**
     ```text
     Factorial: 24
     ```

6. Write a while loop that prints all even numbers between 1 and 50.
   - **Sample input 1:**
     ```text
     No input required
     ```
     **Expected output 1:**
     ```text
     2
     4
     6
     8
     10
     12
     14
     16
     18
     20
     22
     24
     26
     28
     30
     32
     34
     36
     38
     40
     42
     44
     46
     48
     50
     ```
   - **Sample input 2:**
     ```text
     No input required
     ```
     **Expected output 2:**
     ```text
     2
     4
     6
     8
     10
     12
     14
     16
     18
     20
     22
     24
     26
     28
     30
     32
     34
     36
     38
     40
     42
     44
     46
     48
     50
     ```

7. Create a program that calculates the sum of the digits of a given integer using a while loop.
   - **Sample input 1:**
     ```text
     Enter number: 1234
     ```
     **Expected output 1:**
     ```text
     Sum of digits: 10
     ```
   - **Sample input 2:**
     ```text
     Enter number: 567
     ```
     **Expected output 2:**
     ```text
     Sum of digits: 18
     ```

8. Generate a multiplication table for a given number using a while loop.
   - **Sample input 1:**
     ```text
     Enter number: 5
     ```
     **Expected output 1:**
     ```text
     5 x 1 = 5
     5 x 2 = 10
     5 x 3 = 15
     5 x 4 = 20
     5 x 5 = 25
     5 x 6 = 30
     5 x 7 = 35
     5 x 8 = 40
     5 x 9 = 45
     5 x 10 = 50
     ```
   - **Sample input 2:**
     ```text
     Enter number: 7
     ```
     **Expected output 2:**
     ```text
     7 x 1 = 7
     7 x 2 = 14
     7 x 3 = 21
     7 x 4 = 28
     7 x 5 = 35
     7 x 6 = 42
     7 x 7 = 49
     7 x 8 = 56
     7 x 9 = 63
     7 x 10 = 70
     ```

9. Write a program to find all the factors of a given number using a while loop.
   - **Sample input 1:**
     ```text
     Enter number: 12
     ```
     **Expected output 1:**
     ```text
     Factors: 1 2 3 4 6 12
     ```
   - **Sample input 2:**
     ```text
     Enter number: 10
     ```
     **Expected output 2:**
     ```text
     Factors: 1 2 5 10
     ```

10. Implement a program that reverses even numbers using a while loop.
   - **Sample input 1:**
     ```text
     Enter even number: 2468
     ```
     **Expected output 1:**
     ```text
     Reversed number: 8642
     ```
   - **Sample input 2:**
     ```text
     Enter even number: 120
     ```
     **Expected output 2:**
     ```text
     Reversed number: 21
     ```

11. Create a program that prompts the user to enter a password. Keep asking until they enter the correct password.
   - **Sample input 1:**
     ```text
     Enter password: 1234
     Enter password: admin
     ```
     **Expected output 1:**
     ```text
     Incorrect password
     Incorrect password
     ```
   - **Sample input 2:**
     ```text
     Enter password: python
     ```
     **Expected output 2:**
     ```text
     Correct password
     Access granted
     ```

12. Write a program using a while loop to generate the first n terms of the Fibonacci sequence.
   - **Sample input 1:**
     ```text
     Enter number of terms: 5
     ```
     **Expected output 1:**
     ```text
     0 1 1 2 3
     ```
   - **Sample input 2:**
     ```text
     Enter number of terms: 8
     ```
     **Expected output 2:**
     ```text
     0 1 1 2 3 5 8 13
     ```

13. Build a program that checks if a given number is prime using a while loop.
   - **Sample input 1:**
     ```text
     Enter number: 7
     ```
     **Expected output 1:**
     ```text
     7 is a prime number
     ```
   - **Sample input 2:**
     ```text
     Enter number: 10
     ```
     **Expected output 2:**
     ```text
     10 is not a prime number
     ```

14. Create a program that checks if a given word or phrase is a palindrome (reads the same forwards and backwards) using a while loop.
   - **Sample input 1:**
     ```text
     Enter word: madam
     ```
     **Expected output 1:**
     ```text
     madam is a palindrome
     ```
   - **Sample input 2:**
     ```text
     Enter word: hello
     ```
     **Expected output 2:**
     ```text
     hello is not a palindrome
     ```

15. Write a program to generate the first n rows of Pascal's Triangle using while loops.
   - **Sample input 1:**
     ```text
     Enter number of rows: 4
     ```
     **Expected output 1:**
     ```text
     1
     1 1
     1 2 1
     1 3 3 1
     ```
   - **Sample input 2:**
     ```text
     Enter number of rows: 3
     ```
     **Expected output 2:**
     ```text
     1
     1 1
     1 2 1
     ```

16. Create a program that converts a given integer into words (e.g., 123 -> "one hundred twenty-three") using a while loop.
   - **Sample input 1:**
     ```text
     Enter number: 123
     ```
     **Expected output 1:**
     ```text
     One Hundred Twenty Three
     ```
   - **Sample input 2:**
     ```text
     Enter number: 45
     ```
     **Expected output 2:**
     ```text
     Forty Five
     ```

17. Write a program to reverse a given string using a while loop.
   - **Sample input 1:**
     ```text
     Enter string: Python
     ```
     **Expected output 1:**
     ```text
     Reverse: nohtyP
     ```
   - **Sample input 2:**
     ```text
     Enter string: Hello
     ```
     **Expected output 2:**
     ```text
     Reverse: olleH
     ```

18. Implement a program to find the greatest common divisor of two numbers using a while loop and the Euclidean algorithm.
   - **Sample input 1:**
     ```text
     Enter first number: 48
     Enter second number: 18
     ```
     **Expected output 1:**
     ```text
     GCD: 6
     ```
   - **Sample input 2:**
     ```text
     Enter first number: 20
     Enter second number: 8
     ```
     **Expected output 2:**
     ```text
     GCD: 4
     ```

19. Create a program that converts a binary number (entered as a string) to its decimal equivalent using a while loop.
   - **Sample input 1:**
     ```text
     Enter binary number: 1010
     ```
     **Expected output 1:**
     ```text
     Decimal number: 10
     ```
   - **Sample input 2:**
     ```text
     Enter binary number: 1101
     ```
     **Expected output 2:**
     ```text
     Decimal number: 13
     ```

20. Write a program that prints all prime numbers between 1 and 100 using a while loop.
   - **Sample input 1:**
     ```text
     No input required
     ```
     **Expected output 1:**
     ```text
     2 3 5 7 11 13 17 19 23 29
     31 37 41 43 47 53 59 61 67 71
     73 79 83 89 97
     ```
   - **Sample input 2:**
     ```text
     No input required
     ```
     **Expected output 2:**
     ```text
     2 3 5 7 11 13 17 19 23 29
     31 37 41 43 47 53 59 61 67 71
     73 79 83 89 97
     ```

21. Implement a program to calculate the result of raising a number to a given power using a while loop, without using the built-in exponentiation operator.
   - **Sample input 1:**
     ```text
     Enter base: 2
     Enter power: 5
     ```
     **Expected output 1:**
     ```text
     Result: 32
     ```
   - **Sample input 2:**
     ```text
     Enter base: 3
     Enter power: 4
     ```
     **Expected output 2:**
     ```text
     Result: 81
     ```

22. Create a program that calculates and prints the prime factorization of a given number using a while loop.
   - **Sample input 1:**
     ```text
     Enter number: 12
     ```
     **Expected output 1:**
     ```text
     Prime factors: 2 2 3
     ```
   - **Sample input 2:**
     ```text
     Enter number: 60
     ```
     **Expected output 2:**
     ```text
     Prime factors: 2 2 3 5
     ```

23. Build a program that searches for a specific word in a text using a while loop and prints the word's first occurrence.
   - **Sample input 1:**
     ```text
     Enter text: Python is easy and Python is powerful
     Enter word: Python
     ```
     **Expected output 1:**
     ```text
     Word found at index: 0
     ```
   - **Sample input 2:**
     ```text
     Enter text: I love Python programming
     Enter word: Python
     ```
     **Expected output 2:**
     ```text
     Word found at index: 7
     ```

24. Implement matrix multiplication (matrix dot product) using nested while loops.
   - **Sample input 1:**
     ```text
     Matrix A:
     1 2
     3 4
     
     Matrix B:
     5 6
     7 8
     ```
     **Expected output 1:**
     ```text
     Result:
     19 22
     43 50
     ```
   - **Sample input 2:**
     ```text
     Matrix A:
     1 2
     3 4
     
     Matrix B:
     1 0
     0 1
     ```
     **Expected output 2:**
     ```text
     Result:
     1 2
     3 4
     ```

25. Given an unsorted array of integers, find the length of the longest consecutive elements sequence using a while loop.
   - **Sample input 1:**
     ```text
     Array: [100, 4, 200, 1, 3, 2]
     ```
     **Expected output 1:**
     ```text
     Longest consecutive sequence length: 4
     ```
   - **Sample input 2:**
     ```text
     Array: [10, 5, 12, 3, 4, 11, 2]
     ```
     **Expected output 2:**
     ```text
     Longest consecutive sequence length: 4
     ```

26. Reverse a number using a while loop.


## For Loop

1. Print numbers from 1 to 5 using a for loop?

2. Calculate the sum of numbers from 1 to 10 using a for loop ?

3. Print even numbers from 1 to 10 using a for loop?

4. Calculate the factorial of a number using a for loop?

5. Print elements of a list using a for loop ?

6. Find the maximum value in a list using a for loop ?

7. Print characters in a string using a for loop ?

8. Count the number of vowels in a string using a for loop ?

9. Iterate over a dictionary and print key-value pairs using a for loop ?

10. Print a pattern using nested for loops ?

11. Calculate the sum of all even numbers from 1 to 100 using a for loop ?

12. Print the first 10 Fibonacci numbers using a for loop ?

13. Find and print the common elements between two lists using a for loop ?

14. Generate a multiplication table for a given number using a for loop ?

15. Calculate the factorial of a number using a for loop with a range starting from 1 ?

16. Print the reverse of a string using a for loop ?

17. Generate a list of squares for numbers from 1 to 10 using a for loop ?

18. Count the number of words in a sentence using a for loop ?

19. Calculate the sum of digits in a number using a for loop ?

20. Generate a list of prime numbers within a given range using a for loop ?

21. Calculate the power of a number using a for loop ?

22. Reverse a list using a for loop ?

23. Find and print the largest element in a list using a for loop ?

24. Calculate the average of numbers in a list using a for loop ?

25. Print a countdown from a given number using a for loop ?

26. Generate a pattern of numbers using nested for loops ?

27. Calculate the product of elements in a list using a for loop ?

28. Find and print the position (index) of an element in a list using a for loop ?

29. Calculate the sum of all odd numbers from 1 to 100 using a for loop ?

30. Print a triangle of asterisks using a for loop ?

31. Calculate the LCM (Least Common Multiple) of two numbers using a for loop ?

32. Count the number of prime numbers in a range using a for loop ?

33. Reverse words in a sentence using a for loop ?

34. Print a diamond pattern using nested for loops ?

35. Print a hollow square pattern using nested for loops ?

36. Calculate the factorial of a number using a for loop with a specified step ?

37. Print a right-angled triangle pattern using a for loop ?

38. Generate a list of multiples of a number within a given range using a for loop ?

39. Print vowels from a string using a for loop.

40. Print consonants from a string using a for loop.

41. Find the factors of a number using a for loop.


## Break and Continue Statements

1. Write a Python program to find and print the first prime number greater than 100. Use a loop and the break statement to exit the loop once you find the prime number.

2. Create a Python program to calculate the sum of all numbers from 1 to 100. However, if the number is divisible by both 3 and 5, skip it using the continue statement.

3. Write a Python program to find and print the factors of a given number (input by the user). Use a loop and the break statement to exit the loop once you find all factors.

4. Implement a program that calculates the average of a list of numbers, but ignore any negative numbers. Use the continue statement to skip negative numbers in the list.

5. Create a Python program that simulates a basic login system. Ask the user to enter a username and password. If the entered password is incorrect, give the user three attempts. Use the break statement to exit the loop if the password is correct or the user exceeds the maximum attempts.

6. Write a Python program that finds the first 10 even numbers. If a number is divisible by 3, skip it using the continue statement.

7. Implement a program to calculate the factorial of a number entered by the user. Use a loop and the break statement to exit the loop when the calculation is complete.

8. Write a Python program that generates and prints the first 20 terms of the Fibonacci sequence. However, if a term is greater than 100, stop generating the sequence using the break statement.

9. Create a Python program that asks the user to enter a series of numbers. Calculate and print the average of these numbers. If the user enters a negative number, stop taking input and calculate the average of the numbers entered so far using the break statement.

10. Implement a Python program that counts and prints the number of vowels in a given string. Use a loop to iterate through the characters in the string and use the continue statement to skip consonants.

11. Write a Python program to print all the prime numbers between 1 and 100. Use a loop and the break statement to exit the loop when you determine a number is not prime.

12. Create a Python program that simulates a basic menu-driven application. The program should display a menu to the user with options like "Add," "View," and "Exit." Use the break statement to exit the loop when the user selects "Exit."

13. Write a Python program that asks the user to input a password. If the password is not at least 8 characters long, keep asking for a valid password using a loop. Use the continue statement to skip further processing until a valid password is provided.

14. Write a Python program to find the sum of all even numbers from 1 to 100. However, if a multiple of 7 is encountered, skip it using the continue statement.


## Pass Statement

1. Create a Python program that iterates over a list of integers and prints all even numbers. For odd numbers, use the pass statement to do nothing.

2. Write a Python program that asks the user to input a list of numbers. For each number in the list, check if it's a prime number. If it's prime, print it; if not, use the pass statement.

3. Implement a Python program that simulates a basic class structure for a geometric shape. Create a class named Shape, and for now, use the pass statement to indicate that further methods need to be added in the future.

4. Write a Python program that reads a text file and counts the number of lines that contain the word "apple." For lines that don't contain the word, use the pass statement.

5. Create a Python program to check if a given number is a perfect square. If it is, print a message; otherwise, use the pass statement.

6. Implement a Python program that iterates through a list of tasks. For each task, check if it's completed. If it's completed, print a message; if not, use the pass statement.

7. Create a Python program that defines a class called Employee. Use the pass statement to indicate that you need to define attributes and methods for the class later.

8. Write a Python program to iterate through a list of sentences and check if each sentence ends with a question mark. If it does, print the sentence; otherwise, use the pass statement.


# PATTERN GENERATION PROGRAMS


## Star Patterns

1. Print a simple pattern of increasing asterisks.

2. Print a simple pattern of decreasing asterisks.

3. Print a pattern of right-aligned asterisks with spaces.

4. Print a pattern of left-aligned asterisks with spaces.

5. Print a pyramid pattern with spaces.

6. Print an inverted pyramid pattern with spaces.

7. Print an upside-down pyramid pattern with spaces.

8. Print a hollow half pyramid pattern.

9. Print a diamond pattern.

10. Print a hollow square pattern.

11. Print a hollow diamond pattern.

12. Print an hourglass pattern.

13. Print a checkered pattern of stars and spaces.


## Number Patterns

1. Print a pattern of numbers from 1 to n.

2. Print a pattern of numbers in a right-angled triangle.

3. Print a pattern of numbers in an inverted right-angled triangle.

4. Print a pattern of numbers with alternating rows.

5. Print a pattern of numbers in an inverted pyramid.

6. Print a pattern of numbers in a right-angled triangle (inverted).

7. Print a pattern of numbers in a right-angled triangle with reversed rows.

8. Print a pattern of numbers in an hourglass shape.

9. Print a pattern of numbers in a right-angled triangle with descending order.

10. Print a pattern of numbers in an alternating triangle.

11. Print a pattern of numbers with a centered diamond shape.

12. Print a pattern of numbers with a diamond shape.

13. Print a pattern of numbers with a centered triangle.

14. Print a pattern of numbers in a concentric square.

15. Print a pattern of numbers in a spiral order (with variable dimensions and formatting).

16. Print a pattern of numbers in a spiral order.

17. Print a pattern of numbers in a spiral order (with variable dimensions).


# DATA STRUCTURES


## Lists

1. Reverse a list in Python ?

2. Remove duplicates from a list in Python ?

3. Find the maximum and minimum elements in a list ?

4. Sort a list in ascending and descending order ?

5. Check if a list is empty in Python ?

6. Find the index of a specific element in a list ?

7. Count the occurrences of an element in a list ?

8. Merge two lists in Python ?

9. Find the sum of all elements in a list ?

10. Remove an element from a list by its value ?

11. Slice a list to get specific elements ?

12. Find the length (number of elements) of a list ?

13. Add an element to the end of a list ?

14. Iterate through a list using a for loop ?

15. Insert an element at a specific position in a list ?

16. Extend a list with elements from another iterable ?

17. Clear all elements from a list ?

18. Create a copy of a list ?

19. Reverse a list in-place (modify the original list) ?

20. Find the index of the first occurrence of an element from a specific position ?

21. Remove and return the last element from a list ?

22. Find the index of the last occurrence of an element in a list ?

23. Check if two lists are equal?

24. Sort a list in-place (modify the original list) ?

25. Find the second largest element in a list

26. Remove elements at even indices from a list

27. Find the intersection of two lists (common elements)

28. Find the union of two lists (all unique elements from both lists)

29. Remove all occurrences of a specific element from a list

30. Check if a list is a palindrome (reads the same forwards and backwards)

31. Find the frequency of each element in a list and store it in a dictionary

32. Find the longest consecutive subsequence in a list

33. Shuffle a list randomly

34. Find the majority element in a list (element that appears more than n/2 times, if it exists)

35. Check if a list can be divided into two equal sum subarrays

36. Generate all possible subsets of a list

37. Find the missing number in a list containing all numbers from 1 to n except one

38. Implement a stack using a list

39. Implement a queue using two stacks


## Tuples

1. Find the index of the first occurrence and last occurrence of a specific element in a tuple

2. Concatenate two tuples

3. Count the occurrences of an element in a tuple

4. Check if an element exists in a tuple

5. Reverse a tuple

6. Find the maximum and minimum elements in a tuple

7. Check if all elements in a tuple are the same

8. Sort a tuple of numbers in ascending order

9. Find the sum of all elements in a tuple

10. Check if a tuple contains only unique elements

11. Multiply a tuple to repeat its elements

12. Unpack a tuple into individual variables

13. Convert a tuple of strings into a single string

14. Merge two tuples into one using the + operator

15. Create a tuple of tuples (nested tuple)

16. Find the product of all elements in a tuple of numbers

17. Check if a tuple contains duplicate elements

18. Remove an element from a tuple and create a new tuple without that element

19. Find the difference between two tuples

20. Count the occurrences of each element in a tuple and store the results in a dictionary

21. Find the common elements between two tuples

22. Create a tuple from a string

23. Combine multiple tuples into one

24. Find the largest element in a tuple of numbers

25. Create a tuple of even numbers from an existing tuple

26. Check if a tuple is a subset of another tuple

27. Check if a tuple is empty without using the len() function

28. Create a new tuple with elements reversed in order from an existing tuple

29. Check if a tuple contains only numeric elements

30. Check if a tuple is a palindrome (reads the same forwards and backwards)

31. Find the tuple with the maximum sum in a list of tuples

32. Rotate a tuple to the right by k steps

33. Find the kth smallest and kth largest element in a tuple

34. Find the contiguous subarray with the smallest sum in a tuple of integers (Minimum Subarray Sum)

35. Find the longest subarray with at most k distinct elements in a tuple of integers


## Sets

1. Create an empty set in Python and Add or remove an element to a set.

2. Check if an element exists in a set

3. Check if one set is a subset of another

4. Check if two sets are disjoint

5. Find the maximum element in a set

6. Find the minimum element in a set

7. Convert a list to a set

8. Remove an element from a set if it exists, otherwise, do nothing

9. Create a frozen set in Python

10. Check if a set is empty without using len()

11. Remove and return an arbitrary element from a set

12. Update a set with elements from another set

13. Find the sum and average of all elements in a set

14. Implement set operations (union, intersection, difference)

15. Create a set with unique elements from a list

16. Check if a set is a superset of multiple other sets

17. Find the most common element in a set

18. Find the longest consecutive sequence of elements in a set

19. Find the largest subset of elements in a set that forms an arithmetic progression without using built-in functions

20. Implement set difference in constant time without using built-in functions

21. Generate all unique subsets of a set without using built-in functions

22. Find the longest subarray with distinct elements using a set and without using built-in functions

23. Implement constant-time disjoint set operations without using built-in functions

24. Find the longest subarray with at most K distinct elements using a set without using built-in functions


## Dictionaries

1. Create an empty dictionary and add key-value pairs to it

2. Accessing values associated with a specific key

3. Adding a key-value pair or updating if the key exists

4. Removing a specific key-value pair

5. Dictionary comprehension (filtering)

6. Counting occurrences in a list and storing them in a dictionary

7. Merging two dictionaries into one

8. Finding the key with the minimum and maximum value

9. Sorting a dictionary by its keys in ascending order

10. Finding the key with the longest value in a dictionary

11. Determining the number of key-value pairs in a dictionary

12. Checking if a value exists in a dictionary

13. Removing a key from a dictionary and getting its value

14. Reversing key-value pairs in a dictionary

15. Get a default value if the key doesn’t exist

16. Merge dictionaries using the update method

17. Sorting a dictionary by values in ascending order/descending order

18. Getting a list of keys sorted by their values

19. Inverting a dictionary (swapping keys and values)

20. Merging dictionaries so that values are added together if keys exist in both dictionaries

21. Dictionary comprehension with conditions (creating a new dictionary with a condition)

22. Extracting unique values from a dictionary's values

23. Implementing a switch-case statement using a dictionary

24. Finding keys associated with a specific value in a dictionary

25. Updating multiple values in a dictionary

26. Getting a dictionary containing keys from one dictionary and values from another

27. Flattening a nested dictionary

28. Using a dictionary to implement a simple calculator

29. How can you safely retrieve a value from a dictionary without raising an error if the key doesn't exist?

30. How can you create a dictionary using a list comprehension?

31. How can you create a deep copy of a nested dictionary?

32. How can you create a dictionary that calculates the frequency of words in a text string?


## List Comprehensions

1. Create a list of squares from 1 to 10.?

2. Filter even numbers from a list.??

3. Convert characters in a string to uppercase.??

4. Find common elements between two lists.?

5. Extract vowels from a string.?

6. Find lengths of words in a list of words.??

7. Calculate the sum of squares of all even numbers from 1 to 20.??

8. Generate a list of the first 10 multiples of 3.??

9. Flatten a list of lists into a single list.??

10. Find the intersection of two lists of numbers.??

11. Filter names that start with the letter "A" from a list of names.??

12. Create a list of all prime numbers less than 50.?

13. Filter strings with more than five characters from a list of strings.?

14. Create a list comprehension to find the squares of even numbers and cubes of odd numbers in a given list of integers.?

15. Calculate the cumulative sum of a list of numbers using a list comprehension.?

16. Create a list comprehension to extract the first letter of each word in a sentence.?

17. Filter out duplicates from a list using a list comprehension?

18. Create a list comprehension to reverse the order of words in a sentence:


## Set Comprehensions

1. Create a set comprehension that generates a set of all even numbers from 1 to 20.

2. Given a list of words, create a set comprehension that generates a set of unique words longer than 3 characters.

3. Generate a set comprehension that extracts the vowels from a given string.

4. Create a set comprehension that calculates the squares of numbers from 1 to 10, but includes only those that are divisible by 3.

5. Given two sets, A and B, create a set comprehension that generates the union of these sets.

6. Create a set comprehension that extracts all uppercase letters from a given string.

7. Generate a set comprehension that extracts the unique words from a list of sentences.

8. Create a set comprehension that generates a set of all vowels in a given sentence, ignoring case.

9. Create a set comprehension that generates a set of the first 10 multiples of 3.

10. Given a list of numbers, create a set comprehension that generates a set of squares of values if the number is positive.

11. Generate a set comprehension that extracts unique email domains from a list of email addresses.

12. Generate a set comprehension that extracts unique positive even numbers from a given list.

13. Create a set comprehension that generates a set of unique lowercase characters from a given string.

14. Create a set comprehension that produces the unique lengths of words in a sentence.


## Dictionary Comprehensions

1. Create a dictionary comprehension that generates a dictionary of squares of numbers from 1 to n and uses the number as the key.

2. Given two lists, one containing names and the other containing ages, create a dictionary comprehension to map names to ages.

3. Generate a dictionary comprehension that filters out names longer than 5 characters from a list of names.

4. Create a dictionary comprehension to count the frequency of each character in a given string.

5. Given a list of tuples representing words and their lengths, create a dictionary comprehension to construct a dictionary where words are keys and lengths are values.

6. Create a dictionary comprehension that extracts all words starting with a vowel from a given list of words.

7. Given a list of sentences, create a dictionary comprehension that counts the number of words in each sentence.

8. Generate a dictionary comprehension that calculates the square of numbers from 1 to 10, but only for numbers that are divisible by 3.

9. Given a list of strings, create a dictionary comprehension that maps each string to its length and adds a key-value pair only if the length is even.

10. Given a list of email addresses, create a dictionary comprehension that maps the username (before '@') to the domain.

11. Generate a dictionary comprehension that combines two lists into a dictionary.

12. Create a dictionary comprehension that keeps only dictionary entries whose values exceed a specified threshold.


# SHUFFLING


## Shuffling

1. Given a list of numbers, shuffle its elements.
   - **Source example:** A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] · Output: [5, 2, 1, 9, 7, 3, 10, 6, 8, 4]

2. Given a sentence, shuffle its words.
   - **Source example:** S = "This is a sample sentence to shuffle." · Output: sample This sentence shuffle, a to is

3. Given a list of numbers, shuffle the even and odd numbers separately and then merge them.
   - **Source example:** A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] · Output: [4, 1, 6, 3, 8, 5, 10, 7, 2, 9]

4. Given a list of names, create random pairs.
   - **Source example:** A = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah"] · Output: · Hannah, Alice · Charlie, Grace · Bob, David · Eve, Frank

5. Given a list, shuffle its elements such that elements which are the same are at least 2 positions away from each other.
   - **Source example:** Input: [1, 1, 2, 2, 3, 3] · Output: [1, 2, 1, 3, 2, 3] or [2, 1, 3, 1, 2, 3]


# SWAPPING


## Swapping

1. Given two numbers, swap their values without using a third variable.

2. Given two strings, swap their values.
   - **Source example:** Input: str1 = "hello", str2 = "world" · Output: ("world", "hello")

3. Given a list, swap its first and last elements.
   - **Source example:** Input: list = [1, 2, 3, 4, 5] · Output: [5, 2, 3, 4, 1]

4. Given a string, swap the characters at positions i and j
   - **Source example:** Input: s = "hello", i = 1, j = 3 · Output: "hlleo"

5. Given a list, swap elements at even indices with elements at odd indices.

6. Given a list, swap every pair of elements and then reverse the entire list.
   - **Source example:** Input: list = [1, 2, 3, 4, 5, 6] · Output: [6, 5, 4, 3, 2, 1]

7. Given two lists, swap their middle elements. If a list has an even number of elements, consider the two middle elements.
   - **Source example:** list1 = [1, 2, 3, 4, 5] · list2 = ['a', 'b', 'c', 'd', 'e'] · Output: · List1 = [1, 2, 'c', 4, 5] · List2 = ['a', 'b', 3, 'd', 'e']

8. Given a list, swap every element with its mirrored position. For instance, the first element is swapped with the last, the second with the second last, and so on.
   - **Source example:** my_list = [1, 2, 3, 4, 5] · Output = [5, 4, 3, 2, 1]


# SORTING


## Sorting

1. Given a list of numbers, sort them in ascending order.
   - **Source example:** Input: [5, 2, 7, 1, 3] · Output: [1, 2, 3, 5, 7]

2. Given a list of strings, sort them alphabetically.
   - **Source example:** Input: ["apple", "banana", "orange", "grape", "pear"] · Output: ["apple", "banana", "grape", "orange", "pear"]

3. Given a list of strings, sort them by their length.
   - **Source example:** Input: ["apple", "banana", "orange", "grape", "pear"] · Output: ["pear", "apple", "grape", "banana", "orange"]

4. Given a list of numbers, sort them in descending order.
   - **Source example:** Input: [5, 2, 7, 1, 3] · Output: [7, 5, 3, 2, 1]

5. Given a list of tuples where each tuple contains two elements, sort the list based on the second element of each tuple.
   - **Source example:** Input: [(1, 5), (2, 3), (3, 8), (4, 1), (5, 6)] · Output: [(4, 1), (2, 3), (1, 5), (5, 6), (3, 8)]

6. Given a list of words, sort them based on their last character.
   - **Source example:** Input: ["apple", "banana", "orange", "grape", "pear"] · Output: ["banana", "grape", "apple", "orange", "pear"]

7. Given a list of integers and strings, sort them such that all strings are on the left and all integers are on the right.
   - **Source example:** Input: ["apple", 3, "banana", 1, "orange", 5] · Output: ["apple", "banana", "orange", 1, 3, 5]

8. Given a list of words, sort them based on the count of vowels in each word. If two words have the same vowel count, maintain their original order.
   - **Source example:** Input: ["apple", "banana", "orange", "grape", "pear"] · Output: ["pear", "apple", "orange", "banana", "grape"]

9. Given a list of numbers, sort the list such that all even numbers are on the left and all odd numbers are on the right, with both sections sorted in ascending order.
   - **Source example:** Input: [5, 2, 8, 1, 7, 4, 3, 6] · Output: [2, 4, 6, 8, 1, 3, 5, 7]


# STRINGS AND STRING METHODS


## String Operations

1. Write a Program to Reverse given string

2. Write a Program to Count vowels in the given String

3. Write a Program to Capitalize First Letter of Words of given string

4. Write a Program to Check the given string is palindrome or not

5. Write a Program to Count Occurrences of Substring

6. Write a Program to find the Length of string

7. Write a Program to Convert to Uppercase in the given string

8. Write a Program to Convert to Lowercase in the given string

9. Write a Program to Concatenate Strings

10. Write a Program to Check If Character Exists in the given string or not

11. Write a Program to Print First and Last Character of given string

12. Write a Program to Check the given String Repetition or not

13. Write a Program to Replace a Character in the given string

14. Write a Program to Display Your Name

15. Write a Program to Count the number of times the letter 'e' appears in a given string.

16. Write a Program to Simple String Concatenation of 2 Strings

17. Write a Program to Check is the String Empty?

18. Write a program to remove all vowels from a given string.

19. Write a Program to Count Words in the Given String.

20. Write a Program to Check if String is a Palindrome (ignoring spaces)

21. Write a Program to Given a string, display it in a pyramid format

22. Write a Program to Encode String Write a program that encodes a string by replacing each letter with the next letter (i.e., replace 'a' with 'b', 'b' with 'c', ..., 'z' with 'a').

23. Write a Program to Find the Longest Word in the Given String

24. Write a Program to Determine if two given strings are anagrams (i.e., they contain the same characters in any order).

25. Write a Program to Count the number of consonants in a given string.

26. Write a Program to Extract all the numbers from a given string and display them.

27. Write a Program to Find All Occurrences of Substring

28. Write a Program to Implement the string "abcabc" compression using counts of repeated characters.

29. Write a Program to Rotate a string to the right by a given number of positions.

30. Write a Program to Count the occurrence of each character in a string.

31. Write a Program to Check if a given string can be constructed by taking a substring and repeating it.

32. Write a Program to Find Non-Repeating Character Given a string, find the first non-repeating character in it.

33. Write a Program to Given a string, reverse the order of its words

34. Write a Program to Find the first character in a string that repeats in the Given String.

35. Given a string s containing words separated by spaces, return the length of the last word in the string. If the last word does not exist, return the appropriate result.

36. Remove all adjacent duplicate characters from a string. Continue removing until no more duplicates are found.

37. Write a Program to Remove all adjacent duplicate characters from a string. Continue removing until no more duplicates are found.

38. Write a Program to Given a list of strings, find the longest common prefix among them.

39. Write a Program to Given an integer n, generate the nth term of the "count and say" sequence.

40. Write a Program to Check if a given string can become a palindrome by deleting at most one character from it.

41. Write a Program to Given an array of strings, group anagrams together

42. Write a Program to Given two strings, check if they are one edit distance apart, i.e., they can become equal by adding, deleting, or replacing exactly one character.

43. Write a Program to Display a String

44. Write a Program to Access a Character in a String

45. Write a Program to Convert the int into string by using chr() method.


## String Methods

1. Convert the first character of a string to uppercase using capitalize() method.

2. Convert a string into uppercase using upper() method.

3. Convert the string to lowercase using lower() method.

4. Convert string to lowercase, using casefold() method.

5. Return a centered string using center() method.

6. Count the occurrences of a substring in string using count() method.

7. Return an encoded version of the string using encode() method.

8. Check if the string starts with a specific substring using startswith() method.

9. Check if the string ends with the specified suffix using endswith() method.

10. Find a substring in a string using find() method.

11. Find a substring in a string using index() method.

12. Format the string using format() method.

13. Check if the string has only alphanumeric characters using isalnum() method.

14. Check if the string has only alphabetic characters using isalpha() method.

15. Check if the string has only decimal characters using isdecimal() method.

16. Check if the string contains only digits using isdigit() method.

17. Check if the string is a valid identifier or not, using isidentifier() method.

18. Check if all the letters in the text are in lowercase or not, using islower() method.

19. Check if all the letters in the text are in uppercase or not, using isupper() method.

20. Check if the string contains only numeric characters or not, using isnumeric() method.

21. Check if the string is in title case or not, using istitle() method.

22. Concatenate a list of strings using join() method.

23. Divide a string based on a separator using partition() method.

24. Divide a string based on a separator using rpartition() method.

25. Replace a substring with another substring using replace() method.

26. Find a substring in a string, starting from the right using rfind() method.

27. Find a substring in a string, starting from the right using rindex() method.

28. Return a right-justified version of the string using rjust() method.

29. Return a left-justified version of the string using ljust() method.

30. Remove leading whitespaces using lstrip() method.

31. Remove trailing characters (based on the string argument passed) using rstrip() method.

32. Remove leading (spaces at the beginning) and trailing (spaces at the end) characters using strip() method.

33. Convert the string to Swap case, lowercase becomes uppercase and vice versa using swapcase() method.

34. Convert the first character of each word to uppercase using title() method.

35. Remove the specified prefix or suffix from a string removePrefix() and removeSuffix() method.


## Slicing

1. Given a string, slice it to extract the first 3 characters.
   - **Source example:** Input: "Vcube" · Output: "Vcu"

2. Reversing a List using slicing
   - **Source example:** Input: [1,2,3,4] · Output: [4,3,2,1]

3. Slicing a Tuple
   - **Source example:** Input: (10,11,12,13,14) · Output: (10,11,12)

4. Modify a List Using Slicing
   - **Source example:** Input: [100,200,300,400] · Output: [100,500,300,400]

5. Extract Even-indexed Characters from a String
   - **Source example:** Input: "Vcube Solutions" · Output: "Vesltns"

6. Slicing a List of Lists
   - **Source example:** Input: [[1,2,3],4,5,6] · Output: [3,4]

7. Slicing a String in Reverse
   - **Source example:** Input: "Vcube" · Output: "ebucV"

8. Slicing with a Step of 3
   - **Source example:** Input: "Python" · Output: "Ph"

9. Reversing a List of Strings
   - **Source example:** Input: ["vcube","python","java"] · Output: ["avaj","nohtyp","ebucv"]

10. Slicing a String with a Step Value
   - **Source example:** Input: "Vcube Solution" · Output: "VBsun"

11. Concatenating Lists by using slicing.

12. Remove Duplicates from a list using slicing.
   - **Source example:** Input: [1,2,3,1,4,5,2] · Output: [1,2,3,4,5]

13. Write a python program to reverse the order of words in a given string by slicing and joining.
   - **Source example:** Input: "Python" · Output: "nohtyP"

14. Flattening Nested Lists by using slicing.

15. Finding the Maximum Value in a given list by slicing.
   - **Source example:** Input: [10,11,12,13,14,15] · Output: 15

16. Write a python program that count the number of occurrences of substring in string by slicing
   - **Source example:** Input: "Raja" · substring: "aja" · Output: 1

17. Given a string s , determine if it is a palindrome by slicing and checking.

18. Given two dictionaries 'dict1' and 'dict2', merge them together by slicing and combining
   - **Source example:** Example · Input: dict1 = {'a':1,'b':2,'c':3}, dict2 = {'x':10,'y':20,'z':30}, keys1 = ['a','b'], keys2 = ['y','z'] · Output: {'a':1,'b':2,'y':20,'z':30}


# FUNCTIONS AND ADVANCED PARADIGMS


## Functions

1. Can you provide a simple function in Python without arguments and a return statement?

2. How would you define a function with parameters in Python? Can you give an example?

3. How can you create a function with a default parameter in Python? Can you provide an example?

4. How would you write a function with a docstring in Python? Can you show an example?


## Scope

1. Can you provide an example to demonstrate local scope in Python?

2. How would you demonstrate enclosing scope in Python with an example?

3. Can you give an example to illustrate global scope in Python?

4. How can you show built-in scope with an example in Python?


## Modifying and Accessing Variables

1. How would you modify a global variable from within a function in Python? Can you provide an example?

2. Can you show how to access a global variable from within a function in Python?

3. How can you modify a nonlocal variable in a nested function in Python? Can you give an example?

4. How would you access a nonlocal variable in a nested function in Python? Can you provide an example?


## Lambda Functions

1. Can you provide a lambda function to square a number in Python?

2. How can you create a lambda function to add two numbers in Python? Can you give an example?

3. How would you write a lambda function to find the maximum of two numbers in Python? Can you give an example?

4. How can you create a lambda function to check if a number is even in Python? Can you provide an example?

5. Can you demonstrate a lambda function to extract the last character from a string in Python?

6. How would you write a lambda function to sort a list of tuples based on the second element in Python? Can you provide an example?

7. How can you create a lambda function to filter even numbers from a list in Python? Can you give an example?

8. Can you provide a lambda function with a conditional expression to categorize ages in Python?

9. How can you write a lambda function to calculate the factorial of a number using recursion in Python? Can you demonstrate this with an example?


## Use Cases for Lambda Functions

1. How would you filter even numbers from a list in Python? Can you give an example?

2. How can you calculate the square of numbers in a list in Python? Can you demonstrate this with an example?

3. How would you create a simple calculator in Python? Can you provide an example?

4. How can you use lambda with the sorted function for custom sorting in Python? Can you show an example?

5. How can you combine lists element-wise in Python? Can you demonstrate this with an example?

6. How would you remove duplicates from a list in Python? Can you give an example?


## Recursion

1. Write a Python function to calculate the factorial of a given number using recursion.

2. Write a Python function to generate the nth Fibonacci number using recursion.

3. Write a Python function to calculate the sum of digits of a given number using recursive functions.

4. Print the Pattern by using recursive Function
   - **Source example:** n=5 · Output: 54321012345

5. Find the sum of the elements in the given list by using recursive Function
   - **Source example:** L = [1,2,3,4,5,6] · Output: 21

6. Convert nested list into single list by using recursive function
   - **Source example:** L = [[1,2,3],4,[5],[6,7,8,9],10] · Output: [1,2,3,4,5,6,7,8,9,10]

7. Check the given number is Prime or not by using recursive function
   - **Source example:** Input: 5 · Output: Prime number

8. Print n even numbers by using recursive Function
   - **Source example:** Input: 5 · Output: 0,2,4,6,8

9. Print n odd numbers by using recursive Function
   - **Source example:** Input: 5 · Output: 1,3,5,7,9

10. Find the Sum of the given number by using recursive Function
   - **Source example:** Input: 12345 · Output: 15


## Stack Overflow and Tail Recursion

1. How would you implement basic tail recursion in Python?

2. Can you provide an example of a stack overflow occurring without optimization in Python?

3. How do you optimize tail recursion with an accumulator in Python? Can you show an example?

4. Can you demonstrate the calculation of the Fibonacci sequence without optimization in Python?

5. How can a stack overflow occur in a deep recursive function in Python? Can you provide an example?

6. How would you implement tail recursion in the calculation of a factorial in Python?


## Default Arguments

1. How do you define a function with a default argument in Python?

2. How can you define a function with multiple default arguments in Python?

3. How do you handle default arguments with lists in Python?

4. How do you use None as a default argument in Python to avoid issues with mutable default arguments?


## Keyword Arguments

1. Can you provide an example of basic keyword argument usage in Python?

2. How do you use keyword arguments with default values in Python? Can you give an example?

3. Can you demonstrate keyword arguments with input validation in Python?

4. How would you use keyword arguments for file I/O operations in Python?

5. Can you show an example of a function that uses keyword arguments with multiple parameters in Python?


## Variable-Length Keyword Arguments (**kwargs)

1. How do you use **kwargs in Python, and can you provide a simple example?

2. Can you demonstrate how to calculate an average using **kwargs in Python?

3. How would you create a configurable function using **kwargs in Python?

4. Can you provide an example of an HTML element generator using **kwargs in Python?

5. Use *args and **kwargs together to support flexible positional and keyword arguments.


## Higher-Order Functions

1. Can you provide an example of using functions as arguments in Python?

2. How can functions be used as return values in Python? Can you provide an example?

3. How can functions be stored in data structures in Python? Can you give an example?

4. How are functions used as decorators in Python? Can you demonstrate this with an example?

5. Can you provide an example of using a basic function as an argument in Python?

6. How would you use functions for data transformation in Python? Can you give an example?

7. Can you demonstrate using a function for sorting in Python?

8. How can you return a function in Python to perform arithmetic operations?

9. Can you provide an example of returning a function in Python to filter a list?

10. How would you use a function to generate a sequence in Python and return it?

11. How can you square all elements in a list in Python?

12. Can you demonstrate how to convert a list of strings to uppercase in Python?

13. How would you filter even numbers from a list in Python? Can you provide an example with input and output?

14. Can you demonstrate how to filter names with more than 5 characters from a list in Python? Please provide an example with input and output.

15. How can you create a custom higher-order function in Python to apply a function to elements greater than a threshold in a list? Can you provide an example with input and output?

16. Use functools.reduce() to calculate the cumulative product or cumulative sum of a sequence.


## Decorators

1. How do you create a basic decorator in Python?

2. How can you create a decorator with arguments in Python?

3. How would you create a timing decorator in Python?

4. How can you create a logging decorator in Python?

5. How do you implement a memoization decorator (caching) in Python?

6. Logging Decorator: This decorator logs the input arguments and the return value of a function.

7. Timing Decorator: This decorator measures the time taken by a function to execute.

8. Authorization Decorator: These decorator checks if a user is authorized to access a specific function.

9. Common use cases for decorators (e.g., logging, authentication)

10. How would you create an authentication decorator in Python?

11. Can you demonstrate how to create a caching decorator in Python?

12. How do you implement an error handling decorator in Python?


## Closures

1. How can you define a simple nested function in Python?

2. Can you demonstrate how to return a nested function in Python?

3. How do you use parameters in a nested function in Python?

4. How would you access an outer variable in a nested function in Python?

5. Can you provide an example of modifying an outer variable in a nested function in Python?

6. How do you create a closure in Python?

7. Can you demonstrate a closure with mutable state in Python?


## Call Stack

1. How does a recursive function use the call stack in Python?

2. What happens when a recursive function causes a call stack overflow in Python?


## Generator Functions

1. How do you create a simple generator in Python using the 'yield' statement?

2. Create a generator function using yield to produce an infinite sequence.

3. Create a generator that yields records or values in batches for stream processing.


## Python Standard Library and Built-ins (source heading: Infinite Sequence Generator)

1. Can you explain how Python's standard library functions are used for File I/O with open()?

2. How do you perform mathematical operations using the math module in Python?

3. Can you demonstrate how to work with Date and Time using the datetime module in Python?

4. How would you work with JSON data using the json module in Python?

5. How can you use the re module in Python for working with Regular Expressions?

6. What are some commonly used built-in functions in Python, such as len(), range(), zip(), and input()?

7. How does the range() function generate a range of numbers in Python?

8. How do you demonstrate how to combine lists using the zip() function in Python?

9. How do you use the sum() function to calculate the sum of elements in a list in Python?

10. How do you use the input() function to get user input in Python?


## Custom Function Libraries and Modules

1. How do you create and use custom function libraries or modules in Python?

2. Can you provide examples of custom function libraries for Math Operations, Data Processing, and File Handling?

3. Can you explain the process of packaging and distributing functions via PyPI (Python Package Index) in Python?


# OBJECT-ORIENTED PROGRAMMING (OOP)


## Classes and Objects

1. Create a class Rectangle that calculates the area and perimeter of a rectangle.

2. Create a class Person that stores and displays information about a person's name and age.

3. Create a class Calculator that performs basic arithmetic operations: addition, subtraction, multiplication, and division.

4. Create a class Circle that calculates the area and circumference of a circle.

5. Create a class Student that represents a student's information, including name, roll number, and marks in subjects. Calculate the average marks and display the student's details.

6. Create a class BankAccount that represents a simple bank account. Implement methods for deposit, withdrawal, and checking the account balance.

7. Create a class Car that simulates a car with attributes like make, model, and current speed. Implement methods to accelerate and brake the car.

8. Create a class Book that represents a book with attributes like title, author, and publication year. Implement a method to display book details.

9. Create a class Employee to represent employee information, including name, employee ID, and salary. Implement a method to give a salary raise and display employee details.

10. Create a class Bank that represents a bank with attributes like name and location. Implement methods to add and display account holders' names.

11. Create a class Shop that represents an online shop. Implement methods for adding products to the shop and displaying the list of available products.


## Inheritance

1. Create a base class Animal that has a method sound. Extend this class with subclasses Dog and Cat where both provide their specific implementations for the sound they make.

2. Develop a base class Vehicle with a method type_of_vehicle. Extend this class with subclasses Bike and Car, and provide specific types for each vehicle.

3. Design a base class Fruit with an attribute taste. Extend this class with subclasses Apple and Orange, setting their specific taste in the constructors.

4. Create a base class Bird that has a method fly. Extend this class with subclasses Sparrow and Ostrich. Sparrow can fly, while Ostrich cannot.

5. Develop a base class Shape with a method area. Extend this class with subclasses Square and Circle. The subclasses should override this method to calculate the specific areas based on their attributes.

6. Design a base class Person with attributes name and age. Extend this class with subclasses Student and Teacher. The Student class should have an additional attribute grade, and the Teacher class should have attributes subject and salary.

7. Design a class hierarchy for a university system. Begin with a base class UniversityMember with attributes name and id_number. Extend this class with subclasses Student and Professor. The Student class should have additional attributes like major and year, while the Professor class should have department and publications.

8. Create a banking system. Start with a base class Account with methods deposit, withdraw, and balance. Extend this class with subclasses SavingsAccount and CheckingAccount. SavingsAccount should have an added interest rate, while CheckingAccount may have an overdraft limit.

9. Develop a system to manage products in a store. Design a base class Product with attributes name and price. Extend this class with DiscountedProduct, which should apply a discount percentage to the product's price.

10. Design a class hierarchy for a transportation system. Create a base class Vehicle with attributes make and model, and methods start and stop. Extend this class with subclasses Car and Boat. The Car class should have an additional method honk, while the Boat class should have a method anchor.

11. Develop a system to manage different types of employees in a company. Start with a base class Employee with attributes name and salary, and a method display_salary. Extend this class with subclasses Manager and Intern. A Manager has an additional bonus to their salary, while an Intern has a stipend instead of a regular salary.

12. Design an e-commerce system with product ratings and reviews. Start with a class Product with attributes name and price. Extend this class with RatedProduct, which has attributes to keep track of average rating and reviews.

13. Design a class hierarchy for a zoo. Create a base class Animal with attributes name, age, and methods sound and eat. Extend this class with two subclasses Mammal and Bird. Further extend Mammal with Lion and Dolphin and extend Bird with Eagle and Penguin. Each subclass should provide its specific implementation for the sound it makes.


## Abstraction

1. Create a class Smartphone that abstracts the idea of a smartphone. It should have methods to call, text, and browse but will not have the internal workings of these methods defined. Extend this class with a specific implementation of the smartphone brand (e.g., iPhone) that implements the methods.

2. Design an abstract class Vehicle that represents general vehicles. It should have methods to start_engine, stop_engine, and drive. Then, implement a class Car that inherits from Vehicle and provides a concrete implementation for these methods.

3. Design an abstract class Appliance that represents general household appliances. This class should have methods turn_on and turn_off. Extend this class with two specific appliances: Refrigerator and Fan, implementing the methods.

4. Design an abstract class Instrument that represents musical instruments. It should have a method play. Implement two specific instruments: Guitar and Drum, providing specific sounds when played.

5. Create an abstract class Document that represents written documents. It should have methods read and write. Implement two specific types of documents: Letter and Report, and give specific implementations for reading.

6. Design an abstract class Payment that outlines the structure for making payments. It should have methods authorize, pay, and refund. Now, implement two specific payment methods: CreditCard and PayPal, each having its specific way of handling the payment operations.

7. Develop an abstract class Shape that represents geometric shapes. It should have methods area and perimeter. Implement two specific shapes: Rectangle and Circle, providing calculations for area and perimeter for each.

8. Develop an abstract class NotificationService representing a service to send notifications. It should have methods authenticate, send, and logout. Implement two specific services: EmailService and SMSService, which use different protocols for sending notifications.

9. Design an abstract class EcommercePlatform which defines a blueprint for an e-commerce system. The class should have abstract methods for list_product, add_to_cart, checkout, and make_payment. Implement two subclasses Shopify and Magento, providing specific implementations for these methods.

10. Develop an abstract class SocialMediaPlatform that outlines functionalities for a social media service. The class should have abstract methods for post_content, comment, like, and share. Implement subclasses Facebook and Twitter with distinct ways of handling these operations.

11. Design an abstract class GamingPlatform that simulates the operations of a gaming console. It should have methods for load_game, play, save_game, and shutdown. Now, simulate two platforms: PlayBox and GameSphere, each having unique ways of executing these operations.

12. Develop an abstract class StreamingService representing online media streaming. The class should have methods for login, search_content, stream, and logout. Now, create two specific platforms: Netflix and YouTube, implementing unique behaviors.

13. Create an abstract class MusicPlayer that simulates basic operations for playing audio. The class should have methods for play_song, pause, next_track, and previous_track. Develop two specific audio platforms: SpotifyPlayer and AppleMusicPlayer that have distinct behaviors for these operations.

14. Construct an abstract class VehicleControlSystem simulating a vehicle's control system. The class should have methods for start_engine, stop_engine, turn_on_headlights, and play_radio. Create two subclasses CarControlSystem and MotorbikeControlSystem that represent their specific control behaviors.

15. Create an abstract Payment base class with authorize(), pay(), and refund() methods, then implement the methods in CreditCard and PayPal subclasses.


## Polymorphism

1. Define two classes, Rectangle and Circle. Both classes should have a method area that calculates and returns their respective areas. Create objects of these classes and add them to a list. Iterate over this list to print the area for each shape.

2. Create classes Car and Bike. Both should have a method num_of_wheels that returns the number of wheels they have. Instantiate objects from these classes, add them to a list, and then iterate over this list to print the number of wheels each vehicle has.

3. Design a system with a base class Vehicle that has a method capacity. Extend this class into two subclasses: Bus and Car. While Bus can carry multiple passengers, Car is meant for fewer passengers. Instantiate objects of these classes, add them to a list, and loop over this list to display the capacity of each vehicle.

4. Construct a class hierarchy for animals with a base class Animal. This class should have a method diet which returns the general diet of the animal. Extend this class with two subclasses: Carnivore and Herbivore. Further, extend Carnivore with a class Tiger and Herbivore with a class Cow. Instantiate objects and display their diets.

5. Design a system where you have a base class Instrument that has a method sound. Extend this class with three subclasses: Guitar, Piano, and Drums. Each subclass should provide its own implementation for the sound method. Instantiate objects of these subclasses, add them to a list, and loop over this list to play the sound of each instrument.

6. Design a class hierarchy for electronic devices. Create a base class Device with a method purpose. Extend this with ComputingDevice and CommunicationDevice. Further extend ComputingDevice with Laptop and Desktop, and CommunicationDevice with MobilePhone and Landline. Instantiate these and display their purposes.

7. Create a simulation of geometric transformations on shapes. Start with a base class Shape with methods translate and scale. Extend this with Circle and Rectangle. Both subclasses should have their own methods to modify the position or dimensions, influenced by the base class’s transformations.

8. Design a class hierarchy for different payment methods in an e-commerce system. Begin with a base class Payment with methods authorize and charge. Extend this with CreditCard, DebitCard, and PayPal. Each subclass should implement authorization and charging uniquely. Instantiate these classes and demonstrate a payment flow.

9. Create a list of Shape objects (such as Circle and Square) and iterate through it, calling each object’s area method to demonstrate polymorphism.


## Method Overriding and Operator Overloading

1. Design a base class Shape with a method area that returns 0. Create two subclasses, Circle and Square, and override the area method to return the appropriate area for each shape.

2. Design a base class Animal with a method sound that returns "Animal makes a sound". Develop two subclasses, Dog and Cat, and override the sound method to produce the sound each animal generates.

3. Construct a base class Vehicle with a method description that returns "This is a vehicle". Generate two subclasses, Car and Bike, and override the description method to return more specific descriptions for each type of vehicle.

4. Design a base class Bird with a method fly that returns "A bird can fly". Create two subclasses, Ostrich and Penguin, and override the fly method for these birds since they cannot fly.

5. Design a base class Device with a method power_on that returns "Device is powering on". Construct two subclasses, Laptop and Smartphone, and override the power_on method to give a customized power-on message for each device.

6. Create a class BankAccount with methods deposit, withdraw, and get_balance. The get_balance method should simply return the balance. Now, derive a subclass InterestAccount that overrides the get_balance method to include interest on the balance.

7. Build a class OnlineGame with methods start_game and end_game. The start_game method should return "Starting online game..." and end_game should return "Ending online game...". Derive a subclass BattleRoyaleGame that overrides the start_game method to specify that players are joining a battle royale match.

8. Establish a class Vehicle with a method fuel_up that returns "Fueling up vehicle...". Create a subclass ElectricCar that overrides the fuel_up method to indicate that the vehicle is charging its battery.

9. Develop a class Document with a method save that saves the document. Now, derive a subclass EncryptedDocument that overrides the save method. The overridden method should first encrypt the content before saving.

10. Design a class ECommerceSite with methods add_to_cart, remove_from_cart, and checkout. Now, derive a subclass PremiumECommerceSite which overrides the checkout method. In the overridden method, apply a discount for premium users before proceeding to checkout.

11. Design a class StringManipulator that holds a string. Overload the / operator such that it splits the string by another string passed to it.

12. Create a class Polygon that represents a polygon through a list of (x, y) coordinates. Overload the & operator to find the intersection of two polygons.

13. Design a class SafeList that extends the behavior of a regular list but overloads the [] operator (using getitem and setitem). When trying to access an index out of range, it should print an error message instead of throwing an exception.

14. Design a class Currency that represents a specific amount of money in a given currency (e.g., USD, EUR). Overload the + and - operators to allow operations between instances of the same currency. If an operation is attempted between different currencies, print an error message.


## Static Methods

1. Design a class TemperatureConverter that has static methods to convert temperatures between Celsius and Fahrenheit.

2. Create a class StringAnalyzer that has a static method to check if a given string is a palindrome (ignores cases, spaces, and punctuation).

3. Construct a class Calculator with static methods to perform basic arithmetic operations: addition, subtraction, multiplication, and division.

4. Design a class DateValidator that has a static method to check if a given date in the format YYYY-MM-DD is valid or not.

5. Create a class NumberUtility that provides a static method to determine if a number is even or odd.

6. Design a class FileUtility that provides static methods to read and write to a file. The write method should append to a file if it exists or create a new one otherwise.

7. Construct a class Fibonacci that offers a static method to generate the Fibonacci sequence up to a given number or for a given number of terms.

8. Design a class Geometry that offers static methods to calculate the area of different geometric shapes like a circle, rectangle, and triangle.

9. Develop a class DateOperations that provides static methods to determine the number of days between two dates without using any external libraries. (Assume each month has 30 days for simplicity).

10. Design a class BaseConverter that provides a static method to convert numbers from one base to another (between bases 2 and 16).

11. Construct a class BigIntegerOperations that provides a static method to compute the greatest common divisor (GCD) of two large integers represented as strings.


## Property Decorators

1. Design a class Circle that has a private radius. Use property decorators to create getter and setter methods for the radius, ensuring the radius cannot be set to a negative value.

2. Design a class BankAccount that has a private balance attribute. Use property decorators to create a getter for the balance, ensuring that it cannot be set directly but only modified through methods like deposit and withdraw.

3. Design a class Temperature that maintains a temperature in Celsius. Use property decorators to get and set temperatures in Fahrenheit, ensuring proper conversion between Celsius and Fahrenheit.

4. Design a class Employee with private attributes: salary and _bonus. The bonus cannot exceed 20% of the salary. Use property decorators to control access and modifications to these attributes.

5. Design a class Square that has a side attribute. Also, make properties for area and perimeter of the square. Ensure that when the side of the square is set, the area and perimeter change accordingly.

6. Design a class BankAccount where the balance cannot go below a minimum balance. If a withdrawal request would make the balance go below this limit, it should be denied.

7. Design a class Smartphone with attributes _storage_used and _total_storage. Implement properties to get available storage and storage used as percentages.


## Encapsulation

1. Design a class BankAccount that has a private balance. Implement methods to deposit, withdraw, and check balance. Ensure the balance never goes negative.

2. Create a class Student with private attributes for name and age. Implement public methods to get and set the name and age, ensuring age is between 5 and 25.

3. Design a class Laptop that has a private attribute for battery life (in percentage). Create methods to charge the laptop and use it, ensuring the battery percentage stays between 0 and 100.

4. Design a class SafeList that extends Python’s list. This class should override the append method to ensure that only integer values can be added to the list.

5. Design a class UserProfile that has private attributes for username and password. Implement methods to get and set the username and password. Password setting should ensure that it’s at least 8 characters long.

6. Develop a class Library that manages books. It should have private lists for available and issued books. Implement methods to issue, return, and check the status of a book.

7. Design a class LimitedSizeList that behaves like a list but has a maximum size. If elements are added beyond this size, the oldest elements should be removed to maintain the size limit.

8. Design a class PrivateAttributes that uses name mangling to keep all its attributes private. It should also override the default behavior of the dir() function to hide private attributes.

9. Create a class with private __balance and __password attributes and expose controlled access through @property getters and setters.


# SUPPLEMENTARY EXECUTION REFERENCES

The following examples were supplied in the conditional-statement reference documents. They are kept separate from the question inventory to avoid repeating the same question text. Match each example to the question with the same title. Exact thresholds or outputs are retained as shown in the source.

## Best Seller Tag Display

**Sample input 1**
```text
Input: 1200
```

**Expected output 1**
```text
Best Seller
```

**Sample input 2**
```text
Input: 800
```

**Expected output 2**
```text
No Output
```

## Instagram Verification Status

**Sample input 1**
```text
Eligible Account: True
Meta Verified Subscription: True
```

**Expected output 1**
```text
Verified Badge Granted
```

**Sample input 2**
```text
Eligible Account: True
Meta Verified Subscription: False
```

**Expected output 2**
```text
None
```

## Zepto Rain Delivery Charges

**Sample input 1**
```text
Input: True
```

**Expected output 1**
```text
Extra Rain Charges Applied
```

**Sample input 2**
```text
Input: False
```

**Expected output 2**
```text
No Output
```

## Username and Password Login

**Sample input 1**
```text
Username: admin
Password: admin123
```

**Expected output 1**
```text
Login Successful
```

**Sample input 2**
```text
Username: admin
Password: test123
```

**Expected output 2**
```text
Invalid Credentials
```

## Product Search

**Sample input 1**
```text
Available Products: Laptop, Mobile, Watch
Search Product: Mobile
```

**Expected output 1**
```text
Product Found
```

**Sample input 2**
```text
Available Products: Laptop, Mobile, Watch
Search Product: TV
```

**Expected output 2**
```text
Product Not Found
```

## Delivery Charge Calculation

**Sample input 1**
```text
Input: 150
```

**Expected output 1**
```text
Final Bill Amount: 150
```

**Sample input 2**
```text
Input: 80
```

**Expected output 2**
```text
Final Bill Amount: 110
```

## Weekend Planner Based on Budget

**Sample input 1**
```text
Input: 12000
```

**Expected output 1**
```text
Plan: Trip
```

**Sample input 2**
```text
Input: 5000
```

**Expected output 2**
```text
Plan: Movie and Dinner
```

**Sample input 3**
```text
Input: 1000
```

**Expected output 3**
```text
Plan: Stay Home
```

## Greeting Based on Current Hour

**Sample input 1**
```text
Input: 8
```

**Expected output 1**
```text
Good Morning
```

**Sample input 2**
```text
Input: 15
```

**Expected output 2**
```text
Good Afternoon
```

**Sample input 3**
```text
Input: 22
```

**Expected output 3**
```text
Good Night
```

## Hosting Plan Based on Budget

**Sample input 1**
```text
Input: 15000
```

**Expected output 1**
```text
Cloud Hosting
```

**Sample input 2**
```text
Input: 7000
```

**Expected output 2**
```text
Business Hosting
```

**Sample input 3**
```text
Input: 3000
```

**Expected output 3**
```text
Premium Hosting
```

**Sample input 4**
```text
Input: 999
```

**Expected output 4**
```text
Single Hosting
```

## Instagram Story Visibility

**Sample input 1**
```text
Follows Account: True
Close Friend: True
```

**Expected output 1**
```text
Story Visible
```

**Sample input 2**
```text
Follows Account: True
Close Friend: False
```

**Expected output 2**
```text
Not in Close Friends List
```

**Sample input 3**
```text
Follows Account: False
Close Friend: False
```

**Expected output 3**
```text
Follow the Account First
```

## BGMI Tournament Entry

**Sample input 1**
```text
Registered: True
Fee Paid: True
```

**Expected output 1**
```text
Tournament Entry Confirmed
```

**Sample input 2**
```text
Registered: True
Fee Paid: False
```

**Expected output 2**
```text
Entry Fee Pending
```

**Sample input 3**
```text
Registered: False
Fee Paid: False
```

**Expected output 3**
```text
Registration Required
```

## Google Drive File Access

**Sample input 1**
```text
Link Active: True
Permission Granted: True
```

**Expected output 1**
```text
File Opened Successfully
```

**Sample input 2**
```text
Link Active: True
Permission Granted: False
```

**Expected output 2**
```text
Access Denied
```

**Sample input 3**
```text
Link Active: False
Permission Granted: False
```

**Expected output 3**
```text
Invalid File Link
```

## Basic if / if-else examples from the introductory worksheet

### Check Whether a Number is Positive

**Sample input 1**
```text
10
```

**Expected output 1**
```text
Positive Number
```

**Sample input 2**
```text
-8
```

**Expected output 2**
```text
(No Output)
```

### Check Whether a String is Empty

**Sample input 1**
```text
(Empty input)
```

**Expected output 1**
```text
String is Empty
```

**Sample input 2**
```text
Python
```

**Expected output 2**
```text
(No Output)
```

### Check Positive, Negative, or Zero (Using Only if Statements)

**Sample input 1**
```text
25
```

**Expected output 1**
```text
Positive
```

**Sample input 2**
```text
0
```

**Expected output 2**
```text
Zero
```

### Check Whether a Number is a Multiple of Both 3 and 5

**Sample input 1**
```text
45
```

**Expected output 1**
```text
Multiple of 3 and 5
```

**Sample input 2**
```text
18
```

**Expected output 2**
```text
(No Output)
```

### Check Whether a Number is a Perfect Square

**Sample input 1**
```text
49
```

**Expected output 1**
```text
Perfect Square
```

**Sample input 2**
```text
50
```

**Expected output 2**
```text
(No Output)
```

### Check Whether a Number is Divisible by Both 2 and 3

**Sample input 1**
```text
24
```

**Expected output 1**
```text
Divisible by 2 and 3
```

**Sample input 2**
```text
14
```

**Expected output 2**
```text
(No Output)
```

### Check Whether a Number is a Perfect Cube

**Sample input 1**
```text
64
```

**Expected output 1**
```text
Perfect Cube
```

**Sample input 2**
```text
30
```

**Expected output 2**
```text
(No Output)
```

### Check Whether a Number is a Multiple of 4

**Sample input 1**
```text
28
```

**Expected output 1**
```text
Multiple of 4
```

**Sample input 2**
```text
15
```

**Expected output 2**
```text
(No Output)

🔹 If–Else Statement Practice Questions
```

### Check Whether a Year is a Leap Year

**Sample input 1**
```text
2024
```

**Expected output 1**
```text
Leap Year
```

**Sample input 2**
```text
2023
```

**Expected output 2**
```text
Not a Leap Year
```

### Check Whether a Character is a Vowel or Consonant

**Sample input 1**
```text
A
```

**Expected output 1**
```text
Vowel
```

**Sample input 2**
```text
k
```

**Expected output 2**
```text
Consonant
```

### Check Whether a Year is a Century Year

**Sample input 1**
```text
2000
```

**Expected output 1**
```text
Century Year
```

**Sample input 2**
```text
2025
```

**Expected output 2**
```text
Not a Century Year
```

### Check Whether a Number is Prime

**Sample input 1**
```text
17
```

**Expected output 1**
```text
Prime
```

**Sample input 2**
```text
20
```

**Expected output 2**
```text
Not Prime
```

### Check Voting Eligibility

**Sample input 1**
```text
20
```

**Expected output 1**
```text
Eligible
```

**Sample input 2**
```text
16
```

**Expected output 2**
```text
Not Eligible
```

### Check Whether a Number is Positive or Non-Positive

**Sample input 1**
```text
9
```

**Expected output 1**
```text
Positive
```

**Sample input 2**
```text
0
```

**Expected output 2**
```text
Non-Positive
```

### Compare Two Numbers

**Sample input 1**
```text
25
18
```

**Expected output 1**
```text
25
```

**Sample input 2**
```text
10
50
```

**Expected output 2**
```text
50
```

### Check Whether a Character is a Letter

**Sample input 1**
```text
Z
```

**Expected output 1**
```text
Letter
```

**Sample input 2**
```text
7
```

**Expected output 2**
```text
Not a Letter
```

### Find the Smallest of Three Numbers

**Sample input 1**
```text
12
5
18
```

**Expected output 1**
```text
5
```

**Sample input 2**
```text
25
30
10
```

**Expected output 2**
```text
10
```

### Check Whether a String is a Palindrome

**Sample input 1**
```text
madam
```

**Expected output 1**
```text
Palindrome
```

**Sample input 2**
```text
hello
```

**Expected output 2**
```text
Not Palindrome
```

### Find the Largest of Four Numbers

**Sample input 1**
```text
15
8
22
10
```

**Expected output 1**
```text
22
```

**Sample input 2**
```text
40
12
28
35
```

**Expected output 2**
```text
40
```

### Determine the Sign of the Difference of Two Numbers

**Sample input 1**
```text
20
10
```

**Expected output 1**
```text
Positive
```

**Sample input 2**
```text
15
25
```

**Expected output 2**
```text
Negative
```

### Check Leap Year (Alternative Method)

**Sample input 1**
```text
2000
```

**Expected output 1**
```text
Leap Year
```

**Sample input 2**
```text
1900
```

**Expected output 2**
```text
Not a Leap Year
```

### Check Whether a Number is a Multiple of 7

**Sample input 1**
```text
49
```

**Expected output 1**
```text
Multiple of 7
```

**Sample input 2**
```text
30
```

**Expected output 2**
```text
Not a Multiple of 7
```

### Find the Absolute Value of a Number

**Sample input 1**
```text
18
```

**Expected output 1**
```text
18
```

**Sample input 2**
```text
-27
```

**Expected output 2**
```text
27
```

## Additional conditional-statement examples from the detailed worksheet

### Celsius ↔ Fahrenheit Conversion

**Sample input 1**
```text
Enter conversion: C to F
Enter temperature: 25
```

**Expected output 1**
```text
Temperature in Fahrenheit: 77.0
```

**Sample input 2**
```text
Enter conversion: F to C
Enter temperature: 98.6
```

**Expected output 2**
```text
Temperature in Celsius: 37.0
```

### Simple Calculator

**Sample input 1**
```text
Enter first number: 20
Enter second number: 5
Enter operation: +
```

**Expected output 1**
```text
Result: 25
```

**Sample input 2**
```text
Enter first number: 20
Enter second number: 5
Enter operation: /
```

**Expected output 2**
```text
Result: 4.0
```

**Sample input 3**
```text
Enter first number: 15
Enter second number: 3
Enter operation: *
```

**Expected output 3**
```text
Result: 45
```

**Sample input 4**
```text
Enter first number: 15
Enter second number: 3
Enter operation: -
```

**Expected output 4**
```text
Result: 12
```

### Guess the Number Game

**Sample input 1**
```text
Guess the number: 7
```

**Expected output 1**
```text
Congratulations! You guessed the number.
```

**Sample input 2**
```text
Guess the number: 5
```

**Expected output 2**
```text
Wrong guess. Try again.
```

### Password Strength

**Sample input 1**
```text
Enter password: Python123
```

**Expected output 1**
```text
Strong password
```

**Sample input 2**
```text
Enter password: python
```

**Expected output 2**
```text
Weak password
```

### Discount Based on Purchase Amount

**Sample input 1**
```text
Enter purchase amount: 5000
```

**Expected output 1**
```text
Discount: 20%
Final price: 4000.0
```

**Sample input 2**
```text
Enter purchase amount: 1000
```

**Expected output 2**
```text
Discount: 10%
Final price: 900.0
```

### ATM Machine

**Sample input 1**
```text
Enter choice: balance
```

**Expected output 1**
```text
Your balance is: 10000
```

**Sample input 2**
```text
Enter choice: withdraw
Enter amount: 3000
```

**Expected output 2**
```text
Withdrawal successful
Remaining balance: 7000
```

### Greeting Based on Time

**Sample input 1**
```text
Enter hour: 9
```

**Expected output 1**
```text
Good Morning
```

**Sample input 2**
```text
Enter hour: 20
```

**Expected output 2**
```text
Good Evening
```

### Discount Coupon Code

**Sample input 1**
```text
Enter price: 2000
Enter coupon code: SAVE20
```

**Expected output 1**
```text
Discount: 20%
Final price: 1600.0
```

**Sample input 2**
```text
Enter price: 2000
Enter coupon code: INVALID
```

**Expected output 2**
```text
Invalid coupon code
Final price: 2000
```

### Grade Based on Score

**Sample input 1**
```text
Enter score: 85
```

**Expected output 1**
```text
Grade: A
```

**Sample input 2**
```text
Enter score: 110
```

**Expected output 2**
```text
Invalid score
```

### Number of Days in a Month

**Sample input 1**
```text
Enter month number: 2
```

**Expected output 1**
```text
Number of days: 28
```

**Sample input 2**
```text
Enter month number: 4
```

**Expected output 2**
```text
Number of days: 30
```

### BMI Category

**Sample input 1**
```text
Enter weight in kg: 50
Enter height in meters: 1.70
```

**Expected output 1**
```text
BMI: 17.3
Category: Underweight
```

**Sample input 2**
```text
Enter weight in kg: 80
Enter height in meters: 1.70
```

**Expected output 2**
```text
BMI: 27.68
Category: Overweight
```

### Letter Grade to GPA

**Sample input 1**
```text
Enter grade: A
```

**Expected output 1**
```text
GPA: 4.0
```

**Sample input 2**
```text
Enter grade: C
```

**Expected output 2**
```text
GPA: 2.0

NESTED IF STATEMENT
```

### Compare x and y

**Sample input 1**
```text
x = 10
y = 5
```

**Expected output 1**
```text
x is greater than y
x is not greater than 15
```

**Sample input 2**
```text
x = 20
y = 5
```

**Expected output 2**
```text
x is greater than y
x is also greater than 15
```

### Grade and Pass/Fail

**Sample input 1**
```text
Enter grade: 85
```

**Expected output 1**
```text
Letter grade: A
```

**Sample input 2**
```text
Enter grade: 60
```

**Expected output 2**
```text
Letter grade: D
You failed.
```

### Credit Card Eligibility

**Sample input 1**
```text
Enter age: 20
Enter income: 40000
```

**Expected output 1**
```text
You are eligible for a credit card.
```

**Sample input 2**
```text
Enter age: 20
Enter income: 25000
```

**Expected output 2**
```text
Your income is too low for a credit card.
```

### Even/Odd and Greater Than 10

**Sample input 1**
```text
Enter number: 20
```

**Expected output 1**
```text
20 is even
20 is greater than 10
```

**Sample input 2**
```text
Enter number: 7
```

**Expected output 2**
```text
7 is odd
```

### Theme Park Ticket Price

**Sample input 1**
```text
Enter age: 10
Enter height: 3.5
```

**Expected output 1**
```text
Ticket price: $10
```

**Sample input 2**
```text
Enter age: 15
Enter height: 5
```

**Expected output 2**
```text
Ticket price: $20
```

### User Authentication

**Sample input 1**
```text
Enter username: admin
Enter password: 1234
```

**Expected output 1**
```text
Access granted.
```

**Sample input 2**
```text
Enter username: admin
Enter password: 9999
```

**Expected output 2**
```text
Incorrect password.
```

### Food Ordering

**Sample input 1**
```text
Enter food: Burger
Do you want fries? yes
```

**Expected output 1**
```text
Your order: Burger with Fries
```

**Sample input 2**
```text
Enter food: Pizza
Do you want extra cheese? yes
```

**Expected output 2**
```text
Your order: Pizza with Extra Cheese
```

### Positive/Negative/Zero and Even/Odd

**Sample input 1**
```text
Enter number: 20
```

**Expected output 1**
```text
Positive
Even
```

**Sample input 2**
```text
Enter number: -5
```

**Expected output 2**
```text
Negative
```

### Driving Eligibility

**Sample input 1**
```text
Enter age: 25
Do you have a license? yes
```

**Expected output 1**
```text
You are eligible to drive.
```

**Sample input 2**
```text
Enter age: 25
Do you have a license? no
```

**Expected output 2**
```text
You are not eligible to drive.
```

### Voting Eligibility

**Sample input 1**
```text
Enter age: 25
Are you a citizen? yes
```

**Expected output 1**
```text
You are eligible to vote.
```

**Sample input 2**
```text
Enter age: 25
Are you a citizen? no
```

**Expected output 2**
```text
You are not eligible to vote.
```

### Three Numbers in Ascending Order

**Sample input 1**
```text
Enter first number: 30
Enter second number: 10
Enter third number: 20
```

**Expected output 1**
```text
Ascending order: 10 20 30
```

**Sample input 2**
```text
Enter first number: 5
Enter second number: 2
Enter third number: 8
```

**Expected output 2**
```text
Ascending order: 2 5 8
```

### Store Discount and Membership

**Sample input 1**
```text
Enter purchase amount: 200
Do you have membership? yes
```

**Expected output 1**
```text
Discount: 20%
Final amount: 160.0
```

**Sample input 2**
```text
Enter purchase amount: 200
Do you have membership? no
```

**Expected output 2**
```text
Discount: 10%
Final amount: 180.0
```

### Character Classification

**Sample input 1**
```text
Enter character: a
```

**Expected output 1**
```text
Vowel
```

**Sample input 2**
```text
Enter character: 5
```

**Expected output 2**
```text
Neither
```

### Book Recommendation

**Sample input 1**
```text
Enter age: 15
Enter genre: Fantasy
```

**Expected output 1**
```text
Recommended book: Harry Potter
```

**Sample input 2**
```text
Enter age: 30
Enter genre: Mystery
```

**Expected output 2**
```text
Recommended book: Sherlock Holmes
```

### Movie Ticket Price

**Sample input 1**
```text
Enter age: 10
Is it a matinee show? yes
```

**Expected output 1**
```text
Ticket price: $8
```

**Sample input 2**
```text
Enter age: 30
Is it a matinee show? no
```

**Expected output 2**
```text
Ticket price: $15
```

### Delivery Charges

**Sample input 1**
```text
Enter distance: 3
Enter order amount: 500
```

**Expected output 1**
```text
Delivery charge: $0
```

**Sample input 2**
```text
Enter distance: 10
Enter order amount: 300
```

**Expected output 2**
```text
Delivery charge: $50
```

### Employee Performance and Bonus

**Sample input 1**
```text
Enter performance score: 90
Enter years of service: 5
```

**Expected output 1**
```text
Performance: Excellent
Bonus: 20000
```

**Sample input 2**
```text
Enter performance score: 70
Enter years of service: 2
```

**Expected output 2**
```text
Performance: Good
Bonus: 10000
```

### Library Late Fee

**Sample input 1**
```text
Enter overdue days: 5
Enter book type: regular
```

**Expected output 1**
```text
Late fee: $5
```

**Sample input 2**
```text
Enter overdue days: 5
Enter book type: reference
```

**Expected output 2**
```text
Late fee: $10
```

### Scholarship Eligibility

**Sample input 1**
```text
Enter GPA: 3.8
Enter number of activities: 4
```

**Expected output 1**
```text
Scholarship awarded
```

**Sample input 2**
```text
Enter GPA: 3.2
Enter number of activities: 4
```

**Expected output 2**
```text
Scholarship not awarded
```

### Clothing Recommendation

**Sample input 1**
```text
Enter temperature: 15
Is it raining? yes
```

**Expected output 1**
```text
Wear a jacket and carry an umbrella.
```

**Sample input 2**
```text
Enter temperature: 30
Is it raining? no
```

**Expected output 2**
```text
Wear light clothes.
```

### Movie Recommendation

**Sample input 1**
```text
Enter genre: Comedy
Enter age group: Adult
```

**Expected output 1**
```text
Recommended movie: The Hangover
```

**Sample input 2**
```text
Enter genre: Animation
Enter age group: Child
```

**Expected output 2**
```text
Recommended movie: Toy Story
```

### Credit Card Approval

**Sample input 1**
```text
Enter credit score: 750
Enter income: 60000
```

**Expected output 1**
```text
Credit card application approved
```

**Sample input 2**
```text
Enter credit score: 550
Enter income: 20000
```

**Expected output 2**
```text
Credit card application rejected
```

### Vehicle Registration

**Sample input 1**
```text
Enter vehicle type: car
Enter emissions status: clean
```

**Expected output 1**
```text
Registration fee: $100
```

**Sample input 2**
```text
Enter vehicle type: truck
Enter emissions status: high
```

**Expected output 2**
```text
Registration fee: $300
```

### Nested-if multiple-of-five examples from the source tables

**Example set 1 — expected output table**

| Input | Expected output |
|---:|---|
| 22 | 22 is not a multiple of 5 |
| 7 | 7 is not a multiple of 5 |

**Example set 2 — expected output table**

| Input | Expected output |
|---:|---|
| -25 | -25 is a multiple of 5 |
| 5 | 5 is a multiple of 5 |


# SUPPLEMENTARY FOR-LOOP EXECUTION REFERENCES

Examples below are copied from the introductory loop worksheet. Ellipses in the source output are retained rather than filled in.

## Print numbers from 1 to 5 using a for loop

**Sample input**
```text
No input required
```

**Expected output**
```text
1
2
3
4
5
```

## Print even numbers between 1 and 10

**Sample input**
```text
No input required
```

**Expected output**
```text
2 4 6 8 10
```

## Print multiplication table of a number

**Sample input**
```text
Enter number: 5
```

**Expected output**
```text
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
```

## Print all characters of a string

**Sample input**
```text
Enter string: python
```

**Expected output**
```text
p
y
t
h
o
n
```

## Find sum of digits of a number

**Sample input**
```text
Enter number: 123
```

**Expected output**
```text
Sum = 6
```

## Find the factors of a number

**Sample input**
```text
N = 6
```

**Expected output**
```text
Factors: 1 2 3 6
```

## Reverse a number using a while loop

**Sample input**
```text
Enter number: 456
```

**Expected output**
```text
654
```

## Print factorial of a number

**Sample input**
```text
Enter number: 5
```

**Expected output**
```text
Factorial = 120
```

## Print squares of numbers from 1 to n

**Sample input**
```text
Enter number: 4
```

**Expected output**
```text
1 4 9 16
```

## Check if a number is prime

**Sample input**
```text
Enter number: 7
```

**Expected output**
```text
Prime number
```

## Count vowels in a string

**Sample input**
```text
Enter string: hello
```

**Expected output**
```text
Number of vowels = 2
```


# SOURCE COVERAGE NOTES

- **Primary structure and broad question inventory:** `Coding Questions topic type.docx`.
- **Additional introductory conditional questions and examples:** `if,if-else.docx`.
- **Detailed conditional-statement questions and sample I/O:** `Copy of elif,nested-if STATEMENT.docx`.
- **Scenario-based conditional exercises and test cases:** `Conditional Statement Programs.pdf`.
- **For-loop questions and sample outputs:** `Copy of For Loop_.docx`.
- **While-loop questions and detailed sample I/O:** `While loops Questions.docx`.
- **Original working draft checked for consolidation:** `Python Complete Master Practice Sheet.md`.

**Editorial policy:** Repeated copies of the same question were consolidated. Similar-looking questions were retained when their constraints, technique, data structure, or required behavior differ. No code solutions or answer explanations are included. Examples are only included when they appear in the supplied references; no new test outputs have been invented.
