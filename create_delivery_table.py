import sqlite3

conn = sqlite3.connect("database.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS delivery_boys (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT
)
""")

# Default entries
conn.execute("INSERT INTO delivery_boys (name) VALUES ('Papa')")
conn.execute("INSERT INTO delivery_boys (name) VALUES ('Lakshya')")

conn.commit()

print("Delivery table ready")

conn.close()
