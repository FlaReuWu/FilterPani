import sqlite3

conn = sqlite3.connect("database.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
password TEXT
)
""")

# Default users
conn.execute("INSERT INTO users (username, password) VALUES ('Papa', '1234')")
conn.execute("INSERT INTO users (username, password) VALUES ('Lakshya', '1234')")

conn.commit()

print("Users table created")

conn.close()
