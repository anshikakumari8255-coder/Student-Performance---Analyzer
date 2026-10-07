from analyzer import (
    calculate_percentage,
    calculate_grade,
    check_result,
    find_highest_subject,
    find_lowest_subject,
    check_attendance
)


# Test percentage calculation
assert calculate_percentage(450, 500) == 90


# Test grade calculation
assert calculate_grade(90) == "A+"


# Test pass/fail result
assert check_result([80, 75, 90, 85, 88]) == "PASS"


# Test highest subject
subjects = ["Python", "Maths", "English", "Physics", "EVS"]
marks = [80, 75, 90, 85, 88]

assert find_highest_subject(subjects, marks) == "English"


# Test lowest subject
assert find_lowest_subject(subjects, marks) == "Maths"


# Test attendance
assert check_attendance(80) == "Eligible"
assert check_attendance(70) == "Not Eligible"


print("All tests passed successfully!")

print("Testing completed successfully.")