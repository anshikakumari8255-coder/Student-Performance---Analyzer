class Student:

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_student(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)