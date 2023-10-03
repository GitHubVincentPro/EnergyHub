import sqlite3

def get_connection():
conn = sqlite3.connect('database.db')
conn.row_factory = sqlite3.Row
return conn

def execute_query(query, parameters=()):
conn = get_connection()
cursor = conn.cursor()
cursor.execute(query, parameters)
conn.commit()

def select_all(query, parameters=()):
conn = get_connection()
cursor = conn.cursor()
cursor.execute(query, parameters)
return cursor.fetchall()

# Usage:

query = "SELECT * FROM forecasts WHERE date=?"
forecasts = select_all(query, ('2022-01-01',))