📒 FINTRACK PRO - Finance Manager (CLI)

FINTRACK PRO is a simple command-line project made using Python.
It helps you store expenses, organize them by category, and check monthly budget limits using a local database.

This project is mainly for learning Python + databases.

🧩 What This Project Does

Save expense categories (Food, Travel, Shopping, etc.)

Add daily expenses

Update or delete expenses

Search expenses by date

Show total expense for each category

Set a monthly budget

Warn when budget is exceeded

🛠️ Tools Used

Python

SQLAlchemy

SQLite (database file)

No internet or server needed.
Everything runs on your computer.

📁 Files in This Project
fintrack.py   → main program
fintrack.db   → database file (created automatically)
README.md     → project explanation

▶️ How to Run This Project
Step 1: Install SQLAlchemy
pip install sqlalchemy

Step 2: Run the Program
python fintrack.py


The database file will be created automatically.

📋 Menu Options Explained
1. Add Category        → Add Food, Travel, etc.
2. Add Expense         → Add money spent
3. Update Expense      → Change expense amount
4. Delete Expense      → Remove an expense
5. Search by Date      → View expenses on a date
6. Category Report     → Total expense per category
7. Set Budget          → Monthly spending limit
8. Budget Alert        → Check if limit crossed
9. Exit                → Close program

🧠 How This Project Works (Simple)

Python takes user input

SQLAlchemy saves data into SQLite database

Tables are created automatically

Expenses are linked to categories

SQL is used to calculate total expenses

Budget is checked using monthly data

🧪 Example

Category: Food

Expense: Lunch – ₹120

Month: 2026-02

Budget limit: ₹3000

If expenses go above ₹3000 → ⚠️ budget alert shown

🎓 Why This Project Is Useful

This project helps you learn:

Python basics

Database concepts

CRUD operations (Add, View, Update, Delete)

SQL + ORM

Logical thinking
