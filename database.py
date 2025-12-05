import sqlite3

class Database:
    DB_NAME = "database.db"

    @method
    def connect():
        """Connect the SQLite database."""
        return sqlite3.connect(Database.DB_NAME)

    @method
    def initialise():
        """Create tables if they don't exist"""
        conn = Database.connect()
        cursor = conn.cursor()

        #  The student table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            course TEXT NOT NULL,
            mobile TEXT NOT NULL
            )
        """)

        conn.commit()
        conn.close()
