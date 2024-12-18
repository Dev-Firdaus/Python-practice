#1. Counting Word Occurrences:
def count_word_occurrences(sentence):
    words = sentence.split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

string = "To change the overall look of your document. To change the look available in the gallery"
word_counts = count_word_occurrences(string)
for word, count in word_counts.items():
    print(f"{word}: {count}")
    

#output of the code
''' 
To: 2
change: 2   
the: 3      
overall: 1  
look: 2     
of: 1       
your: 1     
document.: 1
available: 1
in: 1       
gallery: 1  
'''

#2. Removing Newlines:
def remove_newlines(string):
    return string.replace('\n', '')

string = "\nBest \nDeeptech \nPython \nTraining\n"
result = remove_newlines(string)
print(result)

#Output is: Best Deeptech Python Training


#3. Reversing Words in a String:
def reverse_words(string):
    words = string.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

string = "Deeptech Python Training"
result = reverse_words(string)
print(result)

#input is:Deeptech Python Training
#Output is: Training Python Deeptech


#4. Counting Vowels:
def count_vowels(string):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    for char in string:
        if char in vowels:
            vowel_count += 1
    return vowel_count

string = "Welcome to python Training"
vowel_count = count_vowels(string)
print("Number of vowels:", vowel_count)
#Output is: Number of vowels: 8

