import sqlite3
import csv
from datetime import datetime

# Initialize database
DB_FILE = "transactions.db"


def main():
    """
    Main function to display the menu and handle user input.
    """
    _init_db()
    print("\n=== Budget Tracker ===")
    while True:
        print("\nMenu:")
        print("1. Add Transaction")
        print("2. Generate Report")
        print("3. Export Data to CSV")
        print("4. Manage Transactions")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            generate_report()
        elif choice == "3":
            export_data_to_csv()
        elif choice == "4":
            manage_transactions()
        elif choice == "5":
            print("Exiting Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def _init_db():
    """
    Initializes the SQLite database.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY,
            date TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def add_transaction():
    """
    Adds a new transaction (income or expense) to the database.
    """
    print("\n=== Add Transaction ===")
    amount = float(input("Enter amount (positive for income, negative for expense): "))
    category = input("Enter category (e.g., Food, Rent, Utilities): ").strip()
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (date, amount, category) VALUES (?, ?, ?)",
                   (date, amount, category))
    conn.commit()
    conn.close()
    print("Transaction added successfully!")


def generate_report():
    """
    Generates a summary report of transactions by category and total balance.
    Allows filtering by a date range.
    """
    print("\n=== Generate Report ===")
    start_date = input("Enter start date (YYYY-MM-DD) or press Enter to skip: ").strip()
    end_date = input("Enter end date (YYYY-MM-DD) or press Enter to skip: ").strip()

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    query = "SELECT date, amount, category FROM transactions"
    if start_date or end_date:
        query += " WHERE 1=1"
        if start_date:
            query += f" AND date >= '{start_date}'"
        if end_date:
            query += f" AND date <= '{end_date}'"
    cursor.execute(query)
    transactions = cursor.fetchall()
    conn.close()

    total_balance = 0
    category_totals = {}
    for date, amount, category in transactions:
        total_balance += amount
        category_totals[category] = category_totals.get(category, 0) + amount

    print("\nTransaction Summary:")
    for category, total in category_totals.items():
        print(f"{category}: ${total: .2f}")
    print(f"\nTotal Balance: ${total_balance: .2f}")


def export_data_to_csv():
    """
    Exports all transaction data to a CSV file.
    """
    print("\n=== Export Data to CSV ===")
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, date, amount, category FROM transactions")
    transactions = cursor.fetchall()
    conn.close()

    if not transactions:
        print("No transactions found to export.")
        return

    # Specify the CSV file name
    file_name = "transactions_report.csv"

    # Open the CSV file in write mode
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(["ID", "Date", "Amount", "Category"])

        # Write the transaction data
        for transaction in transactions:
            writer.writerow(transaction)

    print(f"Data exported successfully to {file_name}")


def manage_transactions():
    """
    Allows the user to view, edit, or delete transactions.
    """
    print("\n=== Manage Transactions ===")
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, date, amount, category FROM transactions")
    transactions = cursor.fetchall()
    conn.close()

    if not transactions:
        print("No transactions found.")
        return

    for idx, (tid, date, amount, category) in enumerate(transactions):
        print(f"{idx + 1}. {date} - ${amount} ({category}) [ID: {tid}]")

    choice = input("\nEnter transaction number to edit/delete, or press Enter to cancel: ").strip()
    if not choice.isdigit():
        print("Cancelled.")
        return

    choice = int(choice) - 1
    if choice < 0 or choice >= len(transactions):
        print("Invalid selection.")
        return

    transaction_id = transactions[choice][0]
    action = input("Enter 'e' to edit or 'd' to delete: ").strip().lower()

    if action == 'e':
        edit_transaction(transaction_id)
    elif action == 'd':
        delete_transaction(transaction_id)
    else:
        print("Invalid action. Returning to menu.")


def edit_transaction(transaction_id):
    """
    Edits a selected transaction.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT date, amount, category FROM transactions WHERE id = ?", (transaction_id,))
    date, amount, category = cursor.fetchone()

    new_date = input(
        f"Enter new date (YYYY-MM-DD) or press Enter to keep [{date}]: ").strip() or date
    new_amount = input(f"Enter new amount or press Enter to keep [{amount}]: ").strip() or amount
    new_category = input(f"Enter new category or press Enter to keep [{
                         category}]: ").strip() or category

    cursor.execute("UPDATE transactions SET date = ?, amount = ?, category = ? WHERE id = ?",
                   (new_date, new_amount, new_category, transaction_id))
    conn.commit()
    conn.close()
    print("Transaction updated successfully!")


def delete_transaction(transaction_id):
    """
    Deletes a selected transaction.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
    conn.commit()
    conn.close()
    print("Transaction deleted successfully!")


if __name__ == "__main__":
    main()
