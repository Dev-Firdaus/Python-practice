
 # Capitalize first letter in a string

def capitalize_words(input_string):
    # Use the title() method to capitalize the first letter of each word
    capitalized_string = input_string.title()
    return capitalized_string

# Input string
user_input = input("Enter a string: ")

# Capitalize the first letter ....
result = capitalize_words(user_input)

# Output
print("Capitalized string:", result)
