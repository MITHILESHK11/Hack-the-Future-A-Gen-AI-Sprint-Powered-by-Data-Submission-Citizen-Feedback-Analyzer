import streamlit as st
import pandas as pd
from gemini_utils import load_gemini, analyze_feedback

st.set_page_config(page_title="Citizen Feedback Analyzer", layout="wide")

# Sidebar: API Key
st.sidebar.title("🔐 Gemini API Setup")
api_key = st.sidebar.text_input("Enter your Gemini API Key", type="password")

# Main App
st.title("📣 Citizen Feedback Analyzer using Gemini AI")

if api_key:
    model = load_gemini(api_key)

    # User Input
    feedback = st.text_area("📝 Enter citizen feedback here", height=200)

    if st.button("Analyze Feedback"):
        if feedback.strip():
            with st.spinner("Analyzing with Gemini..."):
                result = analyze_feedback(model, feedback)

            # Parse response
            lines = result.split("\n")
            sentiment = ""
            department = ""
            for line in lines:
                if "Sentiment" in line:
                    sentiment = line.split(":")[-1].strip()
                elif "Department" in line:
                    department = line.split(":")[-1].strip()

            # Show result
            st.success("✅ Analysis Completed")
            st.write(f"**Sentiment:** {sentiment}")
            st.write(f"**Department:** {department}")

            # Optional: Save to CSV
            df = pd.DataFrame([{"Feedback": feedback, "Sentiment": sentiment, "Department": department}])
            try:
                old_df = pd.read_csv("sample_feedback.csv")
                df = pd.concat([old_df, df], ignore_index=True)
            except:
                pass
            df.to_csv("sample_feedback.csv", index=False)

        else:
            st.warning("Please enter feedback text.")

    # Show existing feedback
    st.subheader("📊 Feedback History")
    try:
        df = pd.read_csv("sample_feedback.csv")
        st.dataframe(df)
    except:
        st.info("No feedback submitted yet.")
else:
    st.warning("Please enter your Gemini API key in the sidebar.")
