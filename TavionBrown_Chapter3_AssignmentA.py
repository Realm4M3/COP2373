from functools import reduce

def get_expenses():
    expenses = []
    while True:
# In a loop until you type in done
        expense_type = input("Enter the type of expense (or 'done' to finish): ")
        if expense_type.lower() == 'done':
            break
        try:
# Enter the amount for the expense
            amount = float(input(f"Enter the amount for {expense_type}: "))
            expenses.append((expense_type, amount))
        except ValueError:
# Display error if it's not a number
            print("Invalid number. Please enter a number.")
    return expenses

# Only if you type in nothing for the expenses
def analyze_expenses(expenses):
    if not expenses:
        print("No expenses at all.")
        return

# Calculating the total, the highest, and the lowest expenses using reduce
    total_expense = reduce(lambda acc, expense: acc + expense[1], expenses, 0)
    highest_expense = reduce(lambda acc, expense: expense if expense[1] > acc[1] else acc, expenses)
    lowest_expense = reduce(lambda acc, expense: expense if expense[1] < acc[1] else acc, expenses)

# Print out the results
    print(f"\nTotal expense: ${total_expense:.2f}")
    print(f"Highest expense: {highest_expense[0]} - ${highest_expense[1]:.2f}")
    print(f"Lowest expense: {lowest_expense[0]} - ${lowest_expense[1]:.2f}")

# Main function
def main():
    expenses = get_expenses()
    analyze_expenses(expenses)

if __name__ == "__main__":
    main()
