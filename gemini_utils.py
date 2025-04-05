import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def load_gemini(api_key=None):
    key = api_key or os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=key)
    return genai.GenerativeModel('gemini-2.0-flash')

def analyze_feedback(model, feedback_text):
    prompt = f"""
    You are analyzing citizen feedback.

    Task:
    1. Detect sentiment: Positive, Negative, or Neutral.
    2. Identify responsible department: sanitation, roads, traffic, water, electricity, healthcare.
    3. Explain briefly why you chose that sentiment.

    Feedback: {feedback_text}
    """
    response = model.generate_content(prompt)
    return response.text.strip()
