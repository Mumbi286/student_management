import sqlite3

DB_NAME = "database.db"

def connection():
    return sqlite3.connect(DB_NAME)