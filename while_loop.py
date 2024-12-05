# 1. Reverse a Number...
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num

number = int(input("Enter a number: "))
reversed_number = reverse_number(number)
print("Reversed number:", reversed_number)

# 2. Check for Palindrome...
def is_palindrome(num):
    original_num = num
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return original_num == reversed_num

number = int(input("Enter a number: "))
if is_palindrome(number):
    print(number, "is a palindrome")
else:
    print(number, "is not a palindrome")
    
# 3. Factorial of a Number...
def factorial(num):
    if num == 0:
        return 1
    factorial = 1
    while num > 0:
        factorial *= num
        num -= 1
    return factorial

number = int(input("Enter a number: "))
result = factorial(number)
print("Factorial of", number, "is", result)

#4. Sum of Numbers until 0....
def sum_until_zero():
    total = 0
    while True:
        num = int(input("Enter a number (0 to stop): "))
        if num == 0:
            break
        total += num
    print("Sum of the numbers:", total)

sum_until_zero()