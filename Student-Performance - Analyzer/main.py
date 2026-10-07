from student import Student
from marks import calculate_total, calculate_average
from analyzer import calculate_percentage, calculate_grade, check_result, find_highest_subject, find_lowest_subject, check_attendance, calculate_class_average
from storage import save_student, display_students, get_students, display_marks, search_student
from report import display_report
from visualization import show_marks_chart, show_student_percentage_chart, show_class_average_chart

def add_student():

    while True:
        name = input("Enter student name: ").strip()

        if name:
            break

        print("Name cannot be empty!")

    while True:
        roll_no = input("Enter roll number: ").strip()

        if not roll_no:
            print("Roll number cannot be empty!")
            continue

        existing_student = search_student(roll_no)

        if existing_student is not None:
            print("This roll number already exists!")
            continue

        break
    

    student1 = Student(name, roll_no)

    student1.display_student()

    while True:

        try:
            python_marks = float(input("Enter Python marks (0-100): "))

            if python_marks >= 0 and python_marks <= 100:
                break

            print("Invalid marks! Enter marks between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")

    while True:

        try:
            maths_marks = float(input("Enter Maths marks (0-100): "))

            if maths_marks >= 0 and maths_marks <= 100:
                break

            print("Invalid marks! Enter marks between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")


    while True:

        try:
            english_marks = float(input("Enter English marks (0-100): "))

            if english_marks >= 0 and english_marks <= 100:
                break

            print("Invalid marks! Enter marks between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")


    while True:

        try:
            physics_marks = float(input("Enter Physics marks (0-100): "))

            if physics_marks >= 0 and physics_marks <= 100:
                break

            print("Invalid marks! Enter marks between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")


    while True:

        try:
            evs_marks = float(input("Enter EVS marks (0-100): "))

            if evs_marks >= 0 and evs_marks <= 100:
                break

            print("Invalid marks! Enter marks between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")

    marks = [
            python_marks,
            maths_marks,
            english_marks,
            physics_marks,
            evs_marks
        ]

    subjects = [
            "Python",
            "Maths",
            "English",
            "Physics",
            "EVS"
        ]

    total = calculate_total(marks)
    average = calculate_average(marks)

    print("Total Marks:", total)
    print("Average Marks:", average)

    percentage = calculate_percentage(total, 500)

    print("Percentage:", percentage, "%")

    grade = calculate_grade(percentage)

    print("Grade:", grade)

    result = check_result(marks)

    print("Result:", result)

    highest_subject = find_highest_subject(subjects, marks)
    lowest_subject = find_lowest_subject(subjects, marks)

    print("Highest Subject:", highest_subject)
    print("Lowest Subject:", lowest_subject)

    while True:

       try:
          attendance = float(input("Enter attendance percentage (0-100): "))

          if attendance >= 0 and attendance <= 100:
              break

          print("Invalid attendance! Enter a value between 0 and 100.")

       except ValueError:
           print("Invalid input! Please enter a number.")


    attendance_status = check_attendance(attendance)

    print("Attendance:", attendance, "%")
    print("Attendance Status:", attendance_status)

    student_data = {
        "Name": name,
        "Roll No": roll_no,
        "Python": python_marks,
        "Maths": maths_marks,
        "English": english_marks,
        "Physics": physics_marks,
        "EVS": evs_marks,
        "Total": total,
        "Average": average,
        "Percentage": percentage,
        "Grade": grade,
        "Result": result,
        "Attendance": attendance,
        "Attendance Status": attendance_status,
        "Highest Subject": highest_subject,
        "Lowest Subject": lowest_subject
    }

    save_student(student_data)

