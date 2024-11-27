import sqlite3
import os
import csv
from unittest.mock import patch
from project import _init_db, add_transaction, generate_report, export_data_to_csv


def test_add_transaction():
    _init_db()
    conn = sqlite3.connect("transactions.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transactions")
    conn.commit()

    # Mock user input for add_transaction()
    with patch('builtins.input', side_effect=[100.0, 'Test1', '2024-11-27']):
        add_transaction()

    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    assert len(transactions) == 1


def test_generate_report(capsys):
    _init_db()
    conn = sqlite3.connect("transactions.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transactions")
    cursor.execute("INSERT INTO transactions (date, amount, category) VALUES (?, ?, ?)",
                   ("2024-11-27", 100, "Test"))
    conn.commit()

    # Mock user input for generate_report()
    with patch('builtins.input', side_effect=['2024-11-01', '2024-11-30']):
        generate_report()

    captured = capsys.readouterr()
    assert "Test" in captured.out


def test_export_data_to_csv():
    # Initialize the database and add some transactions
    _init_db()
    conn = sqlite3.connect("transactions.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transactions")  # Clean up any existing data
    cursor.execute("INSERT INTO transactions (date, amount, category) VALUES (?, ?, ?)",
                   ("2024-11-27", 100, "Test1"))
    cursor.execute("INSERT INTO transactions (date, amount, category) VALUES (?, ?, ?)",
                   ("2024-11-28", -50, "Test2"))
    conn.commit()

    # Call the export function
    export_data_to_csv()

    # Check if the file was created
    assert os.path.exists("transactions_report.csv")

    # Now check the contents of the CSV file
    with open("transactions_report.csv", mode="r") as file:
        reader = csv.reader(file)
        headers = next(reader)  # Skip the header row
        rows = list(reader)

    # Assert the correct data is in the CSV
    assert len(rows) == 2  # Should have 2 transactions in the file
    assert rows[0][0] == '1'  # Check the ID of the first transaction
    assert rows[0][1] == '2024-11-27'  # Date of the first transaction
    assert float(rows[0][2]) == 100.0  # Amount of the first transaction as float
    assert rows[0][3] == 'Test1'  # Category of the first transaction
    assert rows[1][0] == '2'  # Check the ID of the second transaction
    assert rows[1][1] == '2024-11-28'  # Date of the second transaction
    assert float(rows[1][2]) == -50.0  # Amount of the second transaction as float
    assert rows[1][3] == 'Test2'  # Category of the second transaction

    # Clean up: Remove the CSV file after the test to maintain a clean environment
    os.remove("transactions_report.csv")
