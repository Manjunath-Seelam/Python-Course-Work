"""
DAY 12
PYTHON ASSIGNMENT SOLUTIONS

This file contains simple solutions for all 10 questions.
Each question is kept as a separate section.
"""

"""
DAY 12 – NESTED LOOPS AND PATTERN PROGRAMMING IN PYTHON

Topics: Introduction to Nested Loops, Nested for Loops, Nested while Loops, Rows and Columns, Star
Patterns, Number Patterns, Alphabet Patterns, Pyramid Patterns, Inverted Patterns and Problem Solving
Using Nested Loops.

Total Questions: 10

BASIC LEVEL – 3 QUESTIONS

1. Square Star Pattern
Question: Write a Python program to accept the number of rows from the user and display a square star
pattern.
For example, if the user enters 5, the output should be:
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
Perform the same task using nested for loops and nested while loops.
Concepts to Use:
• input() function
• int() type conversion
• Nested for loops
• Nested while loops
• range() function
• print() function
• end parameter
"""

rows = int(input("Enter number of rows: "))

if rows > 0:
    print("\nUsing nested for loops:")
    for i in range(rows):
        for j in range(rows):
            print("*", end=" ")
        print()

    print("\nUsing nested while loops:")
    i = 0
    while i < rows:
        j = 0
        while j < rows:
            print("*", end=" ")
            j += 1
        print()
        i += 1
else:
    print("Enter a positive number of rows.")


"""
2. Right-Angled Triangle Star Pattern
Question: Write a Python program to accept the number of rows from the user and print a right-angled
triangle star pattern.
For example, if the user enters 5, the output should be:
*
* *
* * *
* * * *
* * * * *
Display the pattern using nested loops.
Concepts to Use:
• input() function
• int() type conversion
• Nested for loops
• range() function
• Outer loop
• Inner loop
• print() function
• end parameter
"""

rows = int(input("Enter number of rows: "))

if rows > 0:
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end=" ")
        print()
else:
    print("Enter a positive number of rows.")


"""
3. Increasing Number Triangle Pattern
Question: Develop a Python program to accept the number of rows from the user and display an
increasing number triangle.
For example, if the user enters 5, the output should be:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
Display the same pattern using nested for loops and nested while loops.
Concepts to Use:
• input() function
• int() type conversion
• Nested for loops
• Nested while loops
• range() function
• Loop variables
• print() function
• end parameter
"""

rows = int(input("Enter number of rows: "))

if rows > 0:
    print("\nUsing nested for loops:")
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    print("\nUsing nested while loops:")
    i = 1
    while i <= rows:
        j = 1
        while j <= i:
            print(j, end=" ")
            j += 1
        print()
        i += 1
else:
    print("Enter a positive number of rows.")


"""
MEDIUM LEVEL – 3 QUESTIONS

4. Inverted Star Triangle Pattern
Question: Write a Python program to accept the number of rows from the user and print an inverted
right-angled triangle star pattern.
For example, if the user enters 5, the output should be:
* * * * *
* * * *
* * *
* *
*
Display the pattern using nested loops.
Concepts to Use:
• Nested for loops
• range() function
• Reverse iteration
• Outer and inner loop variables
• print() function
• end parameter
"""

rows = int(input("Enter number of rows: "))

