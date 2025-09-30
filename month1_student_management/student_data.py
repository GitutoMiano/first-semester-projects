students = []

def add_student():
    """
    TODO: Prompt the user to enter student name, age, and grade.
    Append the student as a dictionary to the students list.
    """
    name = input("Enter student name: ")
    age_input = input("Enter student age: ")
    grade_input = input("Enter student grade: ")
    
    try:
        age = int(age_input)
        grade = float(grade_input)
    except ValueError:
        print("Invalid input. Age must be an integer and grade must be a number.")
        return

    student = {"name": name, "age": age, "grade": grade}
    students.append(student)
    print(f"{name} added successfully!\n")


def view_students():
    """
    TODO: Loop through the students list and print each student's info.
    """
    if not students:
        print("No students in the list.\n")
        return

    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
    print()  # blank line


def get_average_grade():
    """
    TODO: Return the average grade of all students.
    """
    if not students:
        print("No students to calculate average.\n")
        return 0

    total = sum(student["grade"] for student in students)
    average = total / len(students)
    return average

# Menu loop
if __name__ == "__main__":
    while True:
        print("1. Add student")
        print("2. View students")
        print("3. Get average grade")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            avg = get_average_grade()
            print(f"Average grade: {avg}\n")
        elif choice == "4":
            break
        else:
            print("Invalid option. Try again.\n")