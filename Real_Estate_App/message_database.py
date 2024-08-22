import sqlite3

# Function to insert data into the database
def insert_into_db(name, email, message):
    conn = sqlite3.connect('contact_form.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO user_queries (name, email, message)
        VALUES (?, ?, ?)
    ''', (name, email, message))
    conn.commit()
    conn.close()

# Create database and table if not exists
def create_database():
    conn = sqlite3.connect('contact_form.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_queries (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialize database
create_database()
