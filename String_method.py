#1. Count all letters, digits, and special symbols from a given string
# Input string
string = "P@#yn26at^&i5ve"

# Count the number of letters in the string using isalpha()
letters = sum(char.isalpha() for char in string)

# Count the number of digits in the string using isdigit()
digits = sum(char.isdigit() for char in string)

# Count the number of special symbols (non-alphanumeric characters)
special = sum(not char.isalnum() for char in string) #isalpha() returns True if the character is a letter

# Display the counts
print("Chars =", letters, "Digits =", digits, "Symbol =", special)
#Output is: Chars = 8 Digits = 3 Symbol = 4

#2. Remove duplicate characters from a given string
# Input string
string = "String and String Function"

# Initialize an empty string to store the result
result = ""

# Loop through each character in the string
for char in string:
    # If the character is not already in the result, add it
    if char not in result:
        result += char

# Display the output string without duplicates
print("Output:", result)
#Output is: Output: String adFuco

#3. Count uppercase, lowercase, special characters, and numeric values
# Input string
string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"

# Count the number of uppercase letters using isupper()
upper = sum(char.isupper() for char in string)

# Count the number of lowercase letters using islower()
lower = sum(char.islower() for char in string)

# Count the number of digits using isdigit()
digits = sum(char.isdigit() for char in string)

# Count special characters by checking if they are not alphanumeric and not spaces
special = sum(not char.isalnum() and not char.isspace() for char in string)

# Display the results
print("UpperCase:", upper)
print("LowerCase:", lower)
print("NumberCase:", digits)
print("SpecialCase:", special)
#Output:
'''UpperCase: 5
LowerCase: 18
NumberCase: 5
SpecialCase: 3'''

#4. Count vowels in a string
# Input string
string = "Welcome to Python Assignment"

# Define the set of vowels 
vowels = "aeiouAEIOU"

# Count vowels by checking each character
vowel_count = sum(1 for char in string if char in vowels)

# Display the total number of vowels
print("Total vowels are:", vowel_count)
#Output is: Total vowels are: 8