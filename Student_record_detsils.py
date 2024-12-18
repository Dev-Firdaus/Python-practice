def display_student_records(records):
    """Displays all student records."""
    print("\nStudent Records:")
    print("-" * 40)
    for record in records:
        name, scores, grade = record
        print(f"Name: {name}, Scores: {scores}, Final Grade: {grade}")
    print("-" * 40)

def calculate_final_grade(scores):
    """Calculates the final grade based on exam scores."""
    average = sum(scores) / len(scores)
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def add_student_record(records):
    """Adds a new student record."""
    name = input("Enter student's name: ")
    scores = tuple(map(int, input("Enter exam scores separated by space: ").split()))
    grade = calculate_final_grade(scores)
    records.append((name, scores, grade))
    print(f"Student {name} added successfully!")

def main():
    """Main function to manage student records."""
    student_records = []  # List to store student records as tuples

    while True:
        print("\nStudent Record Management")
        print("1. Add Student Record")
        print("2. Display All Records")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student_record(student_records)
        elif choice == "2":
            display_student_records(student_records)
        elif choice == "3":
            print("Exiting program. See you soon!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
main()
