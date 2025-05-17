import mysql.connector

def connect_db():
    """Connects to MySQL database."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="resume_ai"
    )
