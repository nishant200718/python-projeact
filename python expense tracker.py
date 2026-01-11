
expenses = [] 

def add_expense():
    """Function to add a new expense"""
    category = input("Enter category (e.g. Food, Travel, Study): ")
    amount = float(input("Enter amount: "))
    expenses.append({"category": category, "amount": amount})
    print("Expense added successfully!\n")

def view_expenses():
    """Function to view all expenses"""
    if not expenses:
        print("No expenses recorded yet.\n")
    else:
        print("\n--- All Expenses ---")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. {expense['category']} - ₹{expense['amount']}")
        print()

def total_expenses():
    """Function to calculate total expenses"""
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal Expenses: ₹{total}\n")

def main():
    """Main program loop"""
    while True:
        print("Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("Exiting... Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice! Please try again.\n")

main()
