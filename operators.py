# Demonstrating Python Operators

a = 10
b = 5

# Arithmetic Operators
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponent:", a ** b)
print("Floor Division:", a // b)


# Comparison Operators
print("a > b:", a > b)
print("a < b:", a < b)
print("a == b:", a == b)
print("a != b:", a != b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


# Logical Operators
print("a > b and b < 10:", (a > b) and (b < 10))
print("a > b or b > 10:", (a > b) or (b > 10))
print("not(a > b):", not(a > b))


# Assignment Operators
x = 10
x += 5
print("x after += :", x)

x -= 3
print("x after -= :", x)


# Identity Operators
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print("x is y:", x is y)
print("x is z:", x is z)


# Membership Operators
numbers = [1, 2, 3, 4]

print("2 in numbers:", 2 in numbers)
print("5 not in numbers:", 5 not in numbers)


# Mini Example (Application)
# Check if a number is even or odd
num = 4

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
