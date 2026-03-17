import sqlite3

conn = sqlite3.connect("database.db")

try:
    conn.execute("ALTER TABLE orders ADD COLUMN delivery_boy TEXT")
    print("delivery_boy column added")
except:
    print("Column already exists")

conn.commit()
conn.close()
