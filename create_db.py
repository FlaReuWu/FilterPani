import sqlite3

conn = sqlite3.connect("database.db")

conn.execute("""
CREATE TABLE products(
id INTEGER PRIMARY KEY,
name TEXT,
price INTEGER
)
""")

conn.execute("""
CREATE TABLE orders(
id INTEGER PRIMARY KEY,
name TEXT,
phone TEXT,
address TEXT,
product TEXT,
quantity INTEGER
)
""")

conn.execute("INSERT INTO products (name, price) VALUES ('20L Water Jar',50)")
conn.execute("INSERT INTO products (name, price) VALUES ('1L Bottle',10)")
conn.execute("INSERT INTO products (name, price) VALUES ('Water Pump',120)")
conn.execute("INSERT INTO products (name, price) VALUES ('Jar Cap',5)")

conn.commit()
conn.close()

print("Database created")
