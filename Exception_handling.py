#Q1. ZeroDivisionError:...
def divide_numbers(a, b):

    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None  #  handle the error 

# Example usage:
try:
    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))
    result = divide_numbers(num1, num2)
    if result is not None:
        print("Result:", result)
except ValueError:
    print("Error: Invalid input. Please enter integers only.")
    
#Q2. ValueError: If the input is not a valid integer...
def get_integer_input():

    while True:
        try:
            num = int(input("Enter an integer: "))
            return num
        except ValueError:
            print("Error: Invalid input. Please enter an integer.")

# Example usage:
num = get_integer_input()
print("You entered:", num)

#Q3. FileNotFoundError:If the file does not exist...
def read_file(file_path):

    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: File not found")

# Example usage:
file_name = input("Enter the file name: ")
read_file(file_name)

#Q4. TypeError:If the inputs are not numerical.
def add_numbers(a, b):
    
    try:
        result = a + b
        return result
    except TypeError:
        print("Error: Invalid input. Please enter numbers only.")

# Example usage:
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = add_numbers(num1, num2)
    print("Sum:", result)
except ValueError:
    print("Error: Invalid input. Please enter numbers only.")