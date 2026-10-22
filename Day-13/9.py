"""
Basic Level Question - if, if-else
9.    Ask the user to enter their name. If the name is “admin”, print “Welcome, Admin!”
"""

name= input("Enter your name: ")
if name == 'admin' or 'Admin':
    print("Welcome,",name,"#Admin!")
else:
    print("Welcome,",name,"#User!")