"""
DAY 1 TO DAY 3
PYTHON ASSIGNMENT SOLUTIONS

This file contains simple solutions for all 30 questions.
Each question is kept as a separate section.
"""

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
1. String Indexing and Slicing
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
