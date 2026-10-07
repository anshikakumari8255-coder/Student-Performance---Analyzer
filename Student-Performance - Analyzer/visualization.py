import matplotlib.pyplot as plt

def show_marks_chart(subjects, marks):

    plt.bar(subjects, marks)

    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.title("Student Subject-wise Performance")

    plt.ylim(0, 100)

    plt.show()

def show_student_percentage_chart(students):

    names = []
    percentages = []

    for student in students:
        names.append(student["Name"])
        percentages.append(float(student["Percentage"]))

    plt.bar(names, percentages)

    plt.xlabel("Students")
    plt.ylabel("Percentage")
    plt.title("Student Percentage Comparison")

    plt.ylim(0, 100)

    plt.show()

def show_class_average_chart(students):

    names = []
    percentages = []

    for student in students:
        names.append(student["Name"])
        percentages.append(float(student["Percentage"]))

    class_average = sum(percentages) / len(percentages)

    plt.bar(["Class Average"], [class_average])

    plt.xlabel("Performance")
    plt.ylabel("Percentage")
    plt.title("Class Average Performance")

    plt.ylim(0, 100)

    plt.show()