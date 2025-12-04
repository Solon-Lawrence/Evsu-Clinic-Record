import sqlite3

conn=sqlite3.connect("student_clinic_record.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS staff  (
    staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    sex TEXT,
    courses TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS medical_records (
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    reason TEXT,
    vital_sign TEXT,
    assessment TEXT,
    treatment_given TEXT,
    medicine_given TEXT,
    remarks TEXT,
    date TEXT,
    FOREIGN KEY(student_id) REFERENCES students(student_id)
)
""")

conn.commit()

conn.close()

print("Database and tables created successfully")