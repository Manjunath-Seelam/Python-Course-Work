"""
CONDITIONAL STATEMENTS
If-Else Statement
2. Write a Python program that checks if a given character is a vowel or a consonant.
"""
n=1
data=input("Enter a Character: ").lower()[:n]
if data in "aeiou":
    print(f"The Entered character {data}, is a Vowel.")
else:
    print(f"The entered character {data} is a consonant")