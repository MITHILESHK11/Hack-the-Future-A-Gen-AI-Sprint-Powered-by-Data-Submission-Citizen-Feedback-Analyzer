import google.generativeai as genai

# Load Gemini model with API key
def load_gemini(api_key):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-2.5-pro-preview-03-25')

# Analyze sentiment and department using Gemini
def analyze_feedback(model, feedback_text):
    prompt = f"""
    Analyze the following citizen feedback.
    Provide:
    1. Sentiment: (Positive / Negative / Neutral)
    2. Responsible Department (choose from: sanitation, roads, traffic, water, electricity, healthcare).

    Feedback: {feedback_text}
    """
    response = model.generate_content(prompt)
    return response.text.strip()
