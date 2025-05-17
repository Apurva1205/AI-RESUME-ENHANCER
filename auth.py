
import streamlit as st
from werkzeug.security import check_password_hash, generate_password_hash
import mysql.connector

# Database Connection
def connect_db():
    """Connects to MySQL database."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="resume_ai"
    )

# Function to register a user
def signup():
    st.title("Sign Up")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        if password != confirm_password:
            st.error("⚠️ Passwords do not match.")
        else:
            conn = connect_db()
            cursor = conn.cursor()
            hashed_password = generate_password_hash(password)

            try:
                cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                               (username, email, hashed_password))
                conn.commit()
                st.success("✅ Account created successfully! Please login.")
            except mysql.connector.Error as err:
                st.error(f"❌ Error: {err}")
            finally:
                conn.close()

# Function to log in the user
def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE username=%s", (username,))
        user_data = cursor.fetchone()

        if user_data and check_password_hash(user_data[0], password):
            st.session_state.authenticated = True
            st.session_state.username = username
            st.success("✅ Login successful! Redirecting to Home Page...")
        else:
            st.error("❌ Invalid username or password.")
        conn.close()
