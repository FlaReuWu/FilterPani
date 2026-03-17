import sqlite3

conn = sqlite3.connect("database.db")

conn.execute("ALTER TABLE orders ADD COLUMN status TEXT DEFAULT 'Pending'")

conn.commit()

print("Database updated")

conn.close()
