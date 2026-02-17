# Expense Tracker

A Python expense tracking system that manages personal expenses using dictionaries for data organization.

## Features

- Add new expenses with category, amount, and date
- View all expenses in organized format  
- Filter expenses by category
- Calculate total expenses with category breakdown
- Delete specific expenses by ID
- Input validation and error handling

## Installation

**Requirements:**
- Python 3.7 or higher

**Setup:**
```bash
git clone https://github.com/coolrack/expensetracker.git
cd expensetracker
python expense_tracker.py
```

## Usage

Run the program and select from the menu:

1. Add new expense - Enter category, amount, and date
2. View all expenses - Display all recorded expenses
3. Filter by category - View expenses for specific category
4. Calculate totals - See total spending by category
5. Delete expense - Remove an expense by ID
6. Exit - Close the program

## Team Roles & Responsibilities

Originally worked with a group where I learned collaborative development practices including Git workflows, code reviews, and pull requests. When the team completed early, I rebuilt the project independently to ensure understanding of all components.

**Features implemented:**
- Adding expenses with validation
- Viewing and filtering functionality
- Total calculations with category breakdown
- Expense deletion with confirmation
- Error handling throughout

## Technical Details

**Data Structure:**
```python
expenses = {
    1: {'category': 'Food', 'amount': 45.50, 'date': '2026-02-05'},
    2: {'category': 'Transport', 'amount': 15.00, 'date': '2026-02-04'}
}
```

**Features:**
- Dictionary-based storage for efficient data management
- Input validation prevents invalid data entry
- Error handling ensures program stability
- Formatted output for clear expense display
- Case-insensitive category filtering

## Challenges & Solutions

**Data Validation**
- Challenge: Users could enter invalid amounts or dates
- Solution: Implemented try-except blocks and input validation for all user inputs

**Category Consistency**
- Challenge: Same category entered with different capitalization
- Solution: Used .title() method to standardize category names

**User Experience**
- Challenge: Clear display of information
- Solution: Formatted tables and organized output with visual separators

**Error Handling**
- Challenge: Program would crash on invalid inputs
- Solution: Comprehensive error checking with helpful error messages

## Reflection

Working collaboratively taught me Git workflows, code organization, and team coordination. Rebuilding independently reinforced my understanding of all features and improved my problem-solving skills. Both approaches have value - collaboration teaches professional practices while independent work ensures mastery of concepts.

## License

MIT

---

Repository: https://github.com/coolrack/expensetracker
