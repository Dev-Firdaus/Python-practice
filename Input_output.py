#Q1. Read and display content line by line...
def read_and_display(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            print(line.rstrip())

# Example usage:
read_and_display("ABC.txt")

#Q2. Count and display total words...
def count_words(file_path):
    with open(file_path, 'r') as file:
        word_count = 0
        for line in file:
            words = line.split()
            word_count += len(words)
    print("Total words:", word_count)

# Example usage:
count_words("ABC.txt")

#Q3. Count uppercase characters...
def count_uppercase(file_path):
    with open(file_path, 'r') as file:
        uppercase_count = 0
        for line in file:
            for char in line:
                if char.isupper():
                    uppercase_count += 1
    print("Uppercase characters:", uppercase_count)

# Example usage:
count_uppercase("ABC.txt")

#Q4. Display words less than 4 characters...
def display_words(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if len(word) < 4:
                    print(word)

# Example usage:
display_words("story.txt")