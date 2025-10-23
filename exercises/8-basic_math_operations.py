import math

def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  if b == 0:
    return "Error: Cannot divide by zero"
  return a / b

def sqrt(a):
  return math.sqrt(a)

def power(a, b):
  return a ** b

print(f"Addition: 10 + 5 = {add(10, 5)}")
print(f"Subtraction: 10 - 5 = {subtract(10, 5)}")
print(f"Multiplication: 10 * 5 = {multiply(10, 5)}")
print(f"Division: 10 / 5 = {divide(10, 5)}")
print(f"Square root of 16 = {sqrt(16)}")
print(f"Power of 2 to 3 = {power(2, 3)}")
