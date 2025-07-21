#To get input
a=input("Enter your name")
print("hi "+a)

#To get multiple inputs
a,b=input("enter your name").split()
print(b)

#in python by default input() takes string input
b=input("enter your name")
print(b)
c=input()
d=b+c
print (d)
#output
"""
enter your name3
3
2
32

"""

#  Variable naming
"""
Variable names can only contain letters, digits and underscores (_).
A variable name cannot start with a digit.
Variable names are case-sensitive (myVar and myvar are different).
Avoid using Python keywords (e.g., if, else, for) as variable names.
"""

# Assigning value to variable
x = 10
print(x) 

# Removing the variable using del
del x
#swapping 2 variable
a,b=5,10
a,b=b,a
print(a,b)
"""output
   10 5
"""

# Floor Division
print("Floor Division:", a // b)  

# Exponentiation
print("Exponentiation:", a ** b)

#if x=2.4
x = int(input())
print(x)
"""
input() function returns the input as a string. When int() tries to convert the string '1.5' into an integer, it raises a ValueError because '1.5' is not a valid integer literal.
"""