while True:

    print("======================================")
    print("     STUDENT PERFORMANCE ANALYZER")
    print("======================================")

    print("1. Add Student")
    print("2. View Student")
    print("3. Enter Marks")
    print("4. Analyze Performance")
    print("5. Generate Report")
    print("6. Search Student")
    print("7. View Performance Graph")
    print("8. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
         display_marks()

    elif choice == "4":
         students = get_students()

         if len(students) == 0:
             print("No student data found.")

         else:
              print("\n===== PERFORMANCE ANALYSIS =====")

              for student in students:
                print("\nName:", student["Name"])
                print("Roll No:", student["Roll No"])
                print("Percentage:", student["Percentage"], "%")
                print("Grade:", student["Grade"])
                print("Result:", student["Result"])
                print("Highest Subject:", student["Highest Subject"])
                print("Lowest Subject:", student["Lowest Subject"])
                print("Attendance:", student["Attendance"], "%")
                print("Attendance Status:", student["Attendance Status"])
        
                class_average = calculate_class_average(students)

                print("\nClass Average Percentage:", class_average, "%")

    elif choice == "5":

        students = get_students()

        if len(students) == 0:
            print("No student data found.")

        else:
            print("\n========== SELECT STUDENT ==========")

            for student in students:
                print(
                    "Roll No:",
                    student["Roll No"],
                    "| Name:",
                    student["Name"]
                )

            roll_no = input("\nEnter Roll No. for report: ")

            selected_student = None

            for student in students:
                if student["Roll No"] == roll_no:
                    selected_student = student
                    break

            if selected_student is None:
                print("Student not found!")

            else:

                subjects = [
                    "Python",
                    "Maths",
                    "English",
                    "Physics",
                    "EVS"
                ]

                marks = [
                    float(selected_student["Python"]),
                    float(selected_student["Maths"]),
                    float(selected_student["English"]),
                    float(selected_student["Physics"]),
                    float(selected_student["EVS"])
                ]

                display_report(
    selected_student["Name"],
    selected_student["Roll No"],
    subjects,
    marks,
    float(selected_student["Total"]),
    float(selected_student["Average"]),
    float(selected_student["Percentage"]),
    selected_student["Grade"],
    selected_student["Result"],
    float(selected_student["Attendance"]),
    selected_student["Attendance Status"],
    selected_student["Highest Subject"],
    selected_student["Lowest Subject"]
)
                
    elif choice == "6":

        roll_no = input("Enter Roll No. to search: ")

        student = search_student(roll_no)

        if student is None:
            print("Student not found!")

        else:
            print("\n========== STUDENT FOUND ==========")
            print("Name:", student["Name"])
            print("Roll No:", student["Roll No"])
            print("Python:", student["Python"])
            print("Maths:", student["Maths"])
            print("English:", student["English"])
            print("Physics:", student["Physics"])
            print("EVS:", student["EVS"])
            print("Total:", student["Total"])
            print("Average:", student["Average"])
            print("Percentage:", student["Percentage"])
            print("Grade:", student["Grade"])
            print("Result:", student["Result"])
            print("Attendance:", student["Attendance"], "%")
            print("Attendance Status:", student["Attendance Status"])
            print("Highest Subject:", student["Highest Subject"])
            print("Lowest Subject:", student["Lowest Subject"])
            print("==================================")


    elif choice == "7":

        students = get_students()

        if len(students) == 0:
            print("No student data found.")

        else:
            print("========== PERFORMANCE GRAPH ==========")
            print("1. Individual Student Marks")
            print("2. All Students Percentage")
            print("3. Class Average")

            graph_choice = input("Enter your choice: ")

            if graph_choice == "1":

                print("\n========== SELECT STUDENT ==========")

                for student in students:
                    print(
                        "Roll No:",
                        student["Roll No"],
                        "| Name:",
                        student["Name"]
                    )

                roll_no = input("\nEnter Roll No. for graph: ")

                selected_student = None

                for student in students:
                    if student["Roll No"] == roll_no:
                        selected_student = student
                        break

                if selected_student is None:
                    print("Student not found!")

                else:

                    subjects = [
                        "Python",
                        "Maths",
                        "English",
                        "Physics",
                        "EVS"
                    ]

                    marks = [
                        float(selected_student["Python"]),
                        float(selected_student["Maths"]),
                        float(selected_student["English"]),
                        float(selected_student["Physics"]),
                        float(selected_student["EVS"])
                    ]

                    show_marks_chart(subjects, marks)

            elif graph_choice == "2":

                 show_student_percentage_chart(students)

            elif graph_choice == "3":

                 show_class_average_chart(students)

            else:
                 print("Invalid choice!")

    elif choice == "8":
        print("Thank you for using Student Performance Analyzer!")
        break