import sqlite3

# Connect to database
conn = sqlite3.connect('nyondo_stock.db')
cursor = conn.cursor()

# -------------------------------
# Create PRODUCTS table
# -------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL
)
""")

# -------------------------------
# Insert products
# -------------------------------
products = [
    ('Cement (bag)', 'Portland cement 50kg bag', 35000),
    ('Iron Sheet 3m', 'Gauge 30 roofing sheet 3m long', 110000),
    ('Paint 5L', 'Exterior wall paint white 5L', 60000),
    ('Nails 1kg', 'Common wire nails 1kg pack', 12000),
    ('Timber 2x4', 'Pine timber plank 2x4 per metre', 25000)
]

cursor.executemany("""
INSERT INTO products (name, description, price)
VALUES (?, ?, ?)
""", products)

# -------------------------------
# Create USERS table
# -------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    role TEXT DEFAULT 'attendant'
)
""")

# Insert users (avoid duplicates)
cursor.execute("""
INSERT OR IGNORE INTO users (id, username, password, role) VALUES
(1, 'admin', 'admin123', 'admin'),
(2, 'fatuma', 'pass456', 'attendant'),
(3, 'wasswa', 'pass789', 'manager')
""")

# -------------------------------
# Show all products
# -------------------------------
rows = cursor.execute("SELECT * FROM products").fetchall()

print("PRODUCTS TABLE:")
for r in rows:
    print(r)

conn.commit()
conn.close()