if rows > 0:
    for i in range(rows, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()
else:
    print("Enter a positive number of rows.")


"""
5. Number Pyramid Pattern
Question: Develop a Python program to accept the number of rows from the user and display a centered
number pyramid.
For example, if the user enters 5, the output should be:
1
1 2 1
1 2 3 2 1
1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
Ensure that the pyramid is properly aligned.
Concepts to Use:
• Nested for loops
• range() function
• Reverse iteration
• Multiple inner loops
• Arithmetic operators
• String repetition
• print() function
• end parameter
"""

rows = int(input("Enter number of rows: "))

if rows > 0:
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")

        for j in range(1, i + 1):
            print(j, end=" ")

        for j in range(i - 1, 0, -1):
            print(j, end=" ")

        print()
else:
    print("Enter a positive number of rows.")


"""
6. Alphabet Triangle Pattern
Question: Write a Python program to accept the number of rows from the user and display an alphabet
triangle pattern.
For example, if the user enters 5, the output should be:
A
A B
A B C
A B C D
A B C D E
Modify the program to display another pattern where each row starts from the letter A and ends with
the alphabet corresponding to that row.
Concepts to Use:
• Nested for loops
• range() function
• chr() function
• ord() function
• ASCII values
• Character conversion
• print() function
• end parameter
"""

rows = int(input("Enter number of rows (maximum 26): "))

if 1 <= rows <= 26:
    print("\nAlphabet triangle:")
    for i in range(1, rows + 1):
        for j in range(i):
            print(chr(ord("A") + j), end=" ")
        print()

    print("\nRepeated alphabet pattern:")
    for i in range(1, rows + 1):
        letter = chr(ord("A") + i - 1)
        for j in range(i):
            print(letter, end=" ")
        print()
else:
    print("Enter a row count between 1 and 26.")


"""
ADVANCED LEVEL – 4 QUESTIONS

7. Diamond Star Pattern Generator
Question: Develop a Python program to accept an odd number of rows from the user and generate a
diamond-shaped star pattern.
For example, if the user enters 5, the output should be:
*
***
*****
***
*
Extend the program to support different odd row counts.
Display an appropriate error message if the user enters an even number or an invalid row count.
Concepts to Use:
• Nested for loops
• range() function
• Conditional statements
• if-else statement
• Modulus operator (%)
• String repetition
• Multiple inner loops
• print() function
"""

rows = int(input("Enter an odd number of rows: "))

if rows > 0 and rows % 2 != 0:
    middle = rows // 2

    for i in range(middle + 1):
        for j in range(2 * i + 1):
            print("*", end="")
        print()

    for i in range(middle - 1, -1, -1):
        for j in range(2 * i + 1):
            print("*", end="")
        print()
else:
    print("Invalid row count. Please enter a positive odd number.")


"""
8. Floyd's Triangle Pattern
Question: Develop a Python program to accept the number of rows from the user and generate Floyd's
triangle.
For example, if the user enters 5, the output should be:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
The numbers must continue sequentially across all rows without restarting from 1.
Concepts to Use:
• Nested for loops
• range() function
• Counter variables
• Increment operators
• Sequential number generation
• print() function
• end parameter
"""

rows = int(input("Enter number of rows: "))

if rows > 0:
    number = 1

    for i in range(1, rows + 1):
        for j in range(i):
            print(number, end=" ")
            number += 1
        print()
else:
    print("Enter a positive number of rows.")


"""
9. Multiplication Tables Grid Generator
Question: Develop a multiplication table grid generator.
Accept the starting and ending numbers from the user.
Generate multiplication tables for all numbers within the given range.
For example, if the user enters 2 as the starting number and 5 as the ending number, generate
multiplication tables from 2 to 5, each from 1 to 10.
Display the tables in a properly organized format.
Concepts to Use:
• input() function
• int() type conversion
• Nested for loops
• range() function
• Arithmetic operators
• Loop variables
• F-string formatting
• print() function
• end parameter
"""

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

if start <= end:
    for i in range(start, end + 1):
        print(f"\nMultiplication Table of {i}")
        print("-------------------------")

        for j in range(1, 11):
            print(f"{i} × {j} = {i * j}")
else:
    print("Invalid range. Starting number must be less than or equal to ending number.")


"""
10. Cinema Seating Arrangement Generator
Question: Develop a cinema seating arrangement application using nested loops.
Accept the following details:
• Number of rows in the cinema hall.
• Number of seats in each row.
• Number of seats to be marked as reserved.
Represent the cinema seating arrangement using a nested list.
Use the following symbols:
• A – Available seat.
• R – Reserved seat.
Display the complete seating arrangement in a row-and-column format.
Perform the following operations:
1. Display all available seats.
2. Display all reserved seats.
3. Calculate the total number of available seats.
4. Calculate the total number of reserved seats.
5. Display the seating arrangement after reservations.
6. Allow the user to select a row and seat number to reserve an available seat.
7. Prevent the reservation of an already reserved or invalid seat.
Concepts to Use:
• Nested lists
• Nested for loops
• while loop
• range() function
• Conditional statements
• break and continue statements
• List indexing
• List modification
• Counter variables
• print() formatting
"""

rows = int(input("Enter number of rows in the cinema hall: "))
seats_per_row = int(input("Enter number of seats in each row: "))
reserved_count = int(input("Enter number of seats to be marked as reserved: "))

if rows <= 0 or seats_per_row <= 0:
    print("Rows and seats per row must be positive.")
elif reserved_count < 0 or reserved_count > rows * seats_per_row:
    print("Invalid number of reserved seats.")
else:
    # Create the seating arrangement with all seats available.
    seats = [["A" for j in range(seats_per_row)] for i in range(rows)]

    # Mark the requested number of seats as reserved, row by row.
    for i in range(rows):
        for j in range(seats_per_row):
            if reserved_count > 0:
                seats[i][j] = "R"
                reserved_count -= 1
            else:
                break
        if reserved_count == 0:
            break

    print("\nInitial Seating Arrangement:")
    for i in range(rows):
        print(f"Row {i + 1}: ", end="")
        for j in range(seats_per_row):
            print(seats[i][j], end=" ")
        print()

    # Display available and reserved seats.
    available_seats = []
    reserved_seats = []
    available_count = 0
    reserved_total = 0

    for i in range(rows):
        for j in range(seats_per_row):
            if seats[i][j] == "A":
                available_seats.append(f"Row {i + 1}, Seat {j + 1}")
                available_count += 1
            else:
                reserved_seats.append(f"Row {i + 1}, Seat {j + 1}")
                reserved_total += 1

    print("\nAvailable Seats:")
    if available_seats:
        for seat in available_seats:
            print(seat)
    else:
        print("No available seats.")

    print("\nReserved Seats:")
    if reserved_seats:
        for seat in reserved_seats:
            print(seat)
    else:
        print("No reserved seats.")

    print(f"\nTotal Available Seats: {available_count}")
    print(f"Total Reserved Seats : {reserved_total}")

    # Allow the user to reserve additional seats.
    while True:
        choice = input("\nDo you want to reserve an available seat? (yes/no): ").lower()

        if choice == "no":
            break
        elif choice != "yes":
            print("Enter yes or no.")
            continue

        row_number = int(input("Enter row number: "))
        seat_number = int(input("Enter seat number: "))

        if not (1 <= row_number <= rows and 1 <= seat_number <= seats_per_row):
            print("Invalid row or seat number.")
            continue

        if seats[row_number - 1][seat_number - 1] == "R":
            print("This seat is already reserved.")
            continue

        seats[row_number - 1][seat_number - 1] = "R"
        print(f"Seat {seat_number} in Row {row_number} reserved successfully.")

    # Display the final seating arrangement and updated counts.
    available_count = 0
    reserved_total = 0

    print("\nFinal Seating Arrangement:")
    for i in range(rows):
        print(f"Row {i + 1}: ", end="")
        for j in range(seats_per_row):
            print(seats[i][j], end=" ")

            if seats[i][j] == "A":
                available_count += 1
            else:
                reserved_total += 1
        print()

    print(f"\nTotal Available Seats: {available_count}")
    print(f"Total Reserved Seats : {reserved_total}")
