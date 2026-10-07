def calculate_percentage(total, maximum_marks):
    return (total / maximum_marks) * 100

def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

def check_result(marks):

    for mark in marks:
        if mark < 40:
            return "FAIL"

    return "PASS"

def find_highest_subject(subjects, marks):
    highest_index = marks.index(max(marks))
    return subjects[highest_index]

def find_lowest_subject(subjects, marks):
    lowest_index = marks.index(min(marks))
    return subjects[lowest_index]

subjects = [
    "Python",
    "Maths",
    "English",
    "Physics",
    "EVS"
]

def attendance_status(attendance):

    if attendance >= 75:
        return "Good"
    else:
        return "Low"

def find_highest_subject(subjects, marks):
    highest_index = marks.index(max(marks))
    return subjects[highest_index]


def find_lowest_subject(subjects, marks):
    lowest_index = marks.index(min(marks))
    return subjects[lowest_index]

def check_attendance(attendance):
    if attendance >= 75:
        return "Eligible"
    else:
        return "Not Eligible"

def calculate_class_average(students):

    if len(students) == 0:
        return 0

    total_percentage = 0

    for student in students:
        total_percentage += float(student["Percentage"])

    return total_percentage / len(students)