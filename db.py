import sqlite3, pandas as pd
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / "data/processed/pocketsmart.db"

def _conn():
    c = sqlite3.connect(DB)
    c.execute("""CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, description TEXT,
        amount REAL, category TEXT)""")
    return c

def add_expense(date, description, amount, category):
    with _conn() as c:
        c.execute("INSERT INTO expenses(date,description,amount,category) VALUES(?,?,?,?)",
                  (str(date), description, amount, category))

def get_expenses():
    with _conn() as c:
        return pd.read_sql("SELECT * FROM expenses ORDER BY date DESC", c)
