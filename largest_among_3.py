# Find Largest Among Three Numbers...
num1 = int(input("Enter the first number: "))  #take input from user
num2 = int(input("Enter the second number: "))  #take input from user
num3 = int(input("Enter the third number: "))  #take input from user

if num1 >= num2 and num1 >= num3: 
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("The largest number is:", largest)