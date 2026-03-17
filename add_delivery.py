import sqlite3

conn = sqlite3.connect("database.db")

conn.execute("ALTER TABLE orders ADD COLUMN delivery_boy TEXT")

conn.commit()

print("Delivery column added")

conn.close()
