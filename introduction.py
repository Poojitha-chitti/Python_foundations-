# Introduction to Python Fundamentals

# Variables and Data Types
name = "Poojitha"
age = 21
is_student = True

print("Name:", name)
print("Age:", age)
print("Student Status:", is_student)


# Variable Naming Conventions
camelCaseVar = "Camel Case"
PascalCaseVar = "Pascal Case"
snake_case_var = "Snake Case"

print(camelCaseVar)
print(PascalCaseVar)
print(snake_case_var)


# Multiple Assignments
a, b, c = 1, 2, 3
print("Multiple values:", a, b, c)

# One value to multiple variables
x = y = z = 100
print("Same value:", x, y, z)


# Global Variable Example
global_var = "I am global"

def display():
    print(global_var)

display()


# Indexing (Accessing characters in string)
text = "Python"
print("First character:", text[0])
print("Last character:", text[-1])


# Type Casting
# Implicit Type Casting
num_int = 10
num_float = 5.5
result = num_int + num_float
print("Implicit casting result:", result)

# Explicit Type Casting
num_str = "20"
num_int2 = int(num_str)
print("Explicit casting result:", num_int2)
