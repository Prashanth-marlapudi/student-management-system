# Student Management System

A simple command-line Student Management System built with Python. This beginner-friendly project uses **Python lists only** (no dictionaries or database) to store and manage student records.

## Features

- Add a student
- View all students
- Search for a student by ID
- Update student details
- Delete a student
- Calculate the average marks of all students
- Menu-driven interface

## Project Structure

```text
Student_Management_System/
├── student_management.py
└── README.md
```

## Requirements

- Python 3.x
- No external libraries are required.

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python student_management.py
   ```

   On some systems, use `python3 student_management.py`.

## Python Concepts Used

- Variables and data types
- Lists and list methods (`append`, `pop`, `index`)
- Functions
- Loops and conditional statements
- User input and output
- Exception handling (`try` / `except`)
- Basic calculations

## How Data Is Stored

The program uses four parallel lists:

- `student_ids`
- `student_names`
- `student_ages`
- `student_marks`

The same index in each list refers to the same student. For example, the details at index `0` in all four lists belong to the first student.

## Limitations

Student records are stored in memory. They are removed when the program exits, so this version does not permanently save data.

## Future Improvements

- Save student records to a file or database
- Add input validation for names and marks
- Add sorting and filtering options
- Build a graphical user interface

## Learning Outcome

This project provides practice with Python fundamentals and the basic CRUD operations: Create, Read, Update, and Delete.
