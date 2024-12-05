# 1. Print the first 10 natural numbers:.....
print("The first 10 natural numbers are:")
for num in range(1, 11):
    print(num)

#2. Check if the given string is a palindrome:...
def is_palindrome(string):
    return string == string[::-1]

string = input("Enter a string: ")
# check palindrom using for loop
if is_palindrome(string):
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")
    
# 3. Check if a given number is an Armstrong number:
def is_armstrong_number(num):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    return num == sum

num = int(input("Enter a number: "))
if is_armstrong_number(num):
    print(num, "is an Armstrong number")
else:
    
    print(num, "is not an Armstrong number")
    
#4. Get the Fibonacci series between 0 to 50:
def fibonacci_series(n):
    fib_series = [0, 1]
    for i in range(2, n+1):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    return fib_series

n = 50
fib_series = fibonacci_series(n)
for num in fib_series:
    if num > 50:
        break
    print(num)
    
# 5. Check the validity of password input by users:
'''
Password criteria:
Minimum 8 characters
Contains at least one digit
Contains at least one uppercase letter
Contains at least one lowercase letter
'''
def is_valid_password(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    return True

password = input("Enter your password: ")
if is_valid_password(password):
    print("Valid password")
else:
    print("Invalid password")