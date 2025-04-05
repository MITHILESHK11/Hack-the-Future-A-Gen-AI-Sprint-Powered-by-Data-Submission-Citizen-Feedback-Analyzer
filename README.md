# 🗳️ Citizen Feedback Analyzer - Hack the Future 🚀

An intelligent, Gemini-powered feedback analysis system built with **Streamlit** and **Google Gemini API** that transforms raw citizen feedback into actionable insights — including **sentiment**, **department classification**, **explanations**, **batch analysis from Excel**, and **analytics dashboard**.

---

## 🔍 Features

✅ Analyze single or multiple feedback entries  
✅ Sentiment Detection (Positive, Negative, Neutral)  
✅ Department Classification (e.g., Sanitation, Roads, Water, Electricity, etc.)  
✅ Explanation for each feedback’s sentiment  
✅ Excel/CSV upload for batch feedback analysis  
✅ Interactive dashboard with sentiment and department charts  
✅ Multilingual input support  
✅ Download results as CSV  
✅ API key input via sidebar or `.env`/Streamlit secrets

---

## 🧠 Powered By

- [Google Gemini Pro API](https://ai.google.dev/)
- [Streamlit](https://streamlit.io/)
- [Matplotlib + Pandas](https://pandas.pydata.org/)

---

## 📦 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/MITHILESHK11/Hack-the-Future-A-Gen-AI-Sprint-Powered-by-Data-Submission-Citizen-Feedback-Analyzer.git
cd Hack-the-Future-A-Gen-AI-Sprint-Powered-by-Data-Submission-Citizen-Feedback-Analyzer
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Your API Key

You can use **any one** of these methods:

#### Option A: Use `.env` file (for local use)
Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

#### Option B: Use the sidebar input (recommended for testing)

When the app runs, input the API key in the sidebar textbox.

#### Option C: Streamlit Cloud Secrets (for deployment)

If deploying to [Streamlit Cloud](https://share.streamlit.io), add this in **Settings → Secrets**:

```toml
GEMINI_API_KEY = "your_gemini_api_key_here"
```

---

## 🚀 Run the App

```bash
streamlit run app.py
```

---

## 📊 Sample Output

- Upload an Excel file with a `feedback` column (see `sample_feedback.xlsx`)
- Results include:
  - Sentiment
  - Department
  - Explanation
  - Visual charts
  - Download button for CSV

---

## 🛠 Project Structure

```
├── app.py                  # Main Streamlit app
├── gemini_utils.py         # API integration logic
├── requirements.txt        # Dependencies
├── .env                    # API key file (not pushed)
├── .gitignore              # To hide .env
└── README.md               # Project instructions
```

---

## 📂 Sample Excel Format

```plaintext
| feedback                         |
|----------------------------------|
| The garbage collection is poor. |
| Water supply is very regular.   |
| Power cuts are frequent.        |
```

---

## 🤖 Example Prompt to Gemini

```
"You are an intelligent assistant. Analyze the following citizen feedback and return:

1. Sentiment (Positive, Negative, Neutral)
2. Department it relates to
3. Short explanation for the sentiment

Feedback: 'The water supply has been erratic for two weeks.'"
```

---

## 🔐 Important Notes

- Your `.env` file is excluded from Git via `.gitignore`
- Never commit your Gemini API key to GitHub
- Supports multilingual feedback like Hindi, Tamil, Telugu, etc.

---

## 🧠 Future Enhancements (Ideas)

- Add login authentication  
- Real-time chatbot for user feedback  
- Geo-tagging for location-based feedback  
- Auto-email reports to departments  
- Feedback severity scoring

---

## 🙌 Contribution & Credits

Built with ❤️ for the [Hack the Future - Gen AI Sprint 🚀].  
Developed by: **Mithilesh K.**  
Model by: **Google Gemini Pro**  
Frontend: **Streamlit**

---

## 📎 License

MIT License – free to use with credit.
```

---

Let me know if you'd like me to help you:
- Add a badge section (e.g., "Built with Gemini", "Made with Streamlit")
- Generate a project thumbnail or preview GIF
- Deploy it on Streamlit Cloud and include the public link

You're almost ready to win that hackathon 💪✨
