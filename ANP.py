#.....Q1 print helloworld
print("Hello World")

#......Q.2 describe local variable and global variable code
x = 10 # Global variable

def my_function():
   
    y = 20 # Local variable
    print("Local variable y:", y)
    print("Global variable x accessed in function:", x)

my_function()
print("Global variable x outside function:", x)
# print(y)  # This would throw an error because y is a local variable



#......Q.3 Write a code that describe Indentation error
# ptint(" hello world") #Indentation error because of the "SPACE BEFORE PRINT"
 
 
#......Q.4 write a code that describe local and global variable with same name
x = "Global Variable"

def my_function():
    x = "Local Variable"
    print("Inside function:", x)

my_function()
print("Outside function:", x)


#........Q5 Write a code for string, int and float input.

name = input("Enter your name: ")# Input a string

age = int(input("Enter your age: "))# Input an integer

height = float(input("Enter your height in meters: "))# Input a float

print("\nUser Details:")
print("Name:", name)
print("Age:", age)
print("Height:", height, "meters")

