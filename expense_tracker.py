"""
Expense Tracker Application
A Python program for managing and tracking personal expenses using dictionaries.
"""

from datetime import datetime

# Dictionary to store all expenses
# Structure: {expense_id: {'category': str, 'amount': float, 'date': str}}
expenses = {}
next_id = 1


def add_expense():
    """
    Add a new expense to the tracker.
    Prompts user for category, amount, and date with input validation.
    """
    global next_id
    
    print("\n=== Add New Expense ===")
    
    # Get and validate category
    category = input("Enter category (e.g., Food, Transport): ").strip()
    if not category:
        print("Error: Category cannot be empty.")
        return
    
    # Get and validate amount
    try:
        amount = float(input("Enter amount ($): "))
        if amount <= 0:
            print("Error: Amount must be positive.")
            return
    except ValueError:
        print("Error: Please enter a valid number.")
        return
    
    # Get date (use today if empty)
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if not date:
        date = datetime.now().strftime('%Y-%m-%d')
    else:
        # Validate date format
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            print("Error: Invalid date format. Use YYYY-MM-DD.")
            return
    
    # Store expense in dictionary
    expenses[next_id] = {
        'category': category.title(),
        'amount': amount,
        'date': date
    }
    
    print(f"Expense added successfully (ID: {next_id})")
    next_id += 1


def view_expenses():
    """
    Display all expenses in a formatted table.
    Shows ID, date, category, and amount for each expense.
    """
    if not expenses:
        print("\nNo expenses recorded yet.")
        return
    
    print("\n=== All Expenses ===")
    print(f"{'ID':<5} {'Date':<12} {'Category':<15} {'Amount':>10}")
    print("-" * 45)
    
    # Sort by ID for consistent display
    for exp_id in sorted(expenses.keys()):
        exp = expenses[exp_id]
        print(f"{exp_id:<5} {exp['date']:<12} {exp['category']:<15} ${exp['amount']:>9.2f}")
    
    print(f"\nTotal entries: {len(expenses)}")


def filter_by_category():
    """
    Filter and display expenses by a specific category.
    Shows only expenses matching the entered category.
    """
    if not expenses:
        print("\nNo expenses to filter.")
        return
    
    category = input("\nEnter category to filter: ").strip()
    
    # Filter expenses by category (case-insensitive)
    filtered = {k: v for k, v in expenses.items() 
                if v['category'].lower() == category.lower()}
    
    if not filtered:
        print(f"No expenses found in category '{category}'.")
        return
    
    print(f"\n=== Expenses in '{category.title()}' ===")
    print(f"{'ID':<5} {'Date':<12} {'Amount':>10}")
    print("-" * 30)
    
    total = 0
    for exp_id, exp in filtered.items():
        print(f"{exp_id:<5} {exp['date']:<12} ${exp['amount']:>9.2f}")
        total += exp['amount']
    
    print(f"\nCategory total: ${total:.2f}")


def calculate_total():
    """
    Calculate and display total expenses.
    Shows breakdown by category and overall total.
    """
    if not expenses:
        print("\nNo expenses to calculate.")
        return
    
    print("\n=== Expense Totals ===")
    
    # Calculate totals by category
    category_totals = {}
    for exp in expenses.values():
        cat = exp['category']
        category_totals[cat] = category_totals.get(cat, 0) + exp['amount']
    
    # Display category breakdown
    overall_total = 0
    for category in sorted(category_totals.keys()):
        amount = category_totals[category]
        print(f"{category}: ${amount:.2f}")
        overall_total += amount
    
    print("-" * 30)
    print(f"Overall Total: ${overall_total:.2f}")


def delete_expense():
    """
    Delete a specific expense by ID.
    Includes confirmation before deletion.
    """
    if not expenses:
        print("\nNo expenses to delete.")
        return
    
    # Show all expenses first
    view_expenses()
    
    try:
        exp_id = int(input("\nEnter expense ID to delete: "))
        
        if exp_id in expenses:
            exp = expenses[exp_id]
            print(f"\nDeleting: {exp['category']} - ${exp['amount']:.2f} on {exp['date']}")
            
            confirm = input("Are you sure? (y/n): ").strip().lower()
            if confirm == 'y' or confirm == 'yes':
                del expenses[exp_id]
                print("Expense deleted successfully.")
            else:
                print("Deletion cancelled.")
        else:
            print("Error: Expense ID not found.")
    except ValueError:
        print("Error: Please enter a valid ID number.")


def main():
    """
    Main function to run the expense tracker.
    Displays menu and handles user choices.
    """
    print("Welcome to Expense Tracker")
    print("-" * 30)
    
    while True:
        print("\n" + "=" * 30)
        print("1. Add new expense")
        print("2. View all expenses")
        print("3. Filter by category")
        print("4. Calculate totals")
        print("5. Delete expense")
        print("6. Exit")
        print("=" * 30)
        
        choice = input("\nSelect an option (1-6): ").strip()
        
        # Handle menu choices
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            filter_by_category()
        elif choice == '4':
            calculate_total()
        elif choice == '5':
            delete_expense()
        elif choice == '6':
            print("\nThank you for using Expense Tracker!")
            break
        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    main()
