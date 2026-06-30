import sqlite3

conn = sqlite3.connect("campus.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    roll TEXT UNIQUE,
    department TEXT,
    semester TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS teachers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    department TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT,
    teacher TEXT,
    credit_hours INTEGER
)
""")

# Assignments Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS assignments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    assignment TEXT,
    subject TEXT,
    due_date TEXT,
    status TEXT
)
""")

# Grades Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS grades(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student TEXT,
    roll TEXT,
    subject TEXT,
    marks INTEGER,
    grade TEXT
)
""")
# Timetable Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS timetable(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    day TEXT,
    time TEXT,
    course TEXT,
    teacher TEXT,
    room TEXT
)
""")


# Default Admin Account
cursor.execute("""
INSERT OR IGNORE INTO users(username,password,role)
VALUES('admin','admin123','Admin')
""")
# Sample Students
cursor.execute("SELECT COUNT(*) FROM students")
count = cursor.fetchone()[0]

if count == 0:
    cursor.execute("""
    INSERT INTO students(name, roll, department, semester)
    VALUES
    ('Mushtaq','23-CS-001','Cyber Security','1'),
    ('Hamza','23-CS-002','Cyber Security','1'),
    ('Abdullah','23-CS-003','Cyber Security','1')
    """)

# Sample Teachers
cursor.execute("SELECT COUNT(*) FROM teachers")

if cursor.fetchone()[0] == 0:

    cursor.execute("""
    INSERT INTO teachers(name, department)
    VALUES
    ('Sir Mohsin Chaudhary', 'Computer Science'),
    ('Sir Zain', 'Mathematics'),
    ('Sir Mujtaba', 'Cyber Security')
    """)

# Sample Courses
cursor.execute("SELECT COUNT(*) FROM courses")

if cursor.fetchone()[0] == 0:

    cursor.execute("""
    INSERT INTO courses(course_name, teacher, credit_hours)
    VALUES
    ('Programming Fundamentals', 'Maam Beenish', 3),
    ('Calculus', 'Sir Shafiq', 3),
    ('Database Systems', 'Maam Bilawal Bhutto', 3)
    """)

# Sample Grades
cursor.execute("SELECT COUNT(*) FROM grades")

if cursor.fetchone()[0] == 0:

    cursor.execute("""
    INSERT INTO grades(student, roll, subject, marks, grade)
    VALUES
    ('Abdullah', '23-CS-003', 'Programming Fundamentals', 92, 'A+'),
    ('Hamza', '23-CS-002', 'Calculus', 81, 'A'),
    ('Mushtaq', '23-CS-001', 'Database Systems', 74, 'B')
    """)

# Sample Timetable
cursor.execute("SELECT COUNT(*) FROM timetable")

if cursor.fetchone()[0] == 0:

    cursor.execute("""
    INSERT INTO timetable(day, time, course, teacher, room)
    VALUES
    ('Monday','08:30 AM - 10:00 AM','Programming Fundamentals','Maam Beenish','Lab-1'),
    ('Monday','10:15 AM - 11:45 AM','Calculus','Sir Shafiq','Room-203'),

    ('Tuesday','08:30 AM - 10:00 AM','Database Systems','Maam Bilawal Bhutto','Lab-2'),
    ('Tuesday','10:15 AM - 11:45 AM','Cyber Security Fundamentals','Sir Mujtaba','Room-305'),

    ('Wednesday','08:30 AM - 10:00 AM','Programming Fundamentals','Maam Beenish','Lab-1'),
    ('Wednesday','10:15 AM - 11:45 AM','English Composition','Maam Ayesha','Room-104'),

    ('Thursday','08:30 AM - 10:00 AM','Calculus','Sir Shafiq','Room-203'),
    ('Thursday','10:15 AM - 11:45 AM','Database Systems','Maam Bilawal Bhutto','Lab-2'),

    ('Friday','08:30 AM - 10:00 AM','Cyber Security Fundamentals','Sir Mujtaba','Room-305'),
    ('Friday','10:15 AM - 11:45 AM','Islamic Studies','Sir Zain','Room-101')
    """)

# Sample Assignments
cursor.execute("SELECT COUNT(*) FROM assignments")

if cursor.fetchone()[0] == 0:

    cursor.execute("""
    INSERT INTO assignments(
        assignment,
        subject,
        due_date,
        status
    )
    VALUES
    ('PF Project', 'Programming Fundamentals', '30-06-2026', 'Pending'),
    ('Calculus Assignment 1', 'Calculus', '02-07-2026', 'Submitted'),
    ('Database ERD', 'Database Systems', '05-07-2026', 'Pending')
    """)

conn.commit()
conn.close()
