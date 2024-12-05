# 1: Division Function...
def div(num1, num2):
    if num2 == 0:
        print("Error: Division by zero")
    else:
        result = num1 / num2
        print("Division:", result)

# Call the function
div(10, 2)  # Pass two numbers
#output is: Division: 5.0

# 2: Square Function...
def square(num):
    result = num * num
    print("Square:", result)

# Call the function
square(5)  # Pass one number
#output is: Square: 25 

# 3: Maximum and Minimum of Random Numbers...
import random

def find_max_min():
    numbers = [random.randint(1, 100) for _ in range(5)]
    print("Random numbers:", numbers)

    max_num = max(numbers)
    min_num = min(numbers)

    print("Maximum:", max_num)
    print("Minimum:", min_num)

# Call the function
find_max_min()
#output is: Maximum: 95
#           Minimum: 24

# 4: Lowercase Name....
def to_lowercase():
    name = input("Enter your name: ")
    lowercase_name = name.lower()
    print("Lowercase name:", lowercase_name)

# Call the function
to_lowercase()
#output is: Enter your name: FIRDAUS
#            Lowercase name: firdaus