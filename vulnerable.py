import sqlite3

conn = sqlite3.connect('nyondo_stock.db')

# -------------------------------
# VALIDATION FUNCTIONS
# -------------------------------
def valid_name(name):
    return isinstance(name, str) and len(name) >= 2 and "<" not in name and ">" not in name and ";" not in name

def valid_username(username):
    return isinstance(username, str) and username != "" and " " not in username

def valid_password(password):
    return isinstance(password, str) and len(password) >= 6

# -------------------------------
# SAFE SEARCH WITH VALIDATION
# -------------------------------
def search_product_safe(name):
    if not valid_name(name):
        print("Invalid product name")
        return None

    query = "SELECT * FROM products WHERE name LIKE ?"
    return conn.execute(query, (f"%{name}%",)).fetchall()

# -------------------------------
# SAFE LOGIN WITH VALIDATION
# -------------------------------
def login_safe(username, password):
    if not valid_username(username):
        print("Invalid username")
        return None

    if not valid_password(password):
        print("Invalid password")
        return None

    query = "SELECT * FROM users WHERE username=? AND password=?"
    return conn.execute(query, (username, password)).fetchone()

# -------------------------------
# TEST CASES
# -------------------------------
print(search_product_safe('cement'))       # works
print(search_product_safe(''))             # rejected
print(search_product_safe('<script>'))     # rejected

print(login_safe('admin', 'admin123'))     # works
print(login_safe('admin', 'ab'))           # rejected
print(login_safe('ad min', 'pass123'))     # rejected
