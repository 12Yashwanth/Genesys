#To display database content in terminal for testing purposes
import sqlite3

conn = sqlite3.connect("contact.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM contacts")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()