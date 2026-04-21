import sqlite3

conn = sqlite3.connect('nyondo_stock.db')
cursor = conn.cursor()

# # Query A
# print("A:", cursor.execute("SELECT * FROM products").fetchall())

# # Query B
# print("B:", cursor.execute("SELECT name, price FROM products").fetchall())

# # # Query C
# print("C:", cursor.execute("SELECT * FROM products WHERE id = 3").fetchall())

# # # Query D
# print("D:", cursor.execute("SELECT * FROM products WHERE name LIKE '%sheet%'").fetchall())

# # # Query E
# print("E:", cursor.execute("SELECT * FROM products ORDER BY price DESC").fetchall())

# # # Query F
# print("F:", cursor.execute("SELECT * FROM products ORDER BY price DESC LIMIT 2").fetchall())

# # # Query G (Update)
cursor.execute("UPDATE products SET price = 38000 WHERE id = 1")
conn.commit()

# print("G:", cursor.execute("SELECT * FROM products").fetchall())

conn.close()
