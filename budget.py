#a basic budget management system that allows adding expenses and calculating total expenses by category. 
#It highlights the use of classes, objects, methods
#data encapsulation in organizing and managing budget-related data within an application.

#we will start by defining the classs#
class Expense:
    def __init__(self, description, amount, category):
        self.description = description
        self.amount = amount
        self.category = category
#creates instance budget mng class#
class BudgetManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount, category):
        expense = Expense(description, amount, category)
        self.expenses.append(expense)
        print(f"Added expense: {description}, Amount: ${amount}, Category: {category}")

    def calculate_total_expenses(self):
        category_totals = {}
        for expense in self.expenses:
            if expense.category in category_totals:
                category_totals[expense.category] += expense.amount
            else:
                category_totals[expense.category] = expense.amount
        return category_totals

    def display_total_expenses(self):
        totals = self.calculate_total_expenses()
        print("\nTotal Expenses by Category:")
        for category, total_amount in totals.items():
             print(f"{category}: Ksh{total_amount}")


# Example Usage:
if __name__ == "__main__":
    budget_manager = BudgetManager()

    # Adding expenses
    budget_manager.add_expense("Groceries", 10000, "Food")
    budget_manager.add_expense("Dinner at Restaurant", 8000, "Food")
    budget_manager.add_expense("Gasoline", 5000, "Transportation")
    budget_manager.add_expense("Movie Tickets", 3000, "Entertainment")
    budget_manager.add_expense("Books", 3500, "Education")

    # Displaying total expenses by category
    budget_manager.display_total_expenses()
    
    #the followng code is the same but with inclusion of an input function
    class Expense:
        def __init__(self, description, amount, category):
            self.description = description
            self.amount = amount
            self.category = category

class BudgetManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount, category):
        expense = Expense(description, amount, category)
        self.expenses.append(expense)
        print(f"Added expense: {description}, Amount: ${amount}, Category: {category}")

    def calculate_total_expenses(self):
        category_totals = {}
        for expense in self.expenses:
            if expense.category in category_totals:
                category_totals[expense.category] += expense.amount
            else:
                category_totals[expense.category] = expense.amount
        return category_totals

    def display_total_expenses(self):
        totals = self.calculate_total_expenses()
        print("\nTotal Expenses by Category:")
        for category, total_amount in totals.items():
            print(f"{category}: ${total_amount}")

def get_user_input():
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    return description, amount, category

# Example Usage:
if __name__ == "__main__":
    budget_manager = BudgetManager()

    # Adding expenses using user input
    while True:
        print("\nEnter expense details (or 'q' to quit):")
        description, amount, category = get_user_input()
        if description.lower() == 'q':
            break
        budget_manager.add_expense(description, amount, category)

    # Displaying total expenses by category
    budget_manager.display_total_expenses()
