# Student Management System
# Beginner-friendly project using Python lists only.

student_ids = []
student_names = []
student_ages = []
student_marks = []

next_id = 1


def add_student():
    global next_id

    name = input("Enter student name: ").strip()

    try:
        age = int(input("Enter student age: "))
        marks = float(input("Enter student marks: "))
    except ValueError:
        print("Please enter a valid age and marks.")
        return

    student_ids.append(next_id)
    student_names.append(name)
    student_ages.append(age)
    student_marks.append(marks)

    print(f"Student added successfully! Student ID: {next_id}")
    next_id += 1


def view_students():
    if not student_ids:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
    for i in range(len(student_ids)):
        print(
            f"ID: {student_ids[i]} | "
            f"Name: {student_names[i]} | "
            f"Age: {student_ages[i]} | "
            f"Marks: {student_marks[i]}"
        )


def search_student():
    try:
        student_id = int(input("Enter student ID to search: "))
    except ValueError:
        print("Please enter a valid student ID.")
        return

    if student_id in student_ids:
        index = student_ids.index(student_id)
        print("\nStudent found:")
        print(f"ID: {student_ids[index]}")
        print(f"Name: {student_names[index]}")
        print(f"Age: {student_ages[index]}")
        print(f"Marks: {student_marks[index]}")
    else:
        print("Student not found.")


def update_student():
    try:
        student_id = int(input("Enter student ID to update: "))
    except ValueError:
        print("Please enter a valid student ID.")
        return

    if student_id not in student_ids:
        print("Student not found.")
        return

    index = student_ids.index(student_id)
    print("Enter the new details:")

    name = input("Enter new name: ").strip()

    try:
        age = int(input("Enter new age: "))
        marks = float(input("Enter new marks: "))
    except ValueError:
        print("Please enter a valid age and marks. No changes were made.")
        return

    student_names[index] = name
    student_ages[index] = age
    student_marks[index] = marks

    print("Student details updated successfully.")


def delete_student():
    try:
        student_id = int(input("Enter student ID to delete: "))
    except ValueError:
        print("Please enter a valid student ID.")
        return

    if student_id not in student_ids:
        print("Student not found.")
        return

    index = student_ids.index(student_id)

    student_ids.pop(index)
    student_names.pop(index)
    student_ages.pop(index)
    student_marks.pop(index)

    print("Student deleted successfully.")


def calculate_average():
    if not student_marks:
        print("No marks available to calculate an average.")
        return

    average = sum(student_marks) / len(student_marks)
    print(f"Average student marks: {average:.2f}")


def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Calculate Average Marks")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            calculate_average()
        elif choice == "7":
            print("Thank you for using Student Management System!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 7.")


if __name__ == "__main__":
    main()
