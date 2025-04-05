import streamlit as st
import pandas as pd
import plotly.express as px
from gemini_utils import load_gemini, analyze_feedback
import os

st.set_page_config(page_title="Citizen Feedback Analyzer", layout="wide")

# Sidebar for API key
st.sidebar.title("🔐 API Configuration")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")
model = load_gemini(api_key) if api_key else None

# Upload Excel section
st.subheader("📥 Upload Excel/CSV for Bulk Analysis")
uploaded_file = st.file_uploader("Upload a file with a 'Feedback' column", type=["xlsx", "csv"])

if uploaded_file and api_key:
    ext = uploaded_file.name.split('.')[-1]
    df_upload = pd.read_csv(uploaded_file) if ext == "csv" else pd.read_excel(uploaded_file)

    if "Feedback" not in df_upload.columns:
        st.error("The uploaded file must contain a 'Feedback' column.")
    else:
        if st.button("Analyze All Feedback"):
            result_data = []
            with st.spinner("Analyzing..."):
                for fb in df_upload["Feedback"]:
                    res = analyze_feedback(model, fb)
                    sentiment = department = explanation = ""
                    for line in res.split("\n"):
                        if "Sentiment" in line: sentiment = line.split(":")[-1].strip()
                        elif "Department" in line: department = line.split(":")[-1].strip()
                        elif "Explain" in line or "Reason" in line: explanation = line.split(":")[-1].strip()
                    result_data.append({
                        "Feedback": fb,
                        "Sentiment": sentiment,
                        "Department": department,
                        "Reason": explanation
                    })

            df_result = pd.DataFrame(result_data)
            st.success("✅ Analysis complete!")
            st.dataframe(df_result)

            # Download
            st.download_button("⬇️ Download CSV", data=df_result.to_csv(index=False), file_name="analyzed_feedback.csv")

            # Plot
            st.subheader("📊 Feedback Insights")
            st.plotly_chart(px.histogram(df_result, x="Sentiment", color="Sentiment", title="Sentiment Distribution"))
            st.plotly_chart(px.histogram(df_result, x="Department", color="Department", title="Department Distribution"))

# Manual input section
st.subheader("📝 Enter Feedback Manually")
feedback = st.text_area("Feedback text here")

if st.button("Analyze Single Feedback") and api_key:
    if feedback.strip():
        with st.spinner("Analyzing..."):
            result = analyze_feedback(model, feedback)
        sentiment = department = explanation = ""
        for line in result.split("\n"):
            if "Sentiment" in line: sentiment = line.split(":")[-1].strip()
            elif "Department" in line: department = line.split(":")[-1].strip()
            elif "Explain" in line or "Reason" in line: explanation = line.split(":")[-1].strip()

        st.success("✅ Analysis done!")
        st.write(f"**Sentiment:** {sentiment}")
        st.write(f"**Department:** {department}")
        st.write(f"**Reason:** {explanation}")
    else:
        st.warning("Please enter some feedback.")
elif not api_key:
    st.info("Please provide your Gemini API key in the sidebar.")
