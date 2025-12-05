from database import connection

# Adds a student
def add_student(name, course, mobile):
    conn =  connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)",
        (name, curse, mobile)
    )
    conn.commit()
    conn.close()

# Update the student record
def view_student():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

# search if the student exists
def search_student(keyword):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM students WHERE name LIKE ? OR moblie LIKE ?",
        (f"%{keyword}, %{keyword}, %{keyword}")
    )
    rows = cursor.fetchall()
    conn.close()
    return rows

# Update the students records
def update_student(student_id, name,course, mobile):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET name=?, course=?, mobile=? WHERE id=?",
        (name, course, mobile, student_id)
    )
    conn.commit()
    conn.close()

# Delete a student record from the database
def delete_student(student_id):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (student_id))
    conn.commit()
    conn.close()