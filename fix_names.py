import sqlite3

conn = sqlite3.connect("database.db")

# Replace old name Rahul → Papa
conn.execute("UPDATE orders SET delivery_boy='Papa' WHERE delivery_boy='Rahul'")

# Replace old name Aman → Lakshya
conn.execute("UPDATE orders SET delivery_boy='Lakshya' WHERE delivery_boy='Aman'")

conn.commit()

print("Names updated successfully")

conn.close()
