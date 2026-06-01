# =========================================================
# SMART CAMPUS INFORMATION SYSTEM
# =========================================================

import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =========================================================
# GLOBAL VARIABLES
# =========================================================

students = []
record_file = "student_records.json"

# =========================================================
# FUNCTION: Calculate Grade
# =========================================================

def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

# =========================================================
# FUNCTION: Fee Calculation
# =========================================================

def calculate_fee(num_courses):
    fee_per_course = 5000
    lab_fee = 2000
    total_fee = (num_courses * fee_per_course) + lab_fee
    return total_fee

# =========================================================
# FUNCTION: Register Student
# =========================================================

def register_student():
    print("\n===== Student Registration =====")

    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))

    num_courses = int(input("Enter Number of Courses: "))

    courses = []
    marks = []

    for i in range(num_courses):
        course = input(f"Enter Course {i+1} Name: ")
        mark = float(input(f"Enter Marks for {course}: "))

        courses.append(course)
        marks.append(mark)

    average = sum(marks) / len(marks)
    grade = calculate_grade(average)
    fee = calculate_fee(num_courses)

    student = {
        "ID": student_id,
        "Name": name,
        "Age": age,
        "Courses": courses,
        "Marks": marks,
        "Average": average,
        "Grade": grade,
        "Fee": fee
    }

    students.append(student)

    print("\nStudent Registered Successfully!")
    print("Average Marks:", average)
    print("Grade:", grade)
    print("Total Fee:", fee)

# =========================================================
# FUNCTION: Display Students
# =========================================================

def display_students():
    print("\n===== Student Records =====")

    if not students:
        print("No student records found.")
        return

    for student in students:
        print("\n-----------------------------")
        print("ID:", student["ID"])
        print("Name:", student["Name"])
        print("Age:", student["Age"])
        print("Courses:", ", ".join(student["Courses"]))
        print("Marks:", student["Marks"])
        print("Average:", round(student["Average"], 2))
        print("Grade:", student["Grade"])
        print("Fee:", student["Fee"])

# =========================================================
# FUNCTION: Search Student
# =========================================================

def search_student():
    print("\n===== Search Student =====")

    sid = input("Enter Student ID to Search: ")

    found = False

    for student in students:
        if student["ID"] == sid:
            print("\nStudent Found")
            print(student)
            found = True
            break

    if not found:
        print("Student not found.")

# =========================================================
# FUNCTION: Sort Students
# =========================================================

def sort_students():
    print("\n===== Sort Students by Average Marks =====")

    if not students:
        print("No student data available.")
        return

    sorted_students = sorted(students, key=lambda x: x["Average"], reverse=True)

    for student in sorted_students:
        print(student["Name"], "-", round(student["Average"], 2))

# =========================================================
# FUNCTION: Save Records to File
# =========================================================

def save_records():
    with open(record_file, "w") as file:
        json.dump(students, file, indent=4)

    print("\nRecords saved successfully.")

# =========================================================
# FUNCTION: Load Records from File
# =========================================================

def load_records():
    global students

    try:
        with open(record_file, "r") as file:
            students = json.load(file)

        print("\nRecords loaded successfully.")

    except FileNotFoundError:
        print("\nNo previous records found.")

# =========================================================
# FUNCTION: Directory Scanning with Exception Handling
# =========================================================

def scan_directory():
    print("\n===== Directory Scanner =====")

    path = input("Enter directory path: ")

    try:
        files = os.listdir(path)

        print("\nFiles and Folders:")

        for file in files:
            print(file)

    except FileNotFoundError:
        print("Directory not found.")

    except PermissionError:
        print("Permission denied.")

    except Exception as e:
        print("Error:", e)

# =========================================================
# FUNCTION: Performance Analytics using NumPy & Pandas
# =========================================================

def performance_analytics():
    print("\n===== Student Performance Analytics =====")

    if not students:
        print("No student data available.")
        return

    data = {
        "Name": [],
        "Average": [],
        "Grade": []
    }

    for student in students:
        data["Name"].append(student["Name"])
        data["Average"].append(student["Average"])
        data["Grade"].append(student["Grade"])

    df = pd.DataFrame(data)

    print("\nStudent DataFrame")
    print(df)

    averages = np.array(data["Average"])

    print("\n===== Statistical Analysis =====")
    print("Highest Average:", np.max(averages))
    print("Lowest Average:", np.min(averages))
    print("Mean Average:", np.mean(averages))
    print("Median Average:", np.median(averages))

    # ==========================
