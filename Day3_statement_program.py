#1. Check if a Number is Even or Odd Using Ternary Operator...
num = int(input("Enter a number: "))
result = "Even" if num % 2 == 0 else "Odd"
print(f"The number {num} is {result}.")


#2. Swap Two Numbers Using Input Function...
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
# Swap the numbers
a, b = b, a
print(f"After swapping: First number = {a}, Second number = {b}")


#3. Program to Convert Kilometers to Miles...
kilometers = float(input("Enter distance in kilometers: "))
# Conversion factor
conversion_factor = 0.621371
miles = kilometers * conversion_factor
print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")


# 4. Find the Simple Interest on Rs. 200 for 5 years at 5% per year.
# Given values
principal = 200  # Rs. 200
rate_of_interest = 5  # 5% per year
time = 5  # 5 years

# Calculate Simple Interest
simple_interest = (principal * rate_of_interest * time) / 100
print(f"The Simple Interest is: Rs. {simple_interest}")

