import joblib
from resume_enhancer_model import ResumeEnhancer

enhancer = ResumeEnhancer()
joblib.dump(enhancer, "resume_enhancer1(1).pkl")


