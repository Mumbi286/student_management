from database import connection

def add_student(name, course, mobile):
    conn =  connection()
    cursor = conn.cursor()
    cursor.execute(
        "" INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)"",
        (name, curse, mobile)
    )
    conn.commit()
    conn.close()

def view_student():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_student(keyword):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM students WHERE name LIKE ? OR moblie LIKE ?",
        (f"%{keyword}, %{keyword}, %{keyword}")
    )