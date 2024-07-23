# Zach Alderete
# Lab 11 - Question 9.3
# 7/22/24.
# Program collects student's first name, last name, and 3 exam grades based on user input. Format per 9.3 csv example. 
# Ensure grades are between 0-100. Can be adjusted as needed. 


import csv

# Open the file 'grades.csv' in write mode
with open('grades.csv', mode='w', newline='') as grades:
    # Create a CSV writer
    writer = csv.writer(grades)
    
    # Write the header row to the CSV file per 9.3 exercise
    writer.writerow(['firstname', 'lastname', 'exam1grade', 'exam2grade', 'exam3grade'])
    
    while True:
        # Prompt for the student's first name
        first_name = input("Enter the student's first name (or type 'done' to finish): ")
        
        # Verify if user is done
        if first_name.lower() == 'done':
            break
        
        # Prompt for the student's last name
        last_name = input("Enter the student's last name: ")
        
        # Prompt for three exam grades and validate them as integers within the range 0-100. 
        while True:
            try:
                exam1 = int(input("Enter the grade for exam 1 (0-100): "))
                if 0 <= exam1 <= 100:
                    break
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid integer for exam 1.")

        while True:
            try:
                exam2 = int(input("Enter the grade for exam 2 (0-100): "))
                if 0 <= exam2 <= 100:
                    break
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid integer for exam 2.")
        
        while True:
            try:
                exam3 = int(input("Enter the grade for exam 3 (0-100): "))
                if 0 <= exam3 <= 100:
                    break
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid integer for exam 3.")
        
        # Write the student's record to the CSV file
        writer.writerow([first_name, last_name, exam1, exam2, exam3])

print("Student records have been written to grades.csv")
