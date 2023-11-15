# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   JRideout,11/15/2023,Created Script
#   <Joseph Rideout>,<11/15/2023>, <Created Script>
# ------------------------------------------------------------------------------------------ #
import json
import os
# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
menu_choice: str  # Hold the choice made by the user.
students: list[dict[str, str]] = []  
file = None

# When the program starts, read the file data into a list of dictionaries
# Extract the data from the file
try:
    with open(FILE_NAME, "r") as file:
        students = json.load(file)
        for item in students:
            print(f'ID:{item["first_name"]}, name:{item["last_name"]}, course:{item["course"]}')
except FileNotFoundError as e:
    print('Text file must exist before running script.\n')
    print('--Technical Error Message--')
    print(e, e.__doc__, type(e), sep='\n')

# Present and Process the data
while True:
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":
        student_first_name = input("Enter the student's first name: ")
        student_last_name = input("Enter the student's last name: ")
        course_name = input("Please enter the name of the course: ")
        student_row: dict[str, str] = {
            'first_name': student_first_name,
            'last_name': student_last_name,
            'course': course_name
        }
        students.append(student_row)
        continue

    # Present the current data
    elif menu_choice == "2":
        print("-" * 50)
        for student in students:
            print(f"Student {student['first_name']} {student['last_name']} is enrolled in {student['course']}")
        print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            with open(FILE_NAME, 'w') as file:
                json.dump(students, file)
            print("Data saved successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")
            print(e, e.__doc__, type(e), sep='\n')
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
