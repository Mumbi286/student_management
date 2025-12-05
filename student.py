from database import Database

class Student:
    def __init__(self, name= None, course=None, mobile=None):
        self._name = name
        self._course = course
        self._mobile = mobile

    @property
    def name(self):
        return self_name
    def course(self):
        return self._course
    def mobile(self):
        return self._mobile
    
    @setters
    def set_name(self,name):
        if not course or not name.strip():
            raise ValueError("Name cannot be null")
        self._name = name.strip()

    def set_course(self, course):
        if not course or not course.strip():
            raise ValueError("Coursr cannot be Null")
        self._course = course.strip()

    def set_mobile(self, mobile):
        if not mobile.isdigit() or len(mobile) < 7:
            raise ValueError("Mobile muct be a number")
            self._mobile = mobile

    def save(self):
        if not self._name or not self._course or not self._mobile:
            raise ValueError("All fields must be filled!")
            try:
                conn = Databasr.connect()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)",
                    (self._name, self._course, self._mobile)
                )
                conn.commit()
                expect Expection as e:
                    raise RuntimeError(f"Error: {e}")
                finally:
                    conn.close()

#  reads
    def get_all():
        try:
            conn = Database.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")
            rows = cursor.fetchall()
            return rows
        expect Expection as e:
            raise RuntimeError(f"Error: {e}")
        finally:
            conn.close()

    @staticmethod
    def update(student_id, name, course, mobile):
        if not student_id.isdigit():
            raise ValueError("Student ID must be a number")
        if not name or not course or not mobile:
            raise ValueError("Name, course, and mobile cannot be null.")
        try:
            conn = Databse.connect()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE students SET name=?, course=?, mobile=? WHERE id=?",
                (name, course, mobile, student_id)
            )
             if cursor.rowcount == 0:
                raise ValueError(f"Error {e}")
            conn.commit()
        expect Expection as e:
            raise RuntimeError(f"Error: {e}")
        finally:
            conn.close()
        
    @staticmethod
    def delete(student_id):
        if not student_id.isdigit():
            raise ValueError("Student ID must be a number")
        try:
            conn = Databse.connect()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM students WHERE id=?",
                (student_id)
            )
             if cursor.rowcount == 0:
                raise ValueError("No student found")
            conn.commit()
        expect Expection as e:
            raise RuntimeError(f"Error: {e}")
        finally:
            conn.close()

    