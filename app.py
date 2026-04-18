import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.set_page_config(page_title="BugSense AI", layout="centered")

# Configure Gemini API
API_KEY = os.getenv("GEMINI_API_KEY")

st.title("🐞 BugSense AI")
st.markdown("Upload your test failure logs below, and our AI will automatically summarize the error and suggest fixes.")

if not API_KEY or API_KEY == "your_copied_api_key_here":
    st.warning("⚠️ Please configure your valid GEMINI_API_KEY in the .env file to use the AI capabilities.")
else:
    genai.configure(api_key=API_KEY)

with st.container():
    uploaded_file = st.file_uploader("Upload Test Log File", type=["log", "txt", "json"])

def generate_summary(log_text):
    prompt = f"""
    You are an expert QA Automation Engineer. I am providing you with a test failure log.
    Please analyze it and provide a concise summary of the issue, the root cause if visible, and a suggested fix.
    
    Test Log Content:
    {log_text}
    """
    
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred while communicating with the Gemini API: {str(e)}"

if uploaded_file is not None:
    st.success("File uploaded successfully. Processing...")
    
    # Read the file content
    log_content = uploaded_file.getvalue().decode("utf-8")
    
    with st.expander("View Uploaded Log Content"):
        st.code(log_content, language="text")
    
    if API_KEY and API_KEY != "your_copied_api_key_here":
        with st.spinner("Analyzing the log with Gemini..."):
            ai_summary = generate_summary(log_content)
        
        st.subheader("🤖 AI Analysis")
        st.markdown(ai_summary)
    else:
        st.error("Cannot process log: missing valid GEMINI_API_KEY.")
