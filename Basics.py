# Assignment-1 : Python Basics
# 1. Print Name
print("My Name is Monisha")

# 2. Single-line Comment
# This is a single-line comment

"""
Multi-line Comment
Used to explain multiple lines
"""

# 3. Different Data Types
age = 21                 # Integer
height = 5.9             # Float
is_student = True        # Boolean
grade = "A"              # String

print(age)
print(height)
print(is_student)
print(grade)

# 4. Local and Global Variables
x = "Global Variable"

def show():
    x = "Local Variable"
    print(x)

show()
print(x)

