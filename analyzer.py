import joblib
import streamlit as st
from pdfplumber import open as open_pdf
from docx import Document

# --------------- Define the ResumeEnhancer Class ---------------
class ResumeEnhancer:
    def __init__(self):
        # Initialize any necessary parameters
        pass
    
    def predict(self, input_data):
        # Example prediction logic, replace with your model's actual logic
        return ["High", "Medium", "Low", "High"]  # Example output

# ------------------ Function to Load Model ----------------------
def load_model():
    """Loads the model from the pickle file."""
    model_path = r"C:\Users\apurv\AI Resume Enhancer\resume_enhancer1(1).pkl"
    try:
        print(f"Attempting to load model from: {model_path}")
        model = joblib.load(model_path)
        print(f"Model loaded successfully: {type(model)}")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

# ------------------ Extract Text Functions ----------------------
def extract_text_from_docx(docx_file):
    """Extracts text from a DOCX file."""
    doc = Document(docx_file)
    text = []
    for para in doc.paragraphs:
        text.append(para.text)
    return "\n".join(text)

def extract_text_from_pdf(pdf_file):
    """Extracts text from a PDF file."""
    with open_pdf(pdf_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
        return text

# ------------------ Main Analyzer Page -------------------------
def show_analyzer_page():
    st.title("AI Resume Analyzer")
    st.write("Upload your resume for instant feedback.")
    
    uploaded_file = st.file_uploader("Choose a resume file", type=["pdf", "docx", "txt"])
    job_description = st.text_area("Job Description", height=300)
    
    if st.button("Analyze"):
        if uploaded_file is None:
            st.error("⚠️ Please upload a resume file before analyzing.")
            return

        st.success("✅ Analysis in progress...")
        st.write(f"File uploaded: **{uploaded_file.name}**")

        resume_text = ""
        if uploaded_file.type == "text/plain":
            resume_text = uploaded_file.read().decode("utf-8")
        elif uploaded_file.type == "application/pdf":
            resume_text = extract_text_from_pdf(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            resume_text = extract_text_from_docx(uploaded_file)

        st.text_area("Resume Content", resume_text, height=300)

        if job_description:
            st.write("### Job Description Provided:")
            st.write(job_description)

        # Load the model and make predictions
        model = load_model()
        if model is None:
            st.error("⚠️ Failed to load model.")
            return

        processed_resume = resume_text.lower()  # Preprocess the resume text
        processed_job_desc = job_description.lower()  # Preprocess the job description text

        try:
            # Make predictions
            analysis_result = model.predict([processed_resume, processed_job_desc])
            st.write("### AI Analysis Results:")
            st.write(f"Skills Match: {analysis_result[0]}")
            st.write(f"Experience Match: {analysis_result[1]}")
            st.write(f"Education Match: {analysis_result[2]}")
            st.write(f"Overall Fit: {analysis_result[3]}")
        except Exception as e:
            st.error(f"⚠️ Error during prediction: {e}")
