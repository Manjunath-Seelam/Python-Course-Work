"""
Basic Level Question - Nested-if/nested if-else conditional statement:
1.Take a character input and check whether it is uppercase letter or lowercase letter or not letter.
"""

char=input("Enter a Alphabet: ")
print("Entered Alphabet is: ", char)
if len(char)==1:
    if char .isalpha():
        if char .isupper():
            print("The entered alphabet ",char,"is Upper.")
        else:
            print("The entered alphabet ",char,"is lower")
    else:
        print("The entered alphabet ", char," is not a letter")
else:
    print("Enter only single character")
    
