#***1. Calculate the Multiplication and Sum of Two Numbers....
# Inputs
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

# Calculations
multiplication = num1 * num2
addition = num1 + num2

# Output
print("Multiplication:", multiplication)
print("Sum:", addition)

#***2. Declare Two Variables and Print the Largest Using Ternary Operators....
# Declare two variables
a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))

# Find the largest
largest = a if a > b else b

print("The largest number is:", largest)

#***3. Convert Temperature from Celsius to Fahrenheit....
# Input
celsius = 30

# Conversion
fahrenheit = celsius * 9 / 5 + 32

# Output
print(f"{celsius}°C is equal to {fahrenheit}°F")

#***4. Find the Area of a Triangle Using Given Sides....

import math

# Sides of the triangle
a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))

# Semi-perimeter
s = (a + b + c) / 2

# Area calculation
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Output
print(f"The area of the triangle is: {area:.2f}")



