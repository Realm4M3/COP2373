import csv
import numpy as np

# Function to write student grades to a CSV file
def write_grades_to_csv():
    # Prompting user for the number of students
    num_students = int(input("Enter number of students: "))
    # Opening the CSV file in write mode
    with open('grades.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Writing the header row
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])
        # Looping through the number of students to get their details
        for i in range(1, num_students + 1):
            first_name = input(f"Enter first name of student {i}: ")
            last_name = input(f"Enter last name of student {i}: ")
            exam1 = int(input(f"Enter exam 1 grade for {first_name} {last_name}: "))
            exam2 = int(input(f"Enter exam 2 grade for {first_name} {last_name}: "))
            exam3 = int(input(f"Enter exam 3 grade for {first_name} {last_name}: "))
            # Writing the student's details to the CSV file
            writer.writerow([first_name, last_name, exam1, exam2, exam3])
        # Confirming that the records have been written
        print(f"{num_students} records have been written to grades.csv")

# Function to read and print student grades from the CSV file
def read_grades_from_csv():
    # Opening the CSV file in read mode
    with open('grades.csv', mode='r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Reading the header row
        # Printing the header row with formatted columns
        print("{:<15} {:<15} {:<8} {:<8} {:<8}".format(*headers))
        print("="*54)
        # Reading and printing each row of data
        for row in reader:
            print("{:<15} {:<15} {:<8} {:<8} {:<8}".format(*row))

# Function to analyze student grades using numpy
def analyze_grades_with_numpy():
    # Loading data from the CSV file into a numpy array, skipping the header
    data = np.genfromtxt('grades.csv', delimiter=',', skip_header=1, usecols=(2, 3, 4))
    # Printing the first few rows of the dataset
    print("First few rows of the dataset:")
    print(data[:5])
    
    exams = ["Exam 1", "Exam 2", "Exam 3"]
    
    # Calculating and printing statistics for each exam
    for i in range(data.shape[1]):
        print(f"\nStatistics for {exams[i]}:")
        print(f"Mean: {np.mean(data[:, i])}")
        print(f"Median: {np.median(data[:, i])}")
        print(f"Standard Deviation: {np.std(data[:, i])}")
        print(f"Minimum: {np.min(data[:, i])}")
        print(f"Maximum: {np.max(data[:, i])}")
    
    # Calculating and printing overall statistics for all exams combined
    print("\nOverall statistics for all exams combined:")
    print(f"Mean: {np.mean(data)}")
    print(f"Median: {np.median(data)}")
    print(f"Standard Deviation: {np.std(data)}")
    print(f"Minimum: {np.min(data)}")
    print(f"Maximum: {np.max(data)}")
    
    pass_grade = 60
    # Determining and printing the number of students who passed and failed each exam
    for i in range(data.shape[1]):
        passed = np.sum(data[:, i] >= pass_grade)
        failed = np.sum(data[:, i] < pass_grade)
        print(f"\n{exams[i]}: {passed} passed, {failed} failed")
    
    # Calculating and printing the overall pass percentage across all exams
    total_exams = data.size
    total_passes = np.sum(data >= pass_grade)
    overall_pass_percentage = (total_passes / total_exams) * 100
    print(f"\nOverall pass percentage across all exams: {overall_pass_percentage:.2f}%")

# Main function to run the program
if __name__ == "__main__":
    while True:
        # Asking the user to choose an option
        choice = input("Enter 'w' to write grades to CSV, 'r' to read grades from CSV, 'a' to analyze grades with numpy, or 'q' to quit: ").lower()
        if choice == 'w':
            write_grades_to_csv()
        elif choice == 'r':
            read_grades_from_csv()
        elif choice == 'a':
            analyze_grades_with_numpy()
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please enter 'w', 'r', 'a', or 'q'.")
