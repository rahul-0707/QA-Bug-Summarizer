# BugSense AI: Project Report

## 1. Project Overview
* **Project Title:** BugSense AI: Automated QA Log Summarizer & Root Cause Analyzer
* **Candidate Name:** Rahul Singh Parihar
* **Course:** MCA 4th Semester (Student ID: 24711001)
* **Project Domain:** Software Quality Assurance (QA) & Artificial Intelligence (AI)

## 2. Abstract & Problem Statement
In modern software development, QA engineers generate massive log data during automated testing. Analyzing lengthy raw logs to find the "Root Cause" of a failed test is time-consuming and prone to human error. **BugSense AI** bridges this gap by leveraging Large Language Models (LLMs) to automatically analyze failed test logs and generate concise, human-readable summaries, error locations, and suggested fixes.

**Key Problems Solved:**
* **Log Overload:** Automated test reports are often too technical and lengthy.
* **Manual Effort:** Significant manual effort is wasted identifying whether a failure is a "Script Issue" or a "Product Bug."
* **Communication Gap:** Stakeholders struggle to understand raw technical error messages.

## 3. Project Objectives
* Automate the extraction of error patterns from raw bug and log files.
* Integrate Generative AI (Google Gemini) for intelligent log interpretation.
* Provide an intuitive web-based dashboard for easy log uploading and report generation.
* Enhance the debugging speed within the Software Testing Life Cycle (STLC).

## 4. Technology Stack
* **Programming Language:** Python 3.x
* **Web Framework (UI):** Streamlit (for building an interactive application)
* **AI Engine:** Google Gemini API (gemini-2.5-flash)
* **Testing Integration:** Pytest (used to generate mock error logs) / Playwright
* **Version Control:** Git & GitHub
* **Deployment:** Streamlit Cloud (Free Hosting)

## 5. Project Workflow & System Architecture
The application runs as a fully contained web dashboard that uses the following workflow:

### **Step 1: Input Layer (Uploading Logs)**
* The user uploads a failed test log file (e.g., `test_failure.txt`, `sample_log.txt`) directly via the Streamlit drag-and-drop dashboard interface. 
* Logs can be generated locally using `pytest` (as demonstrated in `mock_test.py`).

### **Step 2: Processing Layer (Parsing)**
* The Python (`app.py`) script decodes and reads the file to identify the raw error traces, timeout instances, and failing assertions (like 404/500 Errors).
* It aggregates the log text for AI processing.

### **Step 3: AI Integration Layer (Generative Analysis)**
* The parsed log snippet is combined with a customized prompt: *"You are an expert QA Automation Engineer. I am providing you with a test failure log. Please analyze it and provide a concise summary of the issue, the root cause if visible, and a suggested fix."*
* This prompt is securely dispatched to the Google Gemini AI Model (`gemini-2.5-flash`), authenticated via environment variables (`.env`).

### **Step 4: Output Layer (Results Presentation)**
* The AI engine processes the test failure log and returns a structured, human-readable analysis to the Streamlit UI.
* **Displays:** The result includes an Error Category summary, a simplified non-technical explanation, and actionable fixes/insights.

## 6. Key Features
* **Drag-and-Drop Interface:** Simple and fast UI optimized for non-coders.
* **Actionable Insights:** Delivers detailed resolution steps instead of just stating the error.
* **Zero-Cost Setup:** Utilizes highly capable, yet free API tiers and open-source packages.
* **Mock Testing Suite Included:** Project ships with a `mock_test.py` allowing instant demonstration by simulating standard backend assertions (`AssertionError: 500`) or UI failures (`TimeoutError: 30000ms`).

## 7. How to Setup and Run
If the application needs to be run locally, follow these steps:
1. Ensure Python 3.x is installed. 
2. Set up the environment variables: Create a `.env` file in the root directory and add `GEMINI_API_KEY=your_copied_api_key_here`.
3. Activate the virtual environment with `.\venv\Scripts\activate` (Windows).
4. Install dependencies: `pip install -r requirements.txt`.
5. Run the web interface: `python -m streamlit run app.py`.
6. Upload a test log. To generate a sample dummy log, simply run `python -m pytest mock_test.py > test_failure.txt` and upload `test_failure.txt`.

## 8. Future Scope
* **Defect Management Integration:** Auto-creating bug tickets directly in Jira or Azure DevOps using the AI-generated JSON summary.
* **Smart Categorization:** Automatically tagging bugs as "High," "Medium," or "Low" priority based on AI severity calculation.

## 9. Conclusion
By unifying Python’s UI automation mechanics (Streamlit) with AI’s intuitive reasoning engines (Gemini), BugSense AI heavily reduces QA debugging bottlenecks, letting developers focus on shipping quality software over manual log investigation.
