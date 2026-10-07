def display_report(
    name,
    roll_no,
    subjects,
    marks,
    total,
    average,
    percentage,
    grade,
    result,
    attendance,
    attendance_status,
    highest_subject,
    lowest_subject
):

    print("\n======================================")
    print("       STUDENT PERFORMANCE REPORT")
    print("======================================")

    print("Name:", name)
    print("Roll No:", roll_no)

    print("\nSubject Marks:")

    for i in range(len(subjects)):
        print(subjects[i], ":", marks[i])

    print("\nTotal Marks:", total)
    print("Average:", average)
    print("Percentage:", percentage)
    print("Grade:", grade)
    print("Result:", result)
    print("Attendance:", attendance, "%")
    print("Attendance Status:", attendance_status)
    print("Highest Subject:", highest_subject)
    print("Lowest Subject:", lowest_subject)

    print("======================================")
    