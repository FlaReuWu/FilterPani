import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("DELETE FROM products")

cursor.execute("INSERT INTO products (name, price) VALUES ('20L Jar',50)")
cursor.execute("INSERT INTO products (name, price) VALUES ('1L Pack (12 Bottles)',120)")
cursor.execute("INSERT INTO products (name, price) VALUES ('500ml Pack (20 Bottles)',140)")
cursor.execute("INSERT INTO products (name, price) VALUES ('250ml Pack (30 Bottles)',150)")

conn.commit()

print("Products updated successfully")

conn.close()
