#!/usr/bin/env python3
# Author ID: vvsuratwala

class Student:

    # Define the name and number when a student object is created
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)  # Ensures student number is always a string
        self.courses = {}

    # Return student name and number
    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + self.number

    # Add a new course and grade to student's record
    def addGrade(self, course, grade):
        self.courses[course] = grade

    # Calculate the GPA of all courses and return a string
    def displayGPA(self):
        total = 0.0
        count = 0
        for grade in self.courses.values():
            if grade > 0.0:
                total += grade
                count += 1
        if count == 0:
            return 'GPA of student ' + self.name + ' is 0.0'
        return 'GPA of student ' + self.name + ' is ' + str(total / count)

    # Return a list of courses the student passed (grade > 0.0)
    def displayCourses(self):
        passed_courses = [course for course, grade in self.courses.items() if grade > 0.0]
        return passed_courses


if __name__ == '__main__':
    # Create first student object and add grades
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student object and add grades
    student2 = Student('Jessica', 123456)  # This now works even as an integer
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Display student1 info
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Display student2 info
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())
