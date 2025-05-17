import streamlit as st
from auth import login, signup
from home import show_home_page
from analyzer import show_analyzer_page  # Importing the analyzer module
from builder import show_builder_page
from dashboard import show_dashboard_page
from job_search import show_job_search_page
import mysql.connector
from werkzeug.security import check_password_hash

# ---------------------- Database Connection ----------------------
def connect_db():
    """Connects to MySQL database."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="resume_ai"
    )

# ---------------------- Main Streamlit App ----------------------
def main():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.session_state.page = "login"

    st.sidebar.title("ResumeCraft AI")

    if not st.session_state.authenticated:
        option = st.sidebar.radio("Choose an option", ["Login", "Sign Up"])
        if option == "Login":
            login()
        elif option == "Sign Up":
            signup()
    else:
        # Logged-in User Navigation
        st.sidebar.write(f"👋 Welcome, {st.session_state.username}")
        if st.sidebar.button("Logout"):
            st.session_state.authenticated = False
            st.session_state.username = None
            st.session_state.page = "login"
            st.rerun()  

        # Show Home Page & Navigation
        st.sidebar.title("Dashboard Sections")
        page = st.sidebar.radio("Go to", ["🏠 Home", "🔍 Resume Analyzer", "📄 Resume Builder", "📊 Dashboard", "🎯 Job Search"])

        if page == "🏠 Home":
            st.session_state.page = "home"
        elif page == "🔍 Resume Analyzer":
            st.session_state.page = "analyzer"
        elif page == "📄 Resume Builder":
            st.session_state.page = "builder"
        elif page == "📊 Dashboard":
            st.session_state.page = "dashboard"
        elif page == "🎯 Job Search":
            st.session_state.page = "job_search"

        # Page Routing
        if st.session_state.page == "home":
            show_home_page()
        elif st.session_state.page == "analyzer":
            show_analyzer_page()  # Calls the function from analyzer.py
        elif st.session_state.page == "builder":
            show_builder_page()
        elif st.session_state.page == "dashboard":
            show_dashboard_page()
        elif st.session_state.page == "job_search":
            show_job_search_page()

if __name__ == "__main__":
    main()
