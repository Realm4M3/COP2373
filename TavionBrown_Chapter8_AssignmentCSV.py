import csv

def write_grades_to_csv():

# Typing in on how much students you want
    num_students = int(input("Enter number of students: "))
    
# Opening the CVS file as w
    with open('grades.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])
        
        for i in range(1, num_students + 1):
# Typing in your name and the scores for the exam
            first_name = input(f"Enter first name of student {i}: ")
            last_name = input(f"Enter last name of student {i}: ")
            exam1 = int(input(f"Enter exam 1 grade for {first_name} {last_name}: "))
            exam2 = int(input(f"Enter exam 2 grade for {first_name} {last_name}: "))
            exam3 = int(input(f"Enter exam 3 grade for {first_name} {last_name}: "))
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

# Printing out the results           
        print(f"{num_students} records have been written to grades.csv")

def read_grades_from_csv():

# Opening the read file
    with open('grades.csv', mode='r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        
        print("{:<15} {:<15} {:<8} {:<8} {:<8}".format(*headers))
        print("="*54)
        
        for row in reader:
            print("{:<15} {:<15} {:<8} {:<8} {:<8}".format(*row))

if __name__ == "__main__":
    while True:

# A loop depending on the choice you pick
        choice = input("Enter 'w' to write grades to CSV, 'r' to read grades from CSV, or 'q' to quit: ").lower()
        if choice == 'w':
            write_grades_to_csv()
        elif choice == 'r':
            read_grades_from_csv()
        elif choice == 'q':
            break
        else:
# Result if you dont pick the right choice
            print("Invalid choice. Please enter 'w', 'r', or 'q'.")
