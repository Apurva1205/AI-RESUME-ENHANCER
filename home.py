import streamlit as st
from PIL import Image
import os

def show_home_page():
    """Displays the interactive home page for Resume AI"""

    # Hero Section - Load banner image
    image_path = os.path.join("assets", "index_banner.jpg")  # Ensure this file exists

    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)
    else:
        st.error(f"⚠️ Image not found: {image_path}")

    # Title & Subtitle
    st.markdown("<h1 style='text-align: center; color: #2E3B55;'>Welcome to Smart Resume AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Optimize your resume and job search with AI-powered tools.</p>", unsafe_allow_html=True)

    # Call-to-Action Buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📄 Create a Resume", key="resume"):
            st.session_state.page = "builder"
    with col2:
        if st.button("🔍 Analyze My Resume", key="analyze"):
            st.session_state.page = "analyzer"

    # Resume Templates Section
    st.markdown("## Choose a Resume Template")
    col1, col2, col3 = st.columns(3)

    # Template images paths
    template1_path = os.path.join("assets", "template1.jpg")
    template2_path = os.path.join("assets", "template2.jpg")
    template3_path = os.path.join("assets", "template3.jpg")

    # Load templates only if they exist
    with col1:
        if os.path.exists(template1_path):
            st.image(template1_path, caption="Modern Resume", use_container_width=True)
        else:
            st.error(f"❌ Missing: {template1_path}")

    with col2:
        if os.path.exists(template2_path):
            st.image(template2_path, caption="Professional Resume", use_container_width=True)
        else:
            st.error(f"❌ Missing: {template2_path}")

    with col3:
        if os.path.exists(template3_path):
            st.image(template3_path, caption="Creative Resume", use_container_width=True)
        else:
            st.error(f"❌ Missing: {template3_path}")

    # Feature Highlights
    st.markdown("## Why Use Smart Resume AI?")
    st.markdown("""
    - ✅ AI-powered resume optimization
    - ✅ ATS-friendly formatting
    - ✅ Instant feedback and suggestions
    - ✅ Job-matching recommendations
    """)

    # Testimonial Section
    st.markdown("## What Users Say")
    st.success("🚀 'This tool helped me land my dream job in just 2 weeks!' - Alex")
    st.info("💡 'I love how it suggests improvements in real-time!' - Sarah")
