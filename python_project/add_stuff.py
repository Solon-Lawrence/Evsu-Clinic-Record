import sqlite3

conn = sqlite3.connect("student_clinic_record.db")
cursor = conn.cursor()

cursor.execute("""
INSERT OR IGNORE INTO staff (username, password)
VALUES (?, ?)
""", ("admin", "12345"))

conn.commit()
conn.close()

print("Default staff account created (username: admin / password: 12345)")
