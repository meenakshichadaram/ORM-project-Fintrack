# =====================================
# FINTRACK PRO - CLI FINANCE MANAGER
# =====================================

# ---------- IMPORTS ----------
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, text
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# ---------- DATABASE CONNECTION ----------
engine = create_engine("sqlite:///fintrack.db", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# ---------- TABLE DEFINITIONS ----------
class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    expenses = relationship("Expense", back_populates="category")

class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    amount = Column(Float)
    date = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="expenses")

class Subscription(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(Float)
    next_date = Column(String)

class Budget(Base):
    __tablename__ = "budgets"
    id = Column(Integer, primary_key=True)
    month = Column(String)
    limit = Column(Float)

Base.metadata.create_all(engine)

# ---------- FUNCTIONS ----------
def add_category():
    name = input("Category name: ")
    session.add(Category(name=name))
    session.commit()
    print("Category added")

def add_expense():
    title = input("Expense title: ")
    amount = float(input("Amount: "))
    date = input("Date (YYYY-MM-DD): ")
    category_id = int(input("Category ID: "))
    session.add(Expense(title=title, amount=amount, date=date, category_id=category_id))
    session.commit()
    print("Expense added")

def update_expense():
    eid = int(input("Expense ID: "))
    expense = session.query(Expense).filter(Expense.id == eid).first()
    if expense:
        expense.amount = float(input("New amount: "))
        session.commit()
        print("Expense updated")
    else:
        print("Expense not found")

def delete_expense():
    eid = int(input("Expense ID: "))
    expense = session.query(Expense).filter(Expense.id == eid).first()
    if expense:
        session.delete(expense)
        session.commit()
        print("Expense deleted")
    else:
        print("Expense not found")

def search_by_date():
    date = input("Enter date: ")
    expenses = session.query(Expense).filter(Expense.date == date).all()
    for e in expenses:
        print(e.title, "-", e.amount)

# ---------- RAW SQL REPORT ----------
def category_report():
    sql = """
    SELECT categories.name, SUM(expenses.amount)
    FROM categories
    JOIN expenses ON categories.id = expenses.category_id
    GROUP BY categories.name
    """
    result = session.execute(text(sql))
    print("\nCategory Wise Expense Report")
    for row in result:
        print(row[0], "->", row[1])

def set_budget():
    month = input("Month (YYYY-MM): ")
    limit = float(input("Monthly limit: "))
    session.add(Budget(month=month, limit=limit))
    session.commit()
    print("Monthly budget set")

def budget_alert():
    month = input("Month (YYYY-MM): ")
    total = session.execute(
        text("SELECT SUM(amount) FROM expenses WHERE date LIKE :m"),
        {"m": f"{month}%"}
    ).scalar()
    budget = session.query(Budget).filter(Budget.month == month).first()
    if budget and total and total > budget.limit:
        print("Budget limit exceeded")
    else:
        print("Within budget")

# ---------- CLI MENU ----------
while True:
    print("""
===== FINTRACK PRO =====
1. Add Category
2. Add Expense
3. Update Expense
4. Delete Expense
5. Search Expense by Date
6. Category Expense Report
7. Set Monthly Budget
8. Budget Alert
9. Exit
""")
    choice = input("Choose: ")
    if choice == "1":
        add_category()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        update_expense()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        search_by_date()
    elif choice == "6":
        category_report()
    elif choice == "7":
        set_budget()
    elif choice == "8":
        budget_alert()
    elif choice == "9":
        break
    else:
        print("Invalid choice")