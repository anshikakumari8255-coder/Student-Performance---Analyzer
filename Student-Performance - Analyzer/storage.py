import csv
import os


def save_student(data):

    file_exists = os.path.exists("students.csv")
    file_empty = not file_exists or os.path.getsize("students.csv") == 0

    with open("students.csv", "a", newline="") as file:

        fieldnames = [
            "Name",
            "Roll No",
            "Python",
            "Maths",
            "English",
            "Physics",
            "EVS",
            "Total",
            "Average",
            "Percentage",
            "Grade",
            "Result",
            "Attendance",
            "Attendance Status",
            "Highest Subject",
            "Lowest Subject"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if file_empty:
            writer.writeheader()

        writer.writerow(data)

print("Student data saved successfully!")

def display_students():

    try:
        with open("students.csv", "r", newline="") as file:
            reader = csv.DictReader(file)

            print("\n========== SAVED STUDENTS ==========")

            for student in reader:
                print("Name:", student["Name"])
                print("Roll No:", student["Roll No"])
                print("Total:", student["Total"])
                print("Average:", student["Average"])
                print("Percentage:", student["Percentage"])
                print("Grade:", student["Grade"])
                print("Result:", student["Result"])
                print("Attendance:", student["Attendance"], "%")
                print("-----------------------------------")

    except FileNotFoundError:
        print("No student data found.")

def get_students():

    try:
        with open("students.csv", "r", newline="") as file:
            reader = csv.DictReader(file)

            students = list(reader)

            return students

    except FileNotFoundError:
        return []

def display_marks():

    students = get_students()

    if len(students) == 0:
        print("No student data found.")
        return

    print("\n========== SUBJECT-WISE MARKS ==========")

    for student in students:

        print("\nName:", student["Name"])
        print("Roll No:", student["Roll No"])

        print("Python:", student["Python"])
        print("Maths:", student["Maths"])
        print("English:", student["English"])
        print("Physics:", student["Physics"])
        print("EVS:", student["EVS"])

        print("-----------------------------------")

def search_student(roll_no):

    students = get_students()

    for student in students:

        if student["Roll No"] == roll_no:
            return student

    return None    