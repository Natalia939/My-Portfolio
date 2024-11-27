# Budget Tracker Project

#### Video Demo: [https://youtu.be/2-Nf64M1Wv4]

#### Description:

The Budget Tracker Project is a Python-based application that allows users to manage their personal finances effectively. The app utilizes a SQLite database to store transactions, which can be categorized into income and expenses. Users can add new transactions, generate detailed reports, and even export the data to a CSV file for further analysis. Additionally, the application enables users to manage transactions by editing or deleting entries.

The project is designed with simplicity and user-friendliness in mind. It features an easy-to-navigate menu system that lets users perform tasks such as adding transactions, viewing reports, exporting data, and managing their finances with ease.

### Key Features:
- **Add Transactions**: Allows users to input income or expense transactions along with a category and date.
- **Generate Reports**: Displays a summary of transactions by category, including the total balance for a selected date range.
- **Export Data to CSV**: Exports all transactions to a CSV file for further processing or analysis.
- **Manage Transactions**: View, edit, or delete transactions based on transaction ID.

### Files in this Project:

1. **`project.py`**:
    - The main Python script that contains the implementation of the Budget Tracker.
    - It manages the SQLite database, handles user input, and performs operations like adding transactions, generating reports, exporting data, and managing transactions.
    - Includes functions for initializing the database (`_init_db`), adding transactions (`add_transaction`), generating reports (`generate_report`), exporting data to CSV (`export_data_to_csv`), and managing transactions (`manage_transactions`, `edit_transaction`, `delete_transaction`).

2. **`transactions.db`**:
    - The SQLite database that stores all the transaction data. It includes a `transactions` table with columns for `id`, `date`, `amount`, and `category`.

3. **`requirements.txt`**:
    - A file that lists all the Python dependencies required to run the project. For this project, it includes `sqlite3` and any testing libraries, if needed.

4. **`test_project.py`**:
    - The test suite for this project, using the `pytest` framework to ensure that all functions in the `project.py` script work as expected.
    - Contains tests for adding transactions (`test_add_transaction`), generating reports (`test_generate_report`), and exporting data to CSV (`test_export_data_to_csv`).
    - Tests ensure that the database is correctly updated, reports are properly generated, and the CSV export function works as intended.

### Setup Instructions:
To run the project, follow these steps:

1. **Clone the repository**:
    - Use `git clone` to clone the repository to your local machine.

2. **Install dependencies**:
    - Use `pip install -r requirements.txt` to install any required Python libraries (such as `pytest` for testing).

3. **Run the application**:
    - Run the main script with `python project.py` to start the budget tracker. The menu will appear, allowing you to interact with the program.

4. **Running Tests**:
    - To run the tests, use the following command:
      ```bash
      pytest -s test_project.py
      ```
    - The `-s` flag is required to disable output capturing, allowing `input()` functions to work correctly during testing.

### Design Decisions:

- **Database**:
    - I chose to use SQLite as the database because it is lightweight, serverless, and easy to integrate with Python. It stores the transaction data efficiently and allows for quick querying.

- **User Interaction**:
    - The application is designed with simplicity in mind, using a text-based interface where users can navigate through a menu to perform different actions. This makes it accessible even for non-technical users.

- **Export Functionality**:
    - The option to export data to CSV allows users to take their transaction data and use it in spreadsheets or other tools for further analysis.

- **Error Handling**:
    - Basic error handling is implemented to ensure the application functions smoothly. For example, if no transactions are found when trying to export data, the program informs the user rather than crashing.

