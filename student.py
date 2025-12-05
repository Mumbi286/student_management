from database import Database

class Student:
    def __init__(self, name, course, mobile):
        self._name = name
        self._course = course
        self._mobile = mobile


    # GETTERS
    @property
    def name(self):
        return self._name

    @property
    def course(self):
        return self._course

    @property
    def mobile(self):
        return self._mobile


    # SETTERS (Validation)
    @name.setter
    def set_name(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value.strip()

    @course.setter
    def set_course(self, value):
        if not value or not value.strip():
            raise ValueError("Course cannot be empty")
        self._course = value.strip()

    @mobile.setter
    def set_mobile(self, value):
        if not value.isdigit() or len(value) < 7:
            raise ValueError("Mobile must be digits and at least 7 characters")
        self._mobile = value

    
    def save(self):
        if not self._name or not self._course or not self._mobile:
            raise ValueError("All fields must be filled before saving")

        try:
            conn = Database.connect()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)",
                (self._name, self._course, self._mobile)
            )
            conn.commit()
        except Exception as e:
            raise RuntimeError(f"Error saving student: {e}")
        finally:
            conn.close()

    @staticmethod
    def get_all():
        try:
            conn = Database.connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            raise RuntimeError(f"Error reading students: {e}")
        finally:
            conn.close()


    # Updates a students records
    @staticmethod
    def update(student_id, name, course, mobile):
        if not student_id.isdigit():
            raise ValueError("Student ID must be a number")

        try:
            conn = Database.connect()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE students SET name=?, course=?, mobile=? WHERE id=?",
                (name, course, mobile, student_id)
            )

            if cursor.rowcount == 0:
                raise ValueError("No student found with that ID")

            conn.commit()
        except Exception as e:
            raise RuntimeError(f"Error updating student: {e}")
        finally:
            conn.close()

    
    # Delete a student record
    @staticmethod
    def delete(student_id):
        if not student_id.isdigit():
            raise ValueError("Student ID must be a number")

        try:
            conn = Database.connect()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM students WHERE id=?", (student_id,))

            if cursor.rowcount == 0:
                raise ValueError("No student found with that ID")

            conn.commit()
        except Exception as e:
            raise RuntimeError(f"Error deleting student: {e}")
        finally:
            conn.close()
